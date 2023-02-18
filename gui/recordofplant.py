import os
import sqlite3
import tkinter as tk
import customtkinter
from gui import plant_list
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
from utils.util import get_image, small_label, create_header, clear, bttn
from crud.crud_db import get_plants

class RecordOfPlants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()

    def set_plant_list_reference(self, plant_list):
        self.plant_list = plant_list
        

    def create_widgets(self):
        self.background = get_image("add_plant.jpg", self)
        self.header = create_header(self, "Records of Plants", 110, 60)
        self.tabview = customtkinter.CTkTabview(self, fg_color="#f6f6f6", border_color="#f6f6f6", bg_color="#f6f6f6", height=300, width=320)
        self.tab1 = self.tabview.add("Add plant")
        self.tab2 = self.tabview.add("Update plant data")
        self.tab3 = self.tabview.add("Delete plant")
        self.tabview.set("Add plant")
        
        small_label(self.tab1, "Add plant", 10, 35)
        small_label(self.tab1, "Add Image", 10, 90)
        small_label(self.tab2, "Update plant", 10, 35)
        small_label(self.tab2, "Change Image", 10, 90)
        small_label(self.tab3, "Select plant", 10, 35)

        self.conn = sqlite3.connect('PyFlora.db')
        self.c = self.conn.cursor() 
        
        
        self.new_list = get_plants()
        self.add_entry_var = tk.StringVar()
        self.add_entry = customtkinter.CTkEntry(self.tab1, textvariable=self.add_entry_var, corner_radius=8, fg_color="#f6f6f6",text_color="black")
        
        self.open_button = customtkinter.CTkButton(master=self.tab1, width=90, text="Choose Image", height=10, compound="left")
        self.save_image = customtkinter.CTkImage(Image.open("media\icons8-save-100.png").resize((20, 20), Image.ANTIALIAS))
        self.save_button = customtkinter.CTkButton(master=self.tab1, width=90, image=self.save_image, text="Save",compound="left")
        
        self.dropmenu_var = tk.StringVar()
        self.dropmenu = ttk.OptionMenu(self.tab2, self.dropmenu_var, *self.new_list)
        
        self.update_var = tk.StringVar()
        self.update_image_entry = customtkinter.CTkEntry(self.tab2, textvariable=self.update_var, corner_radius=8, fg_color="#f6f6f6",text_color="black")
        self.change_button = customtkinter.CTkButton(master=self.tab2, width=90, text="Choose Image", height=10, compound="left")     
        self.update_image = customtkinter.CTkImage(Image.open("media\icons8-update-100.png").resize((20, 20), Image.ANTIALIAS))
        self.update_button = customtkinter.CTkButton(master=self.tab2, text="Update", image=self.update_image, width=100, height=10)
        
        self.del_plant_var = tk.StringVar()
        self.delete_plant_menu = ttk.OptionMenu(self.tab3, self.del_plant_var, *self.new_list)
        self.delete = customtkinter.CTkImage(Image.open("media\del.png").resize((20, 20), Image.ANTIALIAS))
        self.delete_button = customtkinter.CTkButton(master=self.tab3, text="Delete", fg_color="red2", hover_color="red3", image=self.delete, width=100, height=10)

        bttn(self, 300, 400, '  P L A N T   L I S T  ','#e6e6e6','white', lambda: self.controller.show_frame(plant_list.PlantList))
        
    def place_widgets(self):
        self.tabview.place(x=50, y=100)
        self.add_entry.place(x=145, y=30)
        self.dropmenu.place(x=210 ,y=30)
        self.update_image_entry.place()
        self.delete_plant_menu.place(x=210 ,y=30)
        self.open_button.place(x=195, y=90)
        self.change_button.place(x=195,y=90)
        self.save_button.place(x=100, y=170)
        self.update_button.place(x=100, y=170)
        self.delete_button.place(x=100, y=100)
        #self.home_button.place(x=300, y=400)

    def bind_widgets(self):
        self.open_button.configure(command=self.openFile)
        self.save_button.configure(command=self.insert_data)
        self.change_button.configure(command=self.changeFile)
        self.update_button.configure(command=self.update_data)
        self.delete_button.configure(command=self.delete_data)
    
    def updated_list(self):
        self.new_list.append(self.add_entry.get().capitalize())
        self.add_entry.delete(0, 'end')
        menu = self.dropmenu["menu"]
        menu.delete(0, "end")
        for plant in self.new_list:
            menu.add_command(label=plant, 
                command=lambda value=plant: self.dropmenu_var.set(value))
    
        menu = self.delete_plant_menu["menu"]
        menu.delete(0, "end")
        for del_plant in self.new_list:
            menu.add_command(label=del_plant, 
                command=lambda value=del_plant: self.del_plant_var.set(value))
            
    def delete_selected_item(self):
        selected = self.delete_plant_menu['menu'].index(self.del_plant_var.get())
        self.delete_plant_menu['menu'].delete(selected)
        self.del_plant_var.set(self.delete_plant_menu['menu'].entrycget(0,"label"))
        
        self.dropmenu['menu'].delete(selected)
        self.dropmenu_var.set(self.dropmenu['menu'].entrycget(0,"label"))

    def openFile(self):
        self.filepath = filedialog.askopenfilename(initialdir="C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media", filetypes=(('jpg', '*.jpg'),('png','*.png'),('All files','*.*'))) 
        self.base_filename = os.path.basename(self.filepath)
        self.file_label = ttk.Label(self.tab1, text=self.base_filename, background="#f6f6f6")
        self.file_label.place(x=105, y=90)
    
    def insert_data(self):
        self.read_file = open(self.filepath,'rb')
        self.read_file = self.read_file.read()

        try:
            self.c.execute("SELECT Plant FROM RecordsOfPlants WHERE (Plant=?)",
                        [self.add_entry.get().capitalize()])
            self.result = self.c.fetchone()

            if self.result:
                messagebox.showerror("Error", "Plant is already in the database!")
                clear(self.add_entry)
           
            elif self.add_entry.get() == '':
                messagebox.showerror("Error", "All fields are required!")
           
            else:
                self.c.execute("INSERT INTO RecordsOfPlants (Plant, Photo) VALUES (?,?)",
                        (self.add_entry.get().capitalize(), self.read_file))
                self.updated_list()
                
                self.conn.commit()
                messagebox.showinfo("Success", "Plant is successfully added!")
                clear(self.add_entry)
                self.file_label.destroy()

        except sqlite3.Error as error:
            print("Failed to add data", error)
        self.plant_list.refresh()

    def changeFile(self):
        
        self.filepath = filedialog.askopenfilename(initialdir="C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media", filetypes=(('jpg', '*.jpg'),('png','*.png'),('All files','*.*'))) 
        base_filename = os.path.basename(self.filepath)
        self.file_label = ttk.Label(self.tab2, text=base_filename, background="#f6f6f6")
        self.file_label.place(x=115, y=90)
    
    def insert_updated_data(self):

        self.read_file2 = open(self.filepath,'rb')
        self.read_file2 = self.read_file2.read()
        
        try:
            self.conn = sqlite3.connect('PyFlora.db')
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM RecordsOfPlants WHERE Plant=?",
                [self.dropmenu_var.get()])

            self.result = self.c.fetchone()
            
            if self.result:
                self.c.execute("UPDATE RecordsOfPlants set Photo=? WHERE Plant=?",
                    [self.read_file2, self.dropmenu_var.get()])

            self.conn.commit()
        
        except sqlite3.Error as error:
                print("Failed to update data", error)


    def check_if_plant_exists(self):
        
        self.c.execute("SELECT Plant FROM RecordsOfPlants WHERE (Plant=?)",
                [self.dropmenu_var.get()])

        self.result = self.c.fetchone()
        
        if self.result:
            self.insert_updated_data()
            messagebox.showinfo("Success", "Successfully updated plant!")
            
        else:
            messagebox.showerror(
                "Error", "The entered plant is not in database or doesn't match the plant_id")
            
    def update_data(self):
        
        try:
            self.check_if_plant_exists()
            self.file_label.destroy()
            messagebox.showerror("Error", "All fields are required !")
        
        except sqlite3.Error as error:
            print("Failed to update data", error)

    def delete_data(self):
        
        try:
            self.conn = sqlite3.connect('PyFlora.db')
            self.c = self.conn.cursor()
            
            self.c.execute("SELECT * FROM RecordsOfPlants WHERE Plant=?",
            [self.del_plant_var.get()])
            self.result = self.c.fetchone()
            
            if self.result:
                self.answer = messagebox.askyesno("Confirmation","Are you sure you want to delete selected plant?")
                if self.answer:
                    self.c.execute("DELETE FROM RecordsOfPlants WHERE Plant=?",
                    [self.del_plant_var.get()])
                    self.delete_selected_item()
                        
                self.conn.commit()
                messagebox.showinfo("Success", "Successfully deleted plant!")
            else:
                messagebox.showerror("Error","The entered plant is not in database!")
                clear(self.delete_plant_menu)

        except sqlite3.Error as error:
                print("Failed to update data", error)
    

    
import os
import sqlite3
import tkinter as tk
import customtkinter
from gui import pot_list
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from utils.util import get_image, small_label, create_header, clear, bttn
from crud.crud_db import get_plants, get_pots


class RecordOfPots(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()

    def set_pot_list_reference(self, pot_list):
        self.pot_list = pot_list
        

    def create_widgets(self):
        self.background = get_image("pot.jpg", self)
        self.frame_info = tk.LabelFrame(self, background="#f6f6f6")
        self.tabview = customtkinter.CTkTabview(self.frame_info, fg_color="#f6f6f6", border_color="#f6f6f6", bg_color="#f6f6f6", height=300, width=330)
        self.header = create_header(self.frame_info, "Records of Pots", 165, 10)
        self.tab1 = self.tabview.add("Create pot and add plant")
        self.tab2 = self.tabview.add("Delete pot")
        self.tabview.set("Create pot and add plant")
            
        small_label(self.tab1, "Add pot", 10, 35)
        small_label(self.tab1, "Select the plant you want to place in pot", 10, 100)
        small_label(self.tab2, "Select the pot you want to delete", 62, 35)
        

        self.conn = sqlite3.connect('PyFlora.db')
        self.c = self.conn.cursor() 
        
        self.new_list = get_plants()
        self.new_pot_list = get_pots()
        self.add_entry_var = tk.StringVar()
        self.add_entry = customtkinter.CTkEntry(self.tab1, textvariable=self.add_entry_var, corner_radius=8, fg_color="#f6f6f6",text_color="black")
        self.select_plant_var = tk.StringVar()
        self.select_plant_dropmenu = ttk.OptionMenu(self.tab1, self.select_plant_var, *self.new_list)
        self.save_image = customtkinter.CTkImage(Image.open("media\icons8-save-100.png").resize((20, 20), Image.ANTIALIAS))
        self.save_plant_to_pot_button = customtkinter.CTkButton(master=self.tab1, width=90, image=self.save_image, text="Save",compound="left") 
        
        
        self.del_pot_var = tk.StringVar()
        self.delete_pot_menu = ttk.OptionMenu(self.tab2, self.del_pot_var, *self.new_pot_list)
        self.delete = customtkinter.CTkImage(Image.open("media\del.png").resize((20, 20), Image.ANTIALIAS))
        self.delete_button = customtkinter.CTkButton(master=self.tab2, text="Delete", fg_color="red2", hover_color="red3", image=self.delete, width=100, height=10)

        bttn(self, 265, 430, '  P O T   L I S T  ','#e6e6e6','white', lambda: self.controller.show_frame(pot_list.PotList))
        
    def place_widgets(self):
        self.frame_info.place(x=150, y=60, width=500, height=350)
        self.tabview.place(x=85, y=40)
        self.add_entry.place(x=130, y=30)
        self.select_plant_dropmenu.place(x=250, y=96)
        self.delete_pot_menu.place(x=40 ,y=80)
        self.save_plant_to_pot_button.place(x=110, y=170)
        self.delete_button.place(x=110, y=170)
        #self.home_button.place(x=300, y=400)

    def bind_widgets(self):
        self.save_plant_to_pot_button.configure(command=self.insert_pot_data)
        self.delete_button.configure(command=self.delete_data)
    
    def updated_pot_list(self):
        self.new_pot_list.append(self.add_entry.get().capitalize())
        self.add_entry.delete(0, 'end')
    
        menu = self.delete_pot_menu["menu"]
        menu.delete(0, "end")
        for del_pot in self.new_pot_list:
            menu.add_command(label=del_pot, 
                command=lambda value=del_pot: self.del_pot_var.set(value))
            
    def delete_selected_item(self):
        
        selected = self.delete_pot_menu['menu'].index(self.del_pot_var.get())
        self.delete_pot_menu['menu'].delete(selected)
        self.del_pot_var.set(self.delete_pot_menu['menu'].entrycget(0,"label"))
        
        
        

    def insert_pot_data(self):
        
        try:
            self.c.execute("SELECT Pot FROM RecordsOfPots WHERE (Pot=?)",
                        [self.add_entry.get().capitalize()])
            self.result = self.c.fetchone()

            if self.result:
                messagebox.showerror("Error", "Pot is already in the database!")
                clear(self.add_entry)
           
            elif self.add_entry.get() == '':
                messagebox.showerror("Error", "All fields are required!")
           
            else:
                self.c.execute("INSERT INTO RecordsOfPots (Pot,Plant) VALUES (?,?)",
                        (self.add_entry.get().capitalize(),self.select_plant_var.get()))
                self.updated_pot_list()
                self.conn.commit()
                messagebox.showinfo("Success", "Pot data is successfully added!")
                clear(self.add_entry)
                

        except sqlite3.Error as error:
            print("Failed to add data", error)
        self.pot_list.refresh()
                                

    def delete_data(self):
        
        try:
            self.conn = sqlite3.connect('PyFlora.db')
            self.c = self.conn.cursor()
            
            self.c.execute("SELECT * FROM RecordsOfPots WHERE Pot=?",
            [self.del_pot_var.get()])
            self.result = self.c.fetchone()
            
            if self.result:
                self.answer = messagebox.askyesno("Confirmation","Are you sure you want to delete selected pot?")
                if self.answer:
                    self.c.execute("DELETE FROM RecordsOfPots WHERE Pot=?",
                    [self.del_pot_var.get()])
                    self.delete_selected_item()
                        
                self.conn.commit()
                messagebox.showinfo("Success", "Successfully deleted pot!")
            else:
                messagebox.showerror("Error","The entered pot is not in database!")
                clear(self.delete_pot_menu)

        except sqlite3.Error as error:
                print("Failed to update data", error)
    

from email.errors import MessageError
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
#from gui import list_gui
from utils.util import get_image, small_label, create_header, clear
import customtkinter
from PIL import Image, ImageTk
from gui import list_gui
import sqlite3
import os






class AddPlant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image("add_plant.jpg", self)

        """frame = customtkinter.CTkFrame(
            master=self, width=400, height=250, border_width=4, fg_color="white", border_color="grey")
        frame.place(x=150, y=30)"""


        create_header(self, "Records of Plants", 110, 60)

        tabview = customtkinter.CTkTabview(
            self, fg_color="#f6f6f6", border_color="#f6f6f6", bg_color="#f6f6f6", height=300, width=320)
        tabview.place(x=50, y=100)
        tab1 = tabview.add("Add plant")  # add tab at the end
        tab2 = tabview.add("Update plant data")  # add tab at the end
        tab3 = tabview.add("Delete plant")
        tabview.set("Add plant")  # set currently visible tab

    

        #fetching column Plant
        """conn = sqlite3.connect('PyFlora.db')
        c = conn.cursor()
        c.execute("SELECT Plant FROM RecordsOfPlants")
        result = c.fetchall()
        new_list = [i for i, in result]"""
        
        
        ################################   tab1 Add plant  #######################################
        
        def openFile():
            global filepath, file_label
            filepath = filedialog.askopenfilename(initialdir="C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media", filetypes=(('jpg', '*.jpg'),('png','*.png'),('All files','*.*'))) 
            
            
            base_filename = os.path.basename(filepath)
            file_label = ttk.Label(tab1, text=base_filename, background="#f6f6f6")
            file_label.place(x=95, y=90)   


        small_label(tab1, "Add plant", 10, 35)
        small_label(tab1, "Add Image", 10, 90)
        
        add_entry_var = tk.StringVar()
        add_entry = customtkinter.CTkEntry(
            tab1, textvariable=add_entry_var, corner_radius=8, fg_color="#f6f6f6",text_color="black")
        add_entry.place(x=135, y=30)

        
        def insert_data():
            global filepath, data
            read_file = open(filepath,'rb')
            read_file = read_file.read()
            

            try:
                conn = sqlite3.connect('PyFlora.db')
                c = conn.cursor()
                data = (add_entry.get(),read_file)

                c.execute("SELECT Plant FROM RecordsOfPlants WHERE (Plant=?)",
                        [add_entry.get()])
                
                result = c.fetchone()
                
                if result:
                    messagebox.showerror(
                        "Error", "Plant is already in database!")
                    clear(add_entry)
                
                elif add_entry.get() == '':
                    messagebox.showerror("Error","All fields are required!")
                else:
                    c.execute("INSERT INTO RecordsOfPlants (Plant, Photo) VALUES (?,?)",
                        (data))
                    conn.commit()
                    messagebox.showinfo("Success", "Plant is successfully added!")
                    clear(add_entry)

            except sqlite3.Error as error:
                    print("Failed to add data", error)



        ################################   tab2 Update plant  #####################################
        
        small_label(tab2, "Update plant", 10, 35)
        small_label(tab2, "Change Image", 10, 90)

        plant_var = tk.StringVar()
        update_plant_entry = customtkinter.CTkEntry(tab2, textvariable=plant_var, corner_radius=8, fg_color="#f6f6f6",text_color="black")
        update_plant_entry.place(x=135, y=30)

        update_var = tk.StringVar()
        update_image_entry = customtkinter.CTkEntry(tab2, textvariable=update_var, corner_radius=8, fg_color="#f6f6f6",text_color="black")
        update_image_entry.place()

        conn = sqlite3.connect('Pyflora.db')
        c = conn.cursor()

        def insert_updated_data():
            global data
            
            c.execute("SELECT * FROM RecordsOfPlants WHERE Plant=?",
                [update_plant_entry.get()])

            result = c.fetchone()
            
            if result:
                c.execute("UPDATE RecordsOfPlants set Plant=? WHERE Plant_id=?",
                    [update_plant_entry.get()])
                
                conn.commit()

            
        
        def check_if_plant_exists():
            
            c.execute("SELECT Plant FROM RecordsOfPlants WHERE (Plant=?)",
                    [update_plant_entry.get()])

            result = c.fetchone()
            
            if result:
                insert_updated_data()
                messagebox.showinfo("Success", "Successfully updated plant!")
                clear(update_plant_entry)
            else:
                messagebox.showerror(
                    "Error", "The entered plant is not in database")
                clear(update_plant_entry)


        def update_data():
            
            try:
                if update_plant_entry.get() == '':
                    messagebox.showerror("Error", "All fields are required !")
            
                else:
                    check_if_plant_exists()

            except sqlite3.Error as error:
                print("Failed to update data", error)


    
        def delete_data():
            pass
        



        
        open_button = customtkinter.CTkButton(
            master=tab1, width=90, text="Choose Image", height=10, compound="left", command=lambda:openFile())

        change_button = customtkinter.CTkButton(master=tab2, width=90, text="Choose Image", height=10, compound="left", command=lambda:openFile())
        
        save_image = customtkinter.CTkImage(Image.open(
            "media\icons8-save-100.png").resize((20, 20), Image.ANTIALIAS))

        save_button = customtkinter.CTkButton(
            master=tab1, width=90, image=save_image, text="Save",compound="left", command=insert_data)

        home_image = customtkinter.CTkImage(Image.open(
            "media\icons8-home-256.png").resize((20, 20), Image.ANTIALIAS))

        home_button = customtkinter.CTkButton(
            master=self, text="", image=home_image, width=80, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))

        update_image = customtkinter.CTkImage(Image.open(
            "media\icons8-update-100.png").resize((20, 20), Image.ANTIALIAS))

        update_button = customtkinter.CTkButton(
            master=tab2, text="Update", image=update_image, width=100, height=10, command=update_data)

        delete = customtkinter.CTkImage(Image.open(
            "media\del.png").resize((20, 20), Image.ANTIALIAS))

        delete_button = customtkinter.CTkButton(
            master=tab3, text="Delete", fg_color="red2", hover_color="red3", image=delete, width=100, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))


        open_button.place(x=185, y=90)
        change_button.place(x=185,y=90)
        update_button.place(x=110, y=170)
        delete_button.place(x=100, y=100)
        home_button.place(x=300, y=400)
        save_button.place(x=120, y=170)

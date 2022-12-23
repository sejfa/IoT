import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from turtle import bgcolor
#from gui import list_gui
from utils.util import get_image, small_label, create_header
import customtkinter
from PIL import Image
from gui import list_gui
import sqlite3
import os

class AddPlant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image("add_plant.jpg", self)

        """frame = customtkinter.CTkFrame(
            master=self, width=400, height=250, border_width=4, fg_color="white", border_color="grey")
        frame.place(x=150, y=30)
"""
        create_header(self, "Records of Plants", 110, 60)

        tabview = customtkinter.CTkTabview(
            self, fg_color="#f6f6f6", border_color="#f6f6f6", bg_color="#f6f6f6", height=300, width=320)
        tabview.place(x=50, y=100)
        tab1 = tabview.add("Add plant")  # add tab at the end
        tab2 = tabview.add("Update plant data")  # add tab at the end
        tab3 = tabview.add("Delete plant")
        tabview.set("Add plant")  # set currently visible tab

    

        #fetching column Plant
        conn = sqlite3.connect('PyFlora.db')
        c = conn.cursor()
        c.execute("SELECT Plant FROM RecordsOfPlants")
        result = c.fetchall()
        new_list = [i for i, in result]
        
        #importing Images from directory

        def openFile():
            global filepath
            filepath = filedialog.askopenfilenames(initialdir="C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media", filetypes=(('jpg', '*.jpg'),('png','*.png'),('All files','*.*'))) 

            """if filepath is not None:
                # this gets the full path of your selected file
                filename = filepath.name
                # this is only selecting the name with file extension
                filename = os.path.basename(filename)
                # then create a new label with the filename
                file_label = ttk.Label(tab1, text=filename, background="#f6f6f6")
                file_label.place(x=105, y=90) """  



       

        small_label(tab1, "Add plant", 10, 35)
        small_label(tab1, "Add Image", 10, 90)
        
        # tab1 Add plant
        options = tk.StringVar()
        drop = customtkinter.CTkOptionMenu(
            tab1, values=new_list, variable=options, corner_radius=8,button_color="#a8a8a8", button_hover_color="#9e9e9e",fg_color="#f6f6f6",text_color="black")
        drop.place(x=100, y=30)




        # tab2 Update plant
        


        
        def convert_image_into_binary(filename):
            with open(filename, 'rb') as file:
                photo_image = file.read()
            return photo_image

        def insert_plant_and_image():
            conn = sqlite3.connect('PyFlora.db')
            c = conn.cursor()

            for image in filepath:
                insert_photo = convert_image_into_binary(image)
                
                c.execute("INSERT INTO RecordsOfPlants (Plant, Photo) VALUES (?,:image)",
                        ([options.get()],{'image':insert_photo}))
            conn.commit()
            messagebox.showinfo("Success", "Plant is successfully added!")



        def update_data():
            conn = sqlite3.connect('PyFlora.db')
            c = conn.cursor()

            c.execute("SELECT * FROM RecordsOfPlants WHERE Plant=?",
                  [options.get()])

            result = c.fetchone()
            if result:
                c.execute("UPDATE RecordsOfPlants set Plant=? WHERE Username=? ",
                        [new_password_entry.get(), username_entry.get()])
                messagebox.showinfo(
                    "Success", "Successfully changed password, You can now login with new password!")

             
            conn.commit()


        def delete_data():
            pass
        



        
        open_button = customtkinter.CTkButton(
            master=tab1, width=90, text="Choose File", height=10, compound="left", command=openFile)

            
        save_button = customtkinter.CTkButton(
            master=tab1, width=90, text="Save", fg_color="#e2e2e2", hover_color="#cfcfcf", text_color="black",  height=10, compound="left", command=insert_plant_and_image)

        home = customtkinter.CTkImage(Image.open(
            "media\icons8-home-256.png").resize((20, 20), Image.ANTIALIAS))

        home_button = customtkinter.CTkButton(
            master=self, text="", image=home, width=80, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))

        update = customtkinter.CTkImage(Image.open(
            "media\icons8-update-100.png").resize((20, 20), Image.ANTIALIAS))

        update_button = customtkinter.CTkButton(
            master=tab2, text="Update", image=update, width=100, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))

        delete = customtkinter.CTkImage(Image.open(
            "media\del.png").resize((20, 20), Image.ANTIALIAS))

        delete_button = customtkinter.CTkButton(
            master=tab3, text="Delete", fg_color="red2", hover_color="red3", image=delete, width=100, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))


        open_button.place(x=130, y=90)
        update_button.place(x=20, y=50)
        delete_button.place(x=100, y=100)
        home_button.place(x=300, y=400)
        save_button.place(x=120, y=170)

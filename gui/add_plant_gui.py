import tkinter as tk
from tkinter import ttk, messagebox
#from gui import list_gui
from utils.util import get_image, create_smaller_label, create_header
import customtkinter
from PIL import Image
from gui import list_gui
import sqlite3


class AddPlant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image("bg.jpg", self)
        frame = customtkinter.CTkFrame(
            master=self, width=500, height=400, border_width=4, fg_color="white", border_color="grey")
        frame.place(x=150, y=30)

        create_header(frame, "Records of Plants", 150, 10)

        tabview = customtkinter.CTkTabview(
            frame, fg_color="white", border_color="grey")
        tabview.place(x=100, y=50)
        tab1 = tabview.add("Add plant")  # add tab at the end
        tab2 = tabview.add("Update plant data")  # add tab at the end
        tab3 = tabview.add("Delete plant")
        tabview.set("Add plant")  # set currently visible tab

        conn = sqlite3.connect('PyFlora.db')
        c = conn.cursor()
        c.execute("SELECT Plant FROM RecordsOfPlants")
        result = c.fetchall()
        new_list = [i for i, in result]

        create_smaller_label(tab1, "Add plant", 10, 30)
        create_smaller_label(tab1, "Add Image", 10, 70)
        # tab1 Add plant
        options = tk.StringVar()
        drop = customtkinter.CTkOptionMenu(
            tab1, values=new_list, variable=options, corner_radius=8)
        drop.place(x=100, y=30)

        def save_data():
            conn = sqlite3.connect('PyFlora.db')
            c = conn.cursor()

            c.execute("INSERT INTO RecordsOfPlants (Plant) VALUES (?)",
                      [options.get()])
            conn.commit()
            messagebox.showinfo("Success", "Plant is successfully added!")

        def update_data():
            pass

        def delete_data():
            pass

        save = customtkinter.CTkImage(
            Image.open("media\save.png").resize((20, 20), Image.ANTIALIAS))

        save_button = customtkinter.CTkButton(
            master=tab1, image=save, width=50, text="Save", fg_color="green3", hover_color="green4",  height=10, compound="left", command=save_data)

        home = customtkinter.CTkImage(Image.open(
            "media\icons8-home-256.png").resize((20, 20), Image.ANTIALIAS))

        home_button = customtkinter.CTkButton(
            master=frame, text="", image=home, width=50, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))

        update = customtkinter.CTkImage(Image.open(
            "media\icons8-update-100.png").resize((20, 20), Image.ANTIALIAS))

        update_button = customtkinter.CTkButton(
            master=tab2, text="Update", image=update, width=50, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))

        delete = customtkinter.CTkImage(Image.open(
            "media\del.png").resize((20, 20), Image.ANTIALIAS))

        delete_button = customtkinter.CTkButton(
            master=tab3, text="Delete", fg_color="red2", hover_color="red3", image=delete, width=50, height=10, command=lambda: controller.show_frame(list_gui.SecondPage))

        update_button.place(x=20, y=50)
        delete_button.place(x=100, y=100)
        home_button.place(x=225, y=360)
        save_button.place(x=100, y=150)

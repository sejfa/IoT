import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from svi_gui import list_gui


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("ansp.jpg")
        photo = ImageTk.PhotoImage(load)
        label_backg = tk.Label(self, image=photo)
        label_backg.image = photo
        label_backg.place(x=0, y=0)

        button_back = ttk.Button(
            self, text="Nazad", width=15, command=lambda: controller.show_frame(list_gui.SecondPage))
        button_back.place(x=40, y=450)

from gui import hosta_gui, basil_gui, add_plant_gui
from tkinter import ttk
import tkinter as tk
from utils.util import get_image, create_button, create_label, create_header, get_foreground


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        basil_frame = ttk.Frame(self
                                )
        basil_frame.place(x=50, y=80, width=330, height=160)

        hosta_frame = ttk.Frame(self
                                )
        hosta_frame.place(x=420, y=80, width=330, height=160,)

        mint_frame = ttk.Frame(self
                               )
        mint_frame.place(x=50, y=275, width=330, height=160,)

        get_image('basil5.jpg', basil_frame)
        get_image('hosta1.jpg', hosta_frame)
        get_image('mint1.jpg', mint_frame)

        create_header(self, "List of vessels", x=300, y=5)
        create_label(self, "Basil", x=50, y=55)
        create_label(self, "Hosta", x=420, y=55)
        create_label(self, "Mint", x=50, y=250)

        create_button(self, "Open", controller,
                      basil_gui.BasilPage, 280, 250)
        create_button(self, "Open", controller,
                      hosta_gui.HostaPage, 650, 250,)
        create_button(self, "Open", controller,
                      hosta_gui.HostaPage, 280, 445,)
        create_button(self, "Next", controller,
                      add_plant_gui.AddPlant, 660, 450)

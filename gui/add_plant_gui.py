import tkinter as tk
from tkinter import ttk
#from gui import list_gui
from utils.util import get_image


class AddPlant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('ansp.jpg', self)

        button_back = ttk.Button(
            self, text="Back", width=15, command=None)
        button_back.place(x=20, y=450)

import tkinter as tk
from tkinter import ttk
from gui import main_menu
from utils.util import get_image


class HostaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('new.jpg', self)

        button_back = ttk.Button(
            self, text="Back", width=15, command=lambda: controller.show_frame(main_menu.SecondPage))
        button_back.place(x=20, y=450)

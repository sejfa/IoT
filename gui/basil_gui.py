import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gui import list_gui
from svi_crudovi.crud import get_image, create_label, get_background, create_button


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('ansp.jpg', self)
        basil_info = tk.LabelFrame(self, background=get_background(),
                                   )
        basil_info.place(x=50, y=100, width=250, height=210,)

        create_label(basil_info, "Sensors info", 50, 10)

        create_button(self, "Back", controller,
                      list_gui.SecondPage, 15, 40, 450)

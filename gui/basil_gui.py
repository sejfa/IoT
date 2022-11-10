import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gui import list_gui
from svi_crudovi.crud import get_image, create_label, create_smaller_label,  get_background, create_button, get_hum, get_temp, get_bright, get_ph, get_sal


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('basil2.jpg', self)

       # basil_info = tk.LabelFrame(self, background=get_background(),

        #basil_info.place(x=20, y=100, width=370, height=210,)

        create_label(self, "Basil sensors info", 15, 5)
        hum = get_hum()
        create_smaller_label(self, hum, 15, 45)
        temp = get_temp()
        create_smaller_label(self, temp, 15, 80)
        bright = get_bright()
        create_smaller_label(self, bright, 15, 115)
        ph = get_ph()
        create_smaller_label(self, ph, 15, 150)
        sal = get_sal()
        create_smaller_label(self, sal, 15, 185)

        sync_button = ttk.Button(
            self, text="Sync", width=15, command=None)
        sync_button.place(x=100, y=225)
        create_button(self, "Back", controller,
                      list_gui.SecondPage, 15, 40, 470)

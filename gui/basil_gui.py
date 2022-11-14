import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui import list_gui
from svi_crudovi.crud import get_image, create_label, create_smaller_label, get_background, create_button, get_hum, get_temp, get_bright, get_ph, get_sal
from svi_crudovi.crud import get_optimal_hum, get_optimal_temp, get_optmal_ph, get_optimal_sal, get_optimal_bright


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('basil2.jpg', self)

        basil_info = tk.LabelFrame(self, background=get_background())

        basil_info.place(x=10, y=5, width=370, height=215,)

        create_label(basil_info, "Basil sensors info", 15, 5)

        hum = get_hum()
        create_smaller_label(basil_info, hum, 15, 45)
        temp = get_temp()
        create_smaller_label(basil_info, temp, 15, 80)
        bright = get_bright()
        create_smaller_label(basil_info, bright, 15, 115)
        ph = get_ph()
        create_smaller_label(basil_info, ph, 15, 150)
        sal = get_sal()
        create_smaller_label(basil_info, sal, 15, 185)

        def sync_button():

            basil_info.update()
            optimal_hum = get_optimal_hum()
            create_smaller_label(basil_info, optimal_hum, 15, 45)
            optimal_temp = get_optimal_temp()
            create_smaller_label(basil_info, optimal_temp, 15, 80)
            optimal_bright = get_optimal_bright()
            create_smaller_label(basil_info, optimal_bright, 15, 115)
            optimal_ph = get_optmal_ph()
            create_smaller_label(basil_info, optimal_ph, 15, 150)
            optimal_sal = get_optimal_sal()
            create_smaller_label(basil_info, optimal_sal, 15, 185)

        sync_button = ttk.Button(
            self, text="Sync", width=15, command=sync_button)
        sync_button.place(x=140, y=235)
        create_button(self, "Back", controller,
                      list_gui.SecondPage, 15, 40, 470)

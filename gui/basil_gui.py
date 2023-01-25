import tkinter as tk
from tkinter import ttk
from gui import plant_list
from tkinter import messagebox
from utils.util import get_image, create_label, create_smaller_label, get_background, create_button
from cruds.crud import get_optimal_hum, get_optimal_temp, get_optmal_ph, get_optimal_sal, get_optimal_bright, get_hum, get_temp, get_bright, get_ph, get_sal


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#F0F0F0")

        basil_info = tk.LabelFrame(self, background=get_background())

        basil_info.place(x=2, y=2, width=370, height=215,)

        create_label(basil_info, "Basil sensors info", 15, 5)

        pic_frame = ttk.Frame(self)
        pic_frame.place(x=550, y=10, width=210, height=210)
        get_image('basil4.jpg', pic_frame)

        h = get_hum()
        hum = create_smaller_label(basil_info, h, 15, 45)
        t = get_temp()
        temp = create_smaller_label(basil_info, t, 15, 80)
        b = get_bright()
        bright = create_smaller_label(basil_info, b, 15, 115)
        p = get_ph()
        ph = create_smaller_label(basil_info, p, 15, 150)
        s = get_sal()
        sal = create_smaller_label(basil_info, s, 15, 185)

        def sync_button():

            hum.destroy()
            temp.destroy()
            bright.destroy()
            ph.destroy()
            sal.destroy()

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

            messagebox.showinfo("Success", "Successfully changed data")

        sync_button = ttk.Button(
            self, text="Sync", width=15, command=sync_button)
        sync_button.place(x=125, y=230)
        create_button(self, "Back", controller,
                      plant_list.PlantList, 20, 450)

        sync_button = ttk.Button(
            self, text="Show graphical info", width=25, command=None)
        sync_button.place(x=20, y=420)

from gui import hosta_gui, basil_gui
from PIL import ImageTk
from tkinter import ttk
import tkinter as tk
from svi_crudovi.crud import get_background, get_foreground, get_image, get_label_font, get_status_font
from svi_crudovi.crud import get_all_sensors
from baza_podataka.main import session


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = get_image('ansp.jpg')
        photo = ImageTk.PhotoImage(load)
        label_backg = tk.Label(self, image=photo)
        label_backg.image = photo
        label_backg.place(x=0, y=0)

        label_frame1 = tk.LabelFrame(self, background=get_background(),
                                     )
        label_frame1.place(x=50, y=100, width=330, height=160,)

        label_frame2 = tk.LabelFrame(self, background=get_background(),
                                     )
        label_frame2.place(x=420, y=100, width=330, height=160,)

        load1 = get_image('basil-herb.jpg')
        photo1 = ImageTk.PhotoImage(load1)
        label_basil1 = tk.Label(label_frame1, image=photo1)
        label_basil1.image = photo1
        label_basil1.place(x=0, y=0)

        load2 = get_image('hosta.jpg')
        photo2 = ImageTk.PhotoImage(load2)
        label_hosta = tk.Label(label_frame2, image=photo2)
        label_hosta.image = photo2
        label_hosta.place(x=0, y=0)

        label1 = ttk.Label(label_frame1, text="Posuda\n Bosiljak",
                           foreground=get_foreground(), font=get_label_font())
        label1.place(x=180, y=10)

        label2 = ttk.Label(label_frame2, text="Posuda\n Hosta",
                           foreground=get_foreground(), font=get_label_font())
        label2.place(x=180, y=10)
        button_frame1 = ttk.Button(
            label_frame1, text="Otvori", width=15, command=lambda: controller.show_frame(basil_gui.BasilPage))
        button_frame1.place(x=225, y=130)

        button_frame2 = ttk.Button(label_frame2, text="Otvori", width=15,
                                   command=lambda: controller.show_frame(hosta_gui.HostaPage))
        button_frame2.place(x=225, y=130)

        def refresh_sensors():
            sensors = get_all_sensors(session)
            humidity_label.configure(text=sensors)
            humidity_label.after(4000, refresh_sensors)

        random_hum = get_all_sensors(session)
        humidity_label = ttk.Label(label_frame1, text=random_hum, foreground=get_foreground(
        ), background=get_background(), font=get_status_font())
        humidity_label.place(x=116, y=95)
        refresh_sensors()

import customtkinter
import tkinter as tk
from tkinter import ttk
from gui import plant_list
from utils.util import get_image, create_label, info_label, get_background
from crud.crud_db import plant_hum, plant_temp, plant_bright, plant_sal, plant_ph, get_hosta


class HostaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        self.controller = controller
        self.displayed = False
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()

    def create_widgets(self):
    
        self.header = create_label(self, "Hosta care", 350, 35)
        self.pic_frame = ttk.Frame(self)
        self.pic_frame_image = get_image('hosta1.jpg', self.pic_frame)
        self.sync_button = ttk.Button(self, text="Sync", width=15)
        self.back = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Back", bg_color="white")
        self.h= get_hosta()
        self.info = info_label(self, self.h, 2, 120)

    def place_widgets(self):
        self.pic_frame.place(x=410, y=120, width=313, height=215)
        self.back.place(x=20, y=450)

    def bind_widgets(self):
        self.back.configure(command=self.back_button)
    
    def back_button(self):
        self.controller.show_frame(plant_list.PlantList)
        
        
        
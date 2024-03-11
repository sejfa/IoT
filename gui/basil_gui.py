import customtkinter
import tkinter as tk
from tkinter import ttk
from gui import plant_list
from utils.util import get_image, create_label, info_label, get_background, create_button, bttn
from crud.crud_db import plant_hum, plant_temp, plant_bright, plant_sal, plant_ph, get_basil


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        self.controller = controller
        self.displayed = False
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()


    def create_widgets(self):
        
        self.header = create_label(self, "Basil care", 350, 35)
        self.pic_frame = ttk.Frame(self)
        self.pic_frame_image = get_image('basil.jpg', self.pic_frame)
        self.back = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Back", bg_color="white")
        self.b= get_basil()
        self.info = info_label(self, self.b, 2, 120)
   
    def place_widgets(self):
        
        self.pic_frame.place(x=410, y=120, width=313, height=215)
        self.back.place(x=20, y=450)

    def bind_widgets(self):
        self.back.configure(command=self.back_button)

    def back_button(self):
        self.controller.show_frame(plant_list.PlantList)
        
        
        
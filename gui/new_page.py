import tkinter as tk
import customtkinter
from tkinter import ttk
from gui import pot_list
from utils.util import get_image, create_label, create_smaller_label, get_background, create_button, bttn
from crud.crud_db import sensor_hum, sensor_temp, sensor_bright, sensor_sal, sensor_ph



class NewBlankPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        self.controller = controller
        self.displayed = False
        self.graphical_info_exists = False
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()


    def create_widgets(self):
        self.pot_info = tk.LabelFrame(self, background="white")
        self.header = create_label(self.pot_info, """The page you requested cannot be displayed right now,
              it may be temporarily unavailable, 
                    please try again later! :)""", 170, 75)
        
        self.sync_button = ttk.Button(self, text="Sync", width=15)
        self.back = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Back", bg_color="white")
        self.graphical_button = ttk.Button(self, text="Show graphical info", width=20)
    
    def place_widgets(self):
        self.pot_info.place(x=2, y=130, width=795, height=215,)
        self.back.place(x=20, y=450)

    def bind_widgets(self):
        self.back.configure(command=self.back_button)
        

        
    def back_button(self):
        self.controller.show_frame(pot_list.PotList)
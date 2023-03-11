import customtkinter
import tkinter as tk
from tkinter import ttk
from gui import plant_list
from utils.util import get_image, create_label, create_smaller_label, get_background, create_button, bttn
from crud.crud_db import plant_hum, plant_temp, plant_bright, plant_sal, plant_ph


class BasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        self.controller = controller
        self.displayed = False
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()

    

    def create_widgets(self):
        self.basil_info = tk.LabelFrame(self, background=get_background())
        self.header = create_label(self, "Basil care", 350, 35)
        self.pic_frame = ttk.Frame(self)
        self.pic_frame_image = get_image('basil.jpg', self.pic_frame)
        self.sync_button = ttk.Button(self, text="Sync", width=15)
        #self.optimal_button = ttk.Button(self, text="Set to optimal",width=20)
        self.back = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Back", bg_color="white")
        #self.graphical_button = ttk.Button(self, text="Show graphical info")
        #bttn(self, 2, 230, ' S Y N C ', '#e6e6e6','light grey', self.display_data)
        #bttn(self, 257, 230, '  S E T   T O   O P T I M A L  ', '#e6e6e6','light grey', self.display_optimal_data)

    def place_widgets(self):
        self.basil_info.place(x=80, y=120, width=313, height=215,)
        self.pic_frame.place(x=410, y=120, width=313, height=215)
        self.sync_button.place(x=350, y=400)
        #self.optimal_button.place(x=220, y=230)
        self.back.place(x=20, y=450)

    def bind_widgets(self):
        self.sync_button.configure(command=self.display_data)
        #self.optimal_button.configure(command=self.display_optimal_data)
        #self.graphical_button.configure(command=None)
        self.back.configure(command=self.back_button)
        
    def display_data(self):
        
        if not self.displayed:
            self.h= plant_hum()
            self.hum = create_smaller_label(self.basil_info, self.h, 5, 15)
            self.t = plant_temp()
            self.temp = create_smaller_label(self.basil_info, self.t, 5, 55)
            self.b = plant_bright()
            self.bright = create_smaller_label(self.basil_info, self.b, 5, 95)
            self.p = plant_ph()
            self.ph = create_smaller_label(self.basil_info, self.p, 5, 135)
            self.s = plant_sal()
            self.sal = create_smaller_label(self.basil_info, self.s, 5, 175)
            self.displayed = True

    """ def display_optimal_data(self):

        self.hum.destroy()
        self.temp.destroy()
        self.bright.destroy()
        self.ph.destroy()
        self.sal.destroy()
        self.basil_info.update()

        self.opt_hum = get_optimal_hum()
        self.optimal_hum = create_smaller_label(self.basil_info, self.opt_hum, 15, 45)
        self.opt_temp = get_optimal_temp()
        self.optimal_temp = create_smaller_label(self.basil_info, self.opt_temp, 15, 80)
        self.opt_bright = get_optimal_bright()
        self.optimal_bright = create_smaller_label(self.basil_info, self.opt_bright, 15, 115)
        self.opt_ph = get_optmal_ph()
        self.optimal_ph = create_smaller_label(self.basil_info, self.opt_ph, 15, 150)
        self.opt_sal = get_optimal_sal()
        self.optimal_sal = create_smaller_label(self.basil_info, self.opt_sal, 15, 185)
        """
    def back_button(self):
        self.controller.show_frame(plant_list.PlantList)
        
        
        
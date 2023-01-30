import sqlite3
import tkinter as tk
from tkinter import LEFT, RIGHT, BOTH, END
from gui import basil_gui, hosta_gui, add_plant_gui, main_menu
from utils.util import get_image, create_header, create_frame, create_smaller_label,bttn
from cruds.crud import get_plants

class PlantList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.create_list_widgets()
        #self.place_widgets()
        #self.bind_widgets()

    def create_list_widgets(self):
        self.background_image = get_image("gp.jpg", self)
        self.frame = create_frame(self, 300, 550, 120, 100)
        self.title = create_header(self, "Plant list", 340, 110)  
        self.plants = get_plants()
        self.listbox_var = tk.StringVar(value=self.plants)
        self.listbox = tk.Listbox(self, listvariable=self.listbox_var)
        self.listbox.place(x=280, y=175, width=200, height=150)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.scrollbar.place(x=480, y=175, width=15, height=150)

        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<Double-Button-1>", self.on_item_click)
        bttn(self, 142, 350, '  A D D  P L A N T  ', '#e6e6e6','light grey', lambda: self.controller.show_frame(add_plant_gui.AddPlant))
        bttn(self, 397, 350, 'H O M E', '#e6e6e6','light grey', lambda: self.controller.show_frame(main_menu.SecondPage))
        
    def on_item_click(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.index = int(selection[0])
            if self.index == 0:
                self.controller.show_frame(basil_gui.BasilPage)
            elif self.index == 2:
                self.controller.show_frame(hosta_gui.HostaPage)
        else:
            print("No item selected")


        

     
        

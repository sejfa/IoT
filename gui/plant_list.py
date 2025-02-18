import sqlite3
import tkinter as tk
from tkinter import LEFT, RIGHT, BOTH, END
from gui import ginger_gui, basil_gui, hosta_gui, plant_gui, rose_gui,lilie_gui, main_menu, recordofplant, new_page
from utils.util import get_image, create_header, create_frame, create_smaller_label, bttn
from crud.crud_db import get_plants

class PlantList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.create_list_widgets()
        self.place_widgets()
        self.bind_widgets()

    def refresh(self):
        self.plants = get_plants()
        self.listbox_var.set(self.plants)

    def create_list_widgets(self):
        self.background_image = get_image("gp.jpg", self)
        self.frame = create_frame(self, 300, 550, 120, 100)
        self.title = create_header(self, "Plant list", 340, 110)  
        self.plants = get_plants()
        self.listbox_var = tk.StringVar(value=self.plants)
        self.listbox = tk.Listbox(self, listvariable=self.listbox_var)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        
        bttn(self, 142, 350, '  M A N A G E  P L A N T S ', '#e6e6e6','light grey', lambda: self.controller.show_frame(recordofplant.RecordOfPlants))
        bttn(self, 397, 350, 'H O M E', '#e6e6e6','light grey', lambda: self.controller.show_frame(main_menu.SecondPage))

    def place_widgets(self):
        self.listbox.place(x=280, y=175, width=200, height=150)
        self.scrollbar.place(x=480, y=175, width=15, height=150)

    def bind_widgets(self):
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<Double-Button-1>", self.on_item_click)


    def on_item_click(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.index = int(selection[0])
            #imeOdabrane = self.plants[self.index]
            #self.controller.show_frame(plant_gui.PlantPage(plantName=imeOdabrane))
            if self.index == 0:
                self.controller.show_frame(basil_gui.BasilPage)
            elif self.index == 1:
                self.controller.show_frame(hosta_gui.HostaPage)
            elif self.index == 2:
                self.controller.show_frame(lilie_gui.LiliePage)
            elif self.index == 3:
                self.controller.show_frame(rose_gui.RosePage)
            else:
                self.controller.show_frame(new_page.NewBlankPage)
        else:
            print("No item selected")


        

     
        

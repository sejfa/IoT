import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT, RIGHT, BOTH, END
from gui import kitchen_shelf_by_the_window, living_room_table_near_the_couch, balcony_near_window,bedroom_near_the_bed, main_menu, recordofpots
from utils.util import get_image, create_header, create_frame, create_smaller_label,bttn
from crud.crud_db import get_pots


class PotList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.create_list_widgets()
        self.place_widgets()
        self.bind_widgets()

        
    def refresh(self):
        self.pots = get_pots()
        self.treeview.delete(*self.treeview.get_children())
        for i, pot in enumerate(self.pots):
            if  pot[1] != "None":
                self.treeview.insert('', 'end', values=(pot[0], "Full"))
            else:
                self.treeview.insert('', 'end', values=(pot[0], "Empty"))
        
    
    def create_list_widgets(self):
        
        self.background_image = get_image("gp.jpg", self)
        self.frame = create_frame(self, 300, 550, 120, 100)
        self.title = create_header(self, "Pot list", 340, 110)  
        self.pot = get_pots()
        self.treeview = ttk.Treeview(self, columns=('Pots', 'Status'), show='headings')
        self.treeview.heading('Pots', text='Pots')
        self.treeview.heading('Status', text='Status') 
        for pot in self.pot:
            if  pot[1] != "None":
                self.treeview.insert('', 'end', values=(pot[0], "Full"))
            else:
                self.treeview.insert('', 'end', values=(pot[0], "Empty"))
        
            
        bttn(self, 142, 350, '  M A N A G E  P O T S ', '#e6e6e6','light grey', lambda: self.controller.show_frame(recordofpots.RecordOfPots))
        bttn(self, 397, 350, 'H O M E', '#e6e6e6','light grey', lambda: self.controller.show_frame(main_menu.SecondPage))

    def place_widgets(self):
        self.treeview.place(x=185, y=175, width=420, height=150)
       

    def bind_widgets(self):
        self.treeview.bind("<Double-Button-1>", self.on_item_click)

    def on_item_click(self, event):
        selection = self.treeview.selection()
        if selection:
            item = self.treeview.focus()
            index = self.treeview.index(item)
            if index == 0:
                self.controller.show_frame(kitchen_shelf_by_the_window.KitchenBasilPage)
            elif index == 1:
                self.controller.show_frame(living_room_table_near_the_couch.LivingRoomHosta)
            elif index == 2:
                self.controller.show_frame(balcony_near_window.BalconyNearWindow)
            elif index == 3:
                self.controller.show_frame(bedroom_near_the_bed.BedroomNearBed)
        else:
            print("No item selected")

    
import tkinter as tk
from gui import basil_gui, add_plant_gui, main_menu
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
        self.title = create_header(self, "Plant list", 320, 110)
        self.list_var = tk.StringVar()
        self.list = tk.Listbox(self,listvariable=self.list_var, border=0)  
        self.plants = get_plants()
        self.list.insert(0, *self.plants) 
        self.list.place(x=350, y=150)

        def onselect(event):
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                data = event.widget.get(index)
                self.controller.show_frame(basil_gui.BasilPage)
        
    
        self.list.bind('<<ListboxSelect>>', onselect) 
        
 
        bttn(self, 142, 350, '  A D D  P L A N T  ', '#e6e6e6','light grey', lambda: self.controller.show_frame(add_plant_gui.AddPlant))
        bttn(self, 397, 350, 'H O M E', '#e6e6e6','light grey', lambda: self.controller.show_frame(main_menu.SecondPage))
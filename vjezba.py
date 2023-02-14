import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk, HORIZONTAL,BOTH
from gui import login_gui
from utils.util import get_image
from gui.login_gui import LoginMenu

class LoadWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.background_image = get_image('w.png', self)
        self.controller = controller
        self.create_widgets()
        self.pack()     

    def create_widgets(self):
        self.a = '#f1f1f1'
        self.frame = tk.Frame(self, width=800, height=490, bg='#f1f1f1')
        self.width_of_window = 800
        self.height_of_window = 500
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/2)
        self.master.geometry("%dx%d+%d+%d" %(self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.progress = Progressbar(self, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=810, mode='determinate')
        self.b1 = tk.Button(self, width=10, height=1, text='Get Started', font= 10, command=self.bar, border=0, fg='#023020', bg=self.a, activebackground=self.a, activeforeground='#023020')
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')

        self.frame.pack(fill="both", expand=True)
        self.progress.pack(fill="both", expand=True)
        self.b1.pack(side="bottom", padx=10, pady=10)
        
        

    def bar(self):
        self.l4 = tk.Label(self, text='Loading...', fg='white', bg=self.a)
        lst4 = ('Calibri (Body)', 10)
        self.l4.config(font=lst4)
        self.l4.place(x=370, y=460)

        import time
        for i in range(100):
            self.progress['value'] = i
            self.update_idletasks()
            time.sleep(0.1)  # Add a delay to show the progress bar

        self.l4.destroy()  # Remove the "Loading..." label
        self.master.destroy()  # Close the current window

    # Open the login window
        login_menu = LoginMenu(controller, controller.show_frame(login_gui.LoginMenu))
        login_menu.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    controller = None
    window = LoadWindow(root, controller)
    root.mainloop()


"""from gui import hosta_gui, basil_gui, add_plant_gui
import tkinter as tk
from utils.util import get_image, create_button, create_label, create_header, get_foreground
from tkinter import *
import customtkinter
from tkinter import ttk
from PIL import Image, ImageTk


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        get_image('gp.jpg',self)

        def add_plant_menu():
            f1.destroy()
            controller.show_frame(add_plant_gui.AddPlant)
            toggle_win()
            f1.destroy()


        def toggle_win():
            global f1
            f1=Frame(self,width=300,height=500,bg='white')
            f1.place(x=0,y=0)


            #buttons
            def bttn(x,y,text,bcolor,fcolor,cmd):
            
                def on_entera(e):
                    myButton1['background'] = bcolor #ffcc66
                    myButton1['foreground'] = '#262626'  #000d33

                def on_leavea(e):
                    myButton1['background'] = fcolor
                    myButton1['foreground'] = '#262626'

                myButton1 = Button(f1,text=text,
                            width=42,
                            height=2,
                            fg='#262626',
                            border=0,
                            bg=fcolor,
                            activeforeground='#262626',
                            activebackground=bcolor,            
                                command=cmd)
                            
                myButton1.bind("<Enter>", on_entera)
                myButton1.bind("<Leave>", on_leavea)

                myButton1.place(x=x,y=y)

            #bttn(0,80,'A C E R','#e8eded','white',None)
            bttn(0,117,'D E L L','#e6e6e6','white',None)
            bttn(0,154,'P O T S','#e6e6e6','white',None)
            bttn(0,191,'P L A N T S','#e6e6e6','white',add_plant_menu)
            bttn(0,228,'A B O U T','#e6e6e6','white',None)
            #bttn(0,265,'A C E R','#e6e6e6','white',None)

            #
            def dele():
                f1.destroy()

            global photo1
            root_folder_path = 'media'
            image_name = 'close.png'
            load = Image.open(f"{root_folder_path}/{image_name}")
            photo1 = ImageTk.PhotoImage(load)
            
            label_basil1 = tk.Label(f1, image=photo1)
            label_basil1.image = photo1
            label_basil1.place(x=5, y=10)
            
            
            

            Button(f1,
                image=photo1,
                border=0,
                command=dele,
                bg='grey',
                activebackground='white').place(x=5,y=10)
            

        
        root_folder_path = 'media'
        imagee = 'open.png'
        load2 = Image.open(f"{root_folder_path}/{imagee}")
        photo2 = ImageTk.PhotoImage(load2)

        label_basil1 = tk.Label(self, image=photo2)
        label_basil1.image = photo2
        label_basil1.place(x=5, y=10)

        Button(self,image=photo2,
            command=toggle_win,
            border=0,
            bg='grey',
            activebackground='white').place(x=5,y=10)


"""

"""import tkinter as tk
my_w = tk.Tk()
my_w.geometry("350x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_list = ["PHP","MySQL","Python","HTML","JQuery"]
options = tk.StringVar(my_w)
options.set(my_list[0]) # default value

om1 =tk.OptionMenu(my_w, options, *my_list)
om1.grid(row=2,column=5) 

b1 = tk.Button(my_w,  text='Remove All', command=lambda: my_remove() )  
b1.grid(row=1,column=2)

b2 = tk.Button(my_w,  text='Add All Opt', command=lambda: my_add() )  
b2.grid(row=2,column=2)

b3 = tk.Button(my_w,  text='Remove Selectd', command=lambda: my_remove_sel() )  
b3.grid(row=3,column=2)

def my_remove():
    options.set('') # remove default selection only, not the full list
    om1['menu'].delete(0,'end') # remove full list 
def my_add():
    my_remove() # remove all options 
    for opt in my_list: 
        om1['menu'].add_command(label=opt, command=tk._setit(options, opt))
    options.set(my_list[0]) # default value set 

def my_remove_sel():
    r_index=om1['menu'].index(options.get())
    om1['menu'].delete(r_index)
    options.set(om1['menu'].entrycget(0,"label")) # select the first one 
    
my_w.mainloop()
"""
""""
class App():
    def __init__(self, parent):
        self.parent = parent
        self.options = ['one', 'two', 'three']

        self.om_variable = tk.StringVar(self.parent)
        self.om_variable.set(self.options[0])
        self.om_variable.trace('w', self.option_select)

        self.om = tk.OptionMenu(self.parent, self.om_variable, *self.options)
        self.om.grid(column=0, row=0)

        self.label = tk.Label(self.parent, text='Enter new option')
        self.entry = tk.Entry(self.parent)
        self.button = tk.Button(self.parent, text='Add option to list', command=self.add_option)

        self.label.grid(column=1, row=0)
        self.entry.grid(column=1, row=1)
        self.button.grid(column=1, row=2)

        #self.update_button = tk.Button(self.parent, text='Update option menu', command=self.update_option_menu)
        #self.update_button.grid(column=0, row=2)

     def update_option_menu(self):
            menu = self.om["menu"]
            menu.delete(0, "end")
            for string in self.options:
                menu.add_command(label=string, 
                                command=lambda value=string: self.om_variable.set(value))

    def add_option(self):
         self.options.append(self.entry.get())
         self.entry.delete(0, 'end')
         print (self.options)
         menu = self.om["menu"]
         menu.delete(-1)
         for string in self.options:
            menu.add_command(label=string, 
                             command=lambda value=string: self.om_variable.set(value))

    def option_select(self, *args):
        print (self.om_variable.get())


root = tk.Tk()
App(root)
root.mainloop()"""
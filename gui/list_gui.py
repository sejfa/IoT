from gui import hosta_gui, basil_gui, add_plant_gui
import tkinter as tk
from utils.util import get_image, create_button, create_label, create_header, get_foreground
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

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
                    myButton1['foreground']= '#262626'  #000d33

                def on_leavea(e):
                    myButton1['background'] = fcolor
                    myButton1['foreground']= '#262626'

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
            #bttn(0,117,'D E L L','#e6e6e6','white',None)
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

        basil_frame = ttk.Frame(self
                                )
        basil_frame.place(x=50, y=80, width=330, height=160)

        hosta_frame = ttk.Frame(self
                                )
        hosta_frame.place(x=420, y=80, width=330, height=160,)

        mint_frame = ttk.Frame(self
                               )
        mint_frame.place(x=50, y=275, width=330, height=160,)

        get_image('basil5.jpg', basil_frame)
        get_image('hosta1.jpg', hosta_frame)
        get_image('mint1.jpg', mint_frame)

        create_header(self, "List of vessels", x=300, y=5)
        create_label(self, "Basil", x=50, y=55)
        create_label(self, "Hosta", x=420, y=55)
        create_label(self, "Mint", x=50, y=250)

        create_button(self, "Open", controller,
                      basil_gui.BasilPage, 280, 250)
        create_button(self, "Open", controller,
                      hosta_gui.HostaPage, 650, 250,)
        create_button(self, "Open", controller,
                      hosta_gui.HostaPage, 280, 445,)
        create_button(self, "Next", controller,
                      add_plant_gui.AddPlant, 660, 450)

            
        """
from gui import hosta_gui, basil_gui
from PIL import ImageTk
from tkinter import ttk
import tkinter as tk
from svi_crudovi.crud import get_background, get_image, create_button, create_label
from baza_podataka.main import session
import tkinter.font as font


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('ansp.jpg', self)

        basil_frame = tk.LabelFrame(self, background=get_background(),
                                    )
        basil_frame.place(x=50, y=100, width=330, height=160,)

        hosta_frame = tk.LabelFrame(self, background=get_background(),
                                    )
        hosta_frame.place(x=420, y=100, width=330, height=160,)

        mint_frame = tk.LabelFrame(self, background=get_background(),
                                   )
        mint_frame.place(x=50, y=290, width=330, height=160,)

        get_image('basil-herb.jpg', basil_frame)
        get_image('hosta1.jpg', hosta_frame)
        get_image('mint_pot.jpg', mint_frame)

        create_label(basil_frame, "Basil pot", x=180, y=10)
        create_label(hosta_frame, "Hosta pot", x=180, y=10)
        create_label(mint_frame, "Mint pot", x=180, y=10)

        create_button(basil_frame, "Open", controller,
                      basil_gui.BasilPage, 15, 225, 130)
        create_button(hosta_frame, "Open", controller,
                      hosta_gui.HostaPage, 15, 225, 130,)
        create_button(mint_frame, "Open", controller,
                      hosta_gui.HostaPage, 15, 225, 130,)

        """add_button = tk.Button(self, text="Add pot\n +", width=46, height=10, bg='#EEEE76', fg='#ffffff',
                               command=lambda: controller.show_frame(hosta_gui.HostaPage))
        add_button.place(x=420, y=290)
        myFont = font.Font(family='Times New Roman',
                           size=10, weight='bold')
        add_button['font'] = myFont"""

        create_button(self, "Next", controller,
                      basil_gui.BasilPage, 15, 660, 450)

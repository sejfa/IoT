from gui import hosta_gui, basil_gui
from tkinter import ttk
import tkinter as tk
from utils.util import get_image, create_button, create_label


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        basil_frame = ttk.Frame(self
                                )
        basil_frame.place(x=50, y=100, width=330, height=160)

        hosta_frame = ttk.Frame(self
                                )
        hosta_frame.place(x=420, y=100, width=330, height=160,)

        mint_frame = ttk.Frame(self
                               )
        mint_frame.place(x=50, y=290, width=330, height=160,)

        get_image('bs.jpg', basil_frame)
        get_image('hosta1.jpg', hosta_frame)
        get_image('mint1.jpg', mint_frame)

        create_label(self, "Basil pot", x=180, y=70)
        create_label(self, "Hosta pot", x=180, y=10)
        create_label(self, "Mint pot", x=180, y=10)

        create_button(basil_frame, "Open", controller,
                      basil_gui.BasilPage, 15, 225, 130)
        create_button(hosta_frame, "Open", controller,
                      hosta_gui.HostaPage, 15, 225, 130,)
        create_button(mint_frame, "Open", controller,
                      hosta_gui.HostaPage, 15, 225, 130,)
        create_button(self, "Next", controller,
                      basil_gui.BasilPage, 15, 660, 450)

import tkinter as tk
from tkinter import ttk
from utils.util import create_label, create_smaller_label, get_image, get_foreground, create_frame, forgot_password
import customtkinter


root = tk.Tk()
window = root

frame = customtkinter.CTkFrame(master=root,
                               width=200,
                               height=200,
                               corner_radius=10)
frame.pack(padx=20, pady=20)
text_var = tk.StringVar(value="CTkLabel")

label = customtkinter.CTkLabel(master=root,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def slider_event():
    pass


slider = customtkinter.CTkSlider(
    master=frame, from_=0, to=100, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()

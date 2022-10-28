import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from svi_crudovi.crud import get_image, get_foreground, get_label_font, get_fg
from gui import list_gui, basil_gui, hosta_gui


class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('pl.jpg', self)

        heading_label = tk.Label(self, text="Prijava",
                                 foreground=get_foreground(), font=get_label_font())
        heading_label.place(x=350, y=100)

        name_var = tk.StringVar()
        name_Label = tk.Label(self, text="Name",
                              fg=get_fg())
        name_Label.place(x=310, y=140)
        name_entry = ttk.Entry(
            self, textvariable=name_var, width=25)
        name_entry.place(x=310, y=160)

        surname_var = tk.StringVar()
        surname_Label = tk.Label(self, text="Surname",
                                 fg=get_fg())
        surname_Label.place(x=310, y=190)
        surname_entry = ttk.Entry(
            self, textvariable=surname_var, width=25)
        surname_entry.place(x=310, y=210)

        username_var = tk.StringVar()
        username_Label = tk.Label(self, text="Username",
                                  fg=get_fg())
        username_Label.place(x=310, y=240)
        username_entry = ttk.Entry(
            self, textvariable=username_var, width=25)
        username_entry.place(x=310, y=260)

        password_var = tk.StringVar()
        password_Label = tk.Label(self, text="Password",
                                  fg=get_fg())
        password_Label.place(x=310, y=290)
        password_entry = ttk.Entry(
            self, textvariable=password_var, width=25, show="*")
        password_entry.place(x=310, y=310)

        def verify():
            if username_entry.get() == 'pero' and password_entry.get() == '1234':
                controller.show_frame(list_gui.SecondPage)
            else:
                messagebox.showinfo(
                    "Dogodila se greška", "Molimo unesite točan username i password!")

        login_button = ttk.Button(
            self, text="Prijavi me", width=25, command=verify)
        login_button.place(x=308, y=355)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.resizable(width=False, height=False)

        self.frames = {}
        for i in (LoginMenu, list_gui.SecondPage, basil_gui.BasilPage, hosta_gui.HostaPage):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

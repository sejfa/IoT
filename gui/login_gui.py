import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


from gui import list_gui, basil_gui, hosta_gui


class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("pl.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        heading_label = tk.Label(self, text="Prijava",
                                 foreground='#4D4D4D', font=('Times New Roman', '15', 'bold italic'))
        heading_label.place(x=350, y=130)

        username_var = tk.StringVar()
        username_Label = tk.Label(self, text="Username",
                                  fg='#808080')
        username_Label.place(x=310, y=180)
        username_entry = ttk.Entry(
            self, textvariable=username_var, width=25)
        username_entry.place(x=310, y=200)

        password_var = tk.StringVar()
        password_Label = tk.Label(self, text="Password",
                                  fg='#808080')
        password_Label.place(x=310, y=230)
        password_entry = ttk.Entry(
            self, textvariable=password_var, width=25, show="*")
        password_entry.place(x=310, y=250)

        def verify():
            if username_entry.get() == 'pero' and password_entry.get() == '1234':
                controller.show_frame(list_gui.SecondPage)
            else:
                messagebox.showinfo(
                    "Dogodila se greška", "Molimo unesite točan username i password!")

        login_button = ttk.Button(
            self, text="Prijavi me", width=25, command=verify)
        login_button.place(x=308, y=300)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for i in (LoginMenu, list_gui.SecondPage, basil_gui.BasilPage, hosta_gui.HostaPage):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

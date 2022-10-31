import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from svi_crudovi.crud import get_image, get_foreground, get_label_font, get_fg
from gui import list_gui, login_gui
from baza_podataka.main import session


class SigninMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('pl.jpg', self)

        heading_label = tk.Label(self, text="Py Flora",
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

        already_acc = tk.Label(self, text="Already have an account?", foreground=get_foreground(), font=(
            'times', '8'))
        already_acc.place(x=310, y=375)

        def sign_up():

            if name_entry.get() == '' or surname_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '':
                messagebox.showerror("Error", "All fields are required !")

            else:
                controller.show_frame(list_gui.SecondPage)
                messagebox.showinfo("Success", "Thanks for signing up!")

        login_button = ttk.Button(
            self, text="Sign up", width=10, command=sign_up)
        login_button.place(x=350, y=345)

        login_button = tk.Button(
            self, text="Log in", font=('times', 8, 'bold underline'), bg='#E5E5E5', fg=get_foreground(), bd=0, activebackground='#E5E5E5', activeforeground='blue', command=lambda: controller.show_frame(login_gui.LoginMenu))
        login_button.place(x=310, y=395)

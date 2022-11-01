import tkinter as tk
from tkinter import ttk
import datetime as dt
import sqlite3
from tkinter import messagebox
from svi_crudovi.crud import get_image, get_foreground, get_label_font, get_fg, create_frame, create_button
from gui import login_gui


class SigninMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('pl.jpg', self)

        create_frame(self, 330, 200)

        heading_label = tk.Label(self, text="Py Flora",
                                 foreground=get_foreground(), font=get_label_font())
        heading_label.place(x=360, y=110)

        name_var = tk.StringVar()
        name_Label = tk.Label(self, text="Name",
                              fg=get_fg())
        name_Label.place(x=320, y=140)
        name_entry = ttk.Entry(
            self, textvariable=name_var, width=25)
        name_entry.place(x=320, y=160)

        surname_var = tk.StringVar()
        surname_Label = tk.Label(self, text="Surname",
                                 fg=get_fg())
        surname_Label.place(x=320, y=190)
        surname_entry = ttk.Entry(
            self, textvariable=surname_var, width=25)
        surname_entry.place(x=320, y=210)

        username_var = tk.StringVar()
        username_Label = tk.Label(self, text="Username",
                                  fg=get_fg())
        username_Label.place(x=320, y=240)
        username_entry = ttk.Entry(
            self, textvariable=username_var, width=25)
        username_entry.place(x=320, y=260)

        password_var = tk.StringVar()
        password_Label = tk.Label(self, text="Password",
                                  fg=get_fg())
        password_Label.place(x=320, y=290)
        password_entry = ttk.Entry(
            self, textvariable=password_var, width=25, show="*")
        password_entry.place(x=320, y=310)

        already_acc = tk.Label(self, text="Already have an account?", foreground=get_foreground(), font=(
            'times', '8'))
        already_acc.place(x=320, y=380)

        def insert_user_data():

            date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y %H:%M:%S")
            conn = sqlite3.connect('Sensors.db')
            c = conn.cursor()
            c.execute("INSERT INTO UserData (Name, Surname, Username, Password, Date) VALUES (?,?,?,?,?)",
                      (name_entry.get(), surname_entry.get(), username_entry.get(), password_entry.get(), date))
            conn.commit()

        def sign_up():

            if name_entry.get() == '' or surname_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '':
                messagebox.showerror("Error", "All fields are required !")

            else:
                insert_user_data()
                controller.show_frame(login_gui.LoginMenu)
                messagebox.showinfo("Success", "Thanks for signing up!")

        sign_up_button = ttk.Button(
            self, text="Sign up", width=10, command=sign_up)
        sign_up_button.place(x=360, y=345)

        login_button = tk.Button(
            self, text="Log in", font=('times', 8, 'bold underline'), bg='#E5E5E5', fg=get_foreground(), bd=0, activebackground='#E5E5E5', activeforeground='blue', command=lambda: controller.show_frame(login_gui.LoginMenu))
        login_button.place(x=320, y=400)

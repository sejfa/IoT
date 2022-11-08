import tkinter as tk
from tkinter import ttk
import datetime as dt
import sqlite3
from tkinter import messagebox
from svi_crudovi.crud import create_smaller_label, get_image, get_foreground, create_frame, create_label
from gui import login_gui
from sensors_db import *


class SigninMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('pl.jpg', self)

        create_frame(self, 330, 200)

        create_label(self, "Py Flora", 360, 110)

        name_var = tk.StringVar()
        create_smaller_label(self, "Name", 320, 140)

        name_entry = ttk.Entry(
            self, textvariable=name_var, width=25)
        name_entry.place(x=320, y=160)

        surname_var = tk.StringVar()
        create_smaller_label(self, "Surname", 320, 190)

        surname_entry = ttk.Entry(
            self, textvariable=surname_var, width=25)
        surname_entry.place(x=320, y=210)

        username_var = tk.StringVar()
        create_smaller_label(self, "Username", 320, 240)

        username_entry = ttk.Entry(
            self, textvariable=username_var, width=25)
        username_entry.place(x=320, y=260)

        password_var = tk.StringVar()
        create_smaller_label(self, "Password", 320, 290)

        password_entry = ttk.Entry(
            self, textvariable=password_var, width=25, show="*")
        password_entry.place(x=320, y=310)

        create_smaller_label(self, "Already have an account?", 320, 380)

        def insert_user_data():

            date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y %H:%M:%S")
            conn = sqlite3.connect('Sensors.db')
            c = conn.cursor()
            c.execute("INSERT INTO UserData (Name, Surname, Username, Password, Date) VALUES (?,?,?,?,?)",
                      (name_entry.get(), surname_entry.get(), username_entry.get(), password_entry.get(), date))
            conn.commit()

        def check_if_exist():

            conn = sqlite3.connect('Sensors.db')
            c = conn.cursor()

            c.execute("SELECT Username,Password FROM UserData WHERE (Username=? OR Password=?)",
                      (username_entry.get(), password_entry.get()))
            result = c.fetchone()
            if result:
                messagebox.showerror(
                    "Error", "Username or password already exists!")
                controller.show_frame(SigninMenu)
                clear()
            else:
                insert_user_data()
                controller.show_frame(login_gui.LoginMenu)
                messagebox.showinfo("Success", "Thanks for signing up!")
                clear()

        def clear():
            name_entry.delete(0, 25)
            surname_entry.delete(0, 25)
            username_entry.delete(0, 25)
            password_entry.delete(0, 25)

        def sign_up():

            if name_entry.get() == '' or surname_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '':
                messagebox.showerror("Error", "All fields are required !")
                clear()
            else:
                check_if_exist()

        sign_up_button = ttk.Button(
            self, text="Sign up", width=10, command=sign_up)
        sign_up_button.place(x=360, y=345)

        login_button = tk.Button(
            self, text="Log in", font=('times', 8, 'bold underline'), bg='white', fg=get_foreground(), bd=0, activebackground='white', activeforeground='#4D4D4D', command=lambda: controller.show_frame(login_gui.LoginMenu))
        login_button.place(x=320, y=400)

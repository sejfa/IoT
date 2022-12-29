import tkinter as tk
from tkinter import ttk,FLAT
import datetime as dt
import sqlite3
from tkinter import messagebox
from utils.util import create_smaller_label, get_image, get_foreground, create_frame, create_label
from gui import login_gui
from sensors_db import *
import customtkinter


class SigninMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('bc.jpg', self)

        create_frame(self, 330, 200, 50, 70)

        create_label(self, "Py Flora", 110, 80)

        name_var = tk.StringVar()
        create_smaller_label(self, "Name", 70, 110)

        name_entry = tk.Entry(
            master=self, width=25, fg="black", bg="white", border=0, textvariable=name_var)
        name_entry.place(x=70, y=135)
        
        name_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        name_line.place(x=70, y=150)

        surname_var = tk.StringVar()
        create_smaller_label(self, "Surname", 70, 160)

        surname_entry = tk.Entry(
            master=self, width=25,fg="black", bg="white", border=0, textvariable=surname_var)
        surname_entry.place(x=70, y=185)
        
        surname_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        surname_line.place(x=70, y=205)

        username_var = tk.StringVar()
        create_smaller_label(self, "Username", 70, 210)

        username_entry = tk.Entry(
            master=self, width=25,fg="black", bg="white", border=0, textvariable=username_var)
        username_entry.place(x=70, y=235)
        
        username_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        username_line.place(x=70, y=255)

        password_var = tk.StringVar()
        create_smaller_label(self, "Password", 70, 260)

        password_entry = tk.Entry(
            master=self, width=25,fg="black", bg="white", border=0, textvariable=password_var, show="*")
        password_entry.place(x=70, y=285)

        password_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        password_line.place(x=70, y=305)

        create_smaller_label(self, "Already have an account?", 70, 350)

        def insert_user_data():

            date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y %H:%M:%S")
            conn = sqlite3.connect('Pyflora.db')
            c = conn.cursor()
            c.execute("INSERT INTO UserData (Name, Surname, Username, Password, Date) VALUES (?,?,?,?,?)",
                      (name_entry.get(), surname_entry.get(), username_entry.get(), password_entry.get(), date))
            conn.commit()

        def check_if_exist():

            conn = sqlite3.connect('Pyflora.db')
            c = conn.cursor()

            c.execute("SELECT Username,Password FROM UserData WHERE (Username=? OR Password=?)",
                      [username_entry.get(), password_entry.get()])
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

        signup_button = customtkinter.CTkButton(master=self,
                                                fg_color="green3",
                                                hover_color="green4",
                                                width=100,
                                                height=15,
                                                border_width=0,
                                                corner_radius=13,
                                                text="Sign up",
                                                bg_color="white",
                                                command=sign_up)
        signup_button.place(x=95, y=320)

        login_button = tk.Button(
            self, text="Log in", font=('times', 8, 'bold underline'), bg='white', fg=get_foreground(), bd=0, activebackground='white', activeforeground='#4D4D4D', command=lambda: controller.show_frame(login_gui.LoginMenu))
        login_button.place(x=70, y=370)

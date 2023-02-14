import sqlite3
import customtkinter
import tkinter as tk
import datetime as dt
from sensors_db import *
from gui import login_gui
from tkinter import ttk, FLAT
from tkinter import messagebox
from utils.util import create_smaller_label, get_image, get_foreground, create_frame, create_label


class SigninMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()

    def create_widgets(self):
        self.background_image = get_image('bc.jpg', self)
        self.create_frame = create_frame(self,330, 200, 50, 70)
        self.create_title = create_label(self,"Py Flora", 110, 80)   
        
        self.name_var = tk.StringVar()
        self.name_label = create_smaller_label(self, "Name", 70, 110)
        self.name_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.name_var)
        self.name_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        
        self.surname_var = tk.StringVar()
        self.surname_label = create_smaller_label(self,"Surname", 70, 160)
        self.surname_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.surname_var)
        self.surname_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        
        self.username_var = tk.StringVar()
        self.username_label = create_smaller_label(self, "Username", 70, 210)
        self.username_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.username_var)
        self.username_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        
        self.password_var = tk.StringVar()
        self.password_label = create_smaller_label(self, "Password", 70, 260)
        self.password_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.password_var, show="*")
        self.password_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
        
        self.already_account_label = create_smaller_label(self, "Already have an account?", 70, 350)
        self.signup_button = customtkinter.CTkButton(master=self, text="Sign up", width=100, height=15, border_width=0, corner_radius=13, bg_color="white",fg_color="green3",hover_color="green4")
        self.login_button = tk.Button(self, text="Log in", font=('times', 8, 'bold underline'), bg='white', fg=get_foreground(), bd=0, activebackground='white', activeforeground='#4D4D4D')
        
        
    def bind_widgets(self):
        self.signup_button.configure(command=self.signup)
        self.login_button.configure(command=lambda: self.controller.show_frame(login_gui.LoginMenu))
        

    def place_widgets(self):
        self.name_entry.place(x=70, y=135)
        self.name_line.place(x=70, y=150)
        self.surname_entry.place(x=70, y=185)
        self.surname_line.place(x=70, y=205)
        self.username_entry.place(x=70, y=235)
        self.username_line.place(x=70, y=255)
        self.password_entry.place(x=70, y=285)
        self.password_line.place(x=70, y=305)
        self.signup_button.place(x=90, y=320)
        self.login_button.place(x=70, y=370)

    def insert_user_data(self):

        date = dt.datetime.strftime(dt.datetime.now(), "%d.%m.%Y %H:%M:%S")
        conn = sqlite3.connect('Pyflora.db')
        c = conn.cursor()
        c.execute("INSERT INTO UserData (Name, Surname, Username, Password, Date) VALUES (?,?,?,?,?)",
                    (self.name_entry.get(), self.surname_entry.get(), self.username_entry.get(), self.password_entry.get(), date))
        conn.commit()
    
    def check_if_exist(self):

        conn = sqlite3.connect('Pyflora.db')
        c = conn.cursor()

        c.execute("SELECT Username,Password FROM UserData WHERE (Username=? OR Password=?)",
                    [self.username_entry.get(), self.password_entry.get()])
        result = c.fetchone()
        if result:
            messagebox.showerror(
                "Error", "Username or password already exists!")
            self.controller.show_frame(SigninMenu)
            self.clear()
        else:
            self.insert_user_data()
            self.controller.show_frame(login_gui.LoginMenu)
            messagebox.showinfo("Success", "Thanks for signing up!")
            self.clear()

    def signup(self):
        
        if self.name_entry.get() == '' or self.surname_entry.get() == '' or self.username_entry.get() == '' or self.password_entry.get() == '':
                messagebox.showerror("Error", "All fields are required !")
                self.clear()
        else:
            self.check_if_exist()

    def clear(self):
        self.name_entry.delete(0, 25)
        self.surname_entry.delete(0, 25)
        self.username_entry.delete(0, 25)
        self.password_entry.delete(0, 25)

    

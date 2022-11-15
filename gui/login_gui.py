import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.util import create_label, create_smaller_label, get_image, get_foreground, create_frame, forgot_password
from gui import list_gui, basil_gui, hosta_gui, signin_gui
import sqlite3


class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('indoor_trees.jpg', self)
        create_frame(self, 300, 200)
        create_label(self, "Py Flora", 360, 110)

        username_var = tk.StringVar()
        create_smaller_label(self, "Username", 320, 150)
        username_entry = ttk.Entry(
            self, textvariable=username_var, width=25)
        username_entry.place(x=320, y=170)

        password_var = tk.StringVar()
        create_smaller_label(self, "Password", 320, 200)
        password_entry = ttk.Entry(
            self, textvariable=password_var, width=25, show="*")
        password_entry.place(x=320, y=220)

        forgot_password_button = tk.Button(
            self, text="Forgot password?", font=('times', 8), bg='white', fg=get_foreground(), bd=0, activebackground='white', activeforeground="#4D4D4D", command=forgot_password)
        forgot_password_button.place(x=395, y=245)

        create_smaller_label(self, "Don't have an account?", 320, 330)

        def clear_user_data():
            username_entry.delete(0, 25)
            password_entry.delete(0, 25)

        def use_userdata():
            conn = sqlite3.connect('Sensors.db')
            c = conn.cursor()

            c.execute("SELECT Username,Password FROM UserData WHERE (Username=? AND Password=?)",
                      [username_entry.get(), password_entry.get()])
            result = c.fetchone()
            if result:
                controller.show_frame(list_gui.SecondPage)
                messagebox.showinfo("Success", "Successfully logged in!")
            else:
                messagebox.showerror(
                    "Error", "Incorrect Username or password!")
                controller.show_frame(LoginMenu)
                clear_user_data()

        def log_in():
            if username_entry.get() == "bruce" and password_entry.get() == '1234':
                controller.show_frame(list_gui.SecondPage)
                messagebox.showinfo("Success", "Successfully logged in!")

            elif username_entry.get() == '' or password_entry.get() == '':
                messagebox.showerror("Error", "All fields are required !")
                clear_user_data()
            else:
                use_userdata()

        log_in_button = ttk.Button(
            self, text="Log in", width=10, command=log_in)
        log_in_button.place(x=360, y=280)

        signup_button = tk.Button(
            self, text="Sign up", font=('times', 8, 'bold underline'), bg='white', fg=get_foreground(), bd=0, activebackground='white', activeforeground='#4D4D4D', command=lambda: controller.show_frame(signin_gui.SigninMenu))
        signup_button.place(x=320, y=350)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.resizable(width=False, height=False)

        self.frames = {}
        for i in (LoginMenu, signin_gui.SigninMenu, list_gui.SecondPage, basil_gui.BasilPage, hosta_gui.HostaPage):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginMenu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

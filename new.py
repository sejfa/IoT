import tkinter as tk
from tkinter import FLAT, ttk
from tkinter import messagebox
from utils.util import create_label, create_smaller_label, get_image, get_foreground, create_frame, forgot_password
from gui import basil_gui, hosta_gui, main_menu, signin_gui, add_plant_gui

import sqlite3
import customtkinter



class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self._controller = controller
        self._create_widgets()
        self._place_widgets()
        self._bind_widgets()

    def _create_widgets(self):
        self._background_image = get_image("indoor_trees.jpg", self)
        self._frame = create_frame(self, 300, 200, 300, 100)
        self._title = create_label(self, "Py Flora", 360, 110)

        self._username_var = tk.StringVar()
        self._username_label = create_smaller_label(self, "Username", 320, 150)
        self._username_entry = tk.Entry(self, width=25, fg="black", bg="white", border=0, textvariable=self._username_var)
        self._username_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")

        self._password_var = tk.StringVar()
        self._password_label = create_smaller_label(self, "Password", 320, 200)
        self._password_entry = tk.Entry(self, width=25, fg="black", bg="white", border=0, textvariable=self._password_var, show="*")
        self._password_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")

        self._forgot_password_button = tk.Button(self, text="Forgot password?", font=("times", 8), bg="white", fg="black", bd=0, activebackground="white", activeforeground="#4D4D4D")
        self._no_account_label = create_smaller_label(self, "Don't have an account?", 320, 340)
        self._signup_button = tk.Button(self, text="Sign up", font=("times", 8, "bold underline"), bg="white", fg=get_foreground(), bd=0, activebackground="white", activeforeground="#4D4D4D")
        self._login_button = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Log in", bg_color="white")

    def _place_widgets(self):
        self._username_entry.place(x=320, y=175)
        self._username_line.place(x=320, y=195)
        self._password_entry.place(x=320, y=230)
        self._password_line.place(x=320, y=245)
        self._forgot_password_button.place(x=395, y=255)
        self._signup_button.place(x=320, y=360)
        self._login_button.place(x=345, y=290)
    
    def _bind_widgets(self):
        self._forgot_password_button.config(command=self._forgot_password)
        self._signup_button.config(command=lambda: self._controller.show_frame(signin_gui.SigninMenu))
        self._login_button.config(command=self._log_in)

    def _clear_user_data(self):
        self._username_entry.delete(0, 25)
        self._password_entry.delete(0, 25)

    def _use_userdata(self):
        conn = sqlite3.connect('PyFlora.db')
        c = conn.cursor()

        c.execute("SELECT Username,Password FROM UserData WHERE (Username=? AND Password=?)",
                  [self._username_entry.get(), self._password_entry.get()])
        result = c.fetchone()
        if result:
            self._controller.show_frame(main_menu.SecondPage)
        else:
            messagebox.showerror("Error", "Incorrect Username or password!")
            self._controller.show_frame(LoginMenu)
            self._clear_user_data()

    def _log_in(self):
        if self._username_entry.get() == "bruce" and self._password_entry.get() == '1234':
            self._controller.show_frame(main_menu.SecondPage)
        elif self._username_entry.get() == '' or self._password_entry.get() == '':
            messagebox.showerror("Error", "All fields are required !")
            self._clear_user_data()
        else:
            self._use_userdata()
            self._clear_user_data()
            
#################################################################################################################################################

class SigninMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.get_image('bc.jpg', self)
        self._create_frame(330, 200, 50, 70)
        self._create_label("Py Flora", 110, 80)

        self.name_var = tk.StringVar()
        self._create_smaller_label("Name", 70, 110)
        self.name_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.name_var)
        self.name_entry.place(x=70, y=135)
        self._create_line(70, 150, 155)

        self.surname_var = tk.StringVar()
        self._create_smaller_label("Surname", 70, 160)
        self.surname_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.surname_var)
        self.surname_entry.place(x=70, y=185)
        self._create_line(70, 205, 155)

        self.username_var = tk.StringVar()
        self._create_smaller_label("Username", 70, 210)
        self.username_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.username_var)
        self.username_entry.place(x=70, y=235)
        self._create_line(70, 255, 155)

        self.password_var = tk.StringVar()
        self._create_smaller_label("Password", 70, 260)
        self.password_entry = tk.Entry(master=self, width=25, fg="black", bg="white", border=0, textvariable=self.password_var, show="*")
        self.password_entry.place(x=70, y=285)
        self._create_line(70, 305, 155)

        self._create_smaller_label("Already have an account?", 70, 350)

        self.signup_button = tk.Button(master=self, text="Signup", command=self.on_signup)
        self.signup_button.place(x=210, y=320)

    def on_signup(self):
        if self._check_if_exist():
            messagebox.showerror("Error", "Username or password already exists!")
            self.controller.show_frame(SigninMenu)
            self.clear()
        else:
            self._insert_user_data()
           # self.controller.show_frame(login_gui.LoginMenu)
            messagebox.showinfo("Success", "Thanks for signing up!")
            self.clear()

    def clear(self):
        self.name_entry.delete(0, 25)
        self.surname_entry.delete(0, 25)
        self.username_entry.delete(0, 25)
        self.password_entry.delete(0, 25)

############################################################################################################################

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, background="white")
        self.controller = controller
        self.get_image('gp.jpg',self)
        self.f1 = None
        self.create_button_frame()

    def create_button_frame(self):
        def add_plant_menu():
            self.f1.destroy()
            self.controller.show_frame(add_plant_gui.AddPlant)
            self.toggle_win()
            self.f1.destroy()

        def toggle_win():
            self.f1 = tk.Frame(self, width=300, height=500, bg='white')
            self.f1.place(x=0, y=0)
            self.create_button(0, 154, "POTS", command=None)
            self.create_button(0, 191, "PLANTS", command=add_plant_menu)
            self.create_button(0, 228, "ABOUT", command=None)
            self.create_close_button(5, 10, command=self.f1.destroy)

        self.create_open_button(5, 10, command=toggle_win)

    def create_button(self, x, y, text, command):
        bttn = tk.Button(self.f1, text=text, width=42, height=2, fg='#262626', border=0, bg='white', command=command)
        bttn.place(x=x, y=y)
        bttn.bind("<Enter>", lambda e: self.on_enter(e, bttn, '#e6e6e6', '#262626'))
        bttn.bind("<Leave>", lambda e: self.on_leave(e, bttn, 'white', '#262626'))

    def create_open_button(self, x, y, command):
        root_folder_path = 'media'
        image_name = 'open.png'
        load = Image.open(f"{root_folder_path}/{image_name}")
        photo = ImageTk.PhotoImage(load)
        label_basil1 = tk.Label(self, image=photo)
        label_basil1.image = photo
        label_basil1.place(x=x, y=y)
        button = tk.Button(self, image=photo, border=0, command=command, bg='grey')
        button.place(x=x, y=y)

    def create_close_button(self, x, y, command):
        root_folder_path = 'media'
        image_name = 'close.png'
        load = Image.open(f"{root_folder_path}/{image_name}")
        photo = ImageTk.PhotoImage(load)
        label_basil1 = tk.Label(self.f1, image=photo)
        label_basil1.image = photo
        label_basil1.place(x=5, y=10)
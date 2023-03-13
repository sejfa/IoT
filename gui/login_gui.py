from copyreg import constructor
import sqlite3
import tkinter as tk
import customtkinter
from tkinter import FLAT, ttk
from tkinter import messagebox
from gui import kitchen_shelf_by_the_window, basil_gui,ginger_gui, hosta_gui,lilie_gui, rose_gui, living_room_table_near_the_couch,balcony_near_window,bedroom_near_the_bed, main_menu, recordofplant, recordofpots, signin_gui, plant_list, pot_list
from utils.util import create_label, create_smaller_label, get_image, get_foreground, create_frame, forgot_password



class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()
    
    def create_widgets(self):
        self.background_image = get_image("indoor_trees.jpg", self)
        self.frame = create_frame(self, 300, 200, 300, 100)
        self.title = create_label(self, "Py Flora", 360, 110)

        self.username_var = tk.StringVar()
        self.username_label = create_smaller_label(self, "Username", 320, 150)
        self.username_entry = tk.Entry(self, width=25, fg="black", bg="white", border=0, textvariable=self.username_var)
        self.username_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")

        self.password_var = tk.StringVar()
        self.password_label = create_smaller_label(self, "Password", 320, 200)
        self.password_entry = tk.Entry(self, width=25, fg="black", bg="white", border=0, textvariable=self.password_var, show="*")
        self.password_line = tk.Canvas(self, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")

        self.forgot_password_button = tk.Button(self, text="Forgot password?", font=("times", 8), bg="white", fg="black", bd=0, activebackground="white", activeforeground="#4D4D4D", command=forgot_password)
        self.no_account_label= create_smaller_label(self, "Don't have an account?", 320, 340)
        self.signup_button = tk.Button(self, text="Sign up", font=("times", 8, "bold underline"), bg="white", fg=get_foreground(), bd=0, activebackground="white", activeforeground="#4D4D4D")
        self.login_button = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Log in", bg_color="white")

    def place_widgets(self):
        self.username_entry.place(x=320, y=175)
        self.username_line.place(x=320, y=195)
        self.password_entry.place(x=320, y=230)
        self.password_line.place(x=320, y=245)
        self.forgot_password_button.place(x=395, y=255)
        self.signup_button.place(x=320, y=360)
        self.login_button.place(x=345, y=290)

    def bind_widgets(self):
        self.signup_button.configure(command=lambda: self.controller.show_frame(signin_gui.SigninMenu))
        self.login_button.configure(command=self.log_in)

    def clear_user_data(self):
        self.username_entry.delete(0, 25)
        self.password_entry.delete(0, 25)

    def use_userdata(self):
        conn = sqlite3.connect('PyFlora.db')
        c = conn.cursor()

        c.execute("SELECT Username,Password FROM UserData WHERE (Username=? AND Password=?)",
                  [self.username_entry.get(), self.password_entry.get()])
        result = c.fetchone()
        if result:
            self.controller.show_frame(main_menu.SecondPage)
        else:
            messagebox.showerror("Error", "Incorrect Username or password!")
            self.controller.show_frame(LoginMenu)
            self.clear_user_data()
    
    def log_in(self):
        if self.username_entry.get() == "as" and self.password_entry.get() == 'as':
            self.controller.show_frame(main_menu.SecondPage)
        elif self.username_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror("Error", "All fields are required !")
            self.clear_user_data()
        else:
            self.use_userdata()
            self.clear_user_data()

    
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.resizable(width=False, height=False)

        self.frames = {}
        windows = [LoginMenu, signin_gui.SigninMenu, main_menu.SecondPage,basil_gui.BasilPage,ginger_gui.GingerPage,lilie_gui.LiliePage, rose_gui.RosePage, kitchen_shelf_by_the_window.KitchenBasilPage, hosta_gui.HostaPage, living_room_table_near_the_couch.LivingRoomHosta, recordofpots.RecordOfPots, plant_list.PlantList, pot_list.PotList, recordofplant.RecordOfPlants,balcony_near_window.BalconyNearWindow, bedroom_near_the_bed.BedroomNearBed]
        for i,constructor in enumerate(windows):
            frame = constructor(window, self)
            self.frames[constructor] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.frames[recordofplant.RecordOfPlants].set_plant_list_reference(self.frames[plant_list.PlantList])
        self.frames[recordofpots.RecordOfPots].set_pot_list_reference(self.frames[pot_list.PotList])
        
        self.show_frame(LoginMenu)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


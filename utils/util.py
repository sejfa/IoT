import sqlite3
import customtkinter
import tkinter as tk
from tkinter import *
import datetime as dt
from PIL import Image, ImageTk
from tkinter import ttk, Toplevel, messagebox



def add_plant():

    conn = sqlite3.connect('PyFlora.db')
    c = conn.cursor()
    c.execute("SELECT Plant FROM RecordsOfPlants")
    result = c.fetchall()
    new_list = [i for i, in result]
    return new_list



def clear(name):
    name.delete(0,25)

def clear_user_data(self):
        self.username_entry.delete(0, 25)
        self.password_entry.delete(0, 25)

def create_frame(root, height, width, x, y):
    """"Function that creates Frame with arbitrary dimensions
    """

    frame = customtkinter.CTkFrame(master=root,
                                   width=width,
                                   height=height,
                                   fg_color="white",
                                   border_color="light grey",
                                   border_width=4

                                   )
    frame.place(x=x, y=y)


def create_button(root, text, controller, page, x, y):

    button = customtkinter.CTkButton(master=root,
                                     width=100,
                                     height=15,
                                     border_width=0,
                                     corner_radius=12,
                                     bg_color="white",
                                     text=text,
                                     command=lambda: controller.show_frame(page))
    button.place(x=x, y=y)

    return button


def bttn(self,x,y,text,bcolor,fcolor,cmd):

    def on_entera(e):
        myButton1['background'] = bcolor #ffcc66
        myButton1['foreground'] = '#262626'  #000d33

    def on_leavea(e):
        myButton1['background'] = fcolor
        myButton1['foreground'] = '#262626'

    myButton1 = Button(self,text=text,
                width=35,
                height=2,
                fg='#262626',
                border=0,
                bg=fcolor,
                activeforeground='#262626',
                activebackground=bcolor,            
                    command=cmd)
                
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)



def create_header(root, text, x, y):

    header = ttk.Label(root, text=text, background="#f6f6f6",
                       foreground=get_foreground(), font=get_header_font())
    header.place(x=x, y=y)
    return header


def create_label(root, text, x, y):

    label = ttk.Label(root, text=text, background="white",
                      foreground=get_foreground(), font=get_label_font())
    label.place(x=x, y=y)
    return label


def create_smaller_label(root, text, x, y):

    label = ttk.Label(root, text=text, background='white',
                      foreground=get_foreground(), font=get_status_font())
    label.place(x=x, y=y)
    return label

def small_label(root, text, x, y):

    label = ttk.Label(root, text=text, background='#f6f6f6',
                      foreground=get_foreground(), font=get_status_font())
    label.place(x=x, y=y)
    return label



def formatted_date():
    """Function that uses strftime format for dates.
    """
    today = dt.datetime.now()

    return today.strftime("%A, %d %B %Y")


def formatted_time():
    """Function that uses strftime format for time.
    """
    now_time = dt.datetime.now()

    return now_time.strftime("%H:%M:%S")


def get_background():
    """Function that defines background in LableFrame widget.
    """
    background = 'white'
    return background


def get_foreground():
    """Function that defines foreground in Lable widget.
    """
    foreground = '#4D4D4D'
    return foreground


def get_fg():
    """Function that defines color in Label
    """
    fg = '#808080'
    return fg


def get_header_font():
    font_style = 'Times New Roman', '18', 'bold italic'
    return font_style


def get_label_font():
    font_style = 'Times New Roman', '14', 'bold italic'
    return font_style


def get_status_font():
    font_style = 'arial', '8', 'bold'
    return font_style


def get_image(image_name, root):
    
    global photo1
    
    root_folder_path = 'media'
    load = Image.open(f"{root_folder_path}/{image_name}")
    photo1 = ImageTk.PhotoImage(load)

    label_basil1 = tk.Label(root, image=photo1)
    label_basil1.image = photo1
    label_basil1.place(x=0, y=0)


def login(root, text, a, b, c, d):

    name_var = tk.StringVar()
    name_Label = tk.Label(root, text=text,
                          fg=get_fg())
    name_Label.place(x=a, y=b)
    name_entry = ttk.Entry(
        root, textvariable=name_var, width=25)
    name_entry.place(x=c, y=d)


def forgot_password():

    new_window = Toplevel(background="white")
    new_window.title("Reset password")
    new_window.geometry("210x260+300+200")
    new_window.resizable(width=False, height=False)

    create_label(new_window, "Reset password", 40, 20)
    create_smaller_label(new_window, "Username", 25, 60)
    create_smaller_label(new_window, "New password", 25, 110)
    create_smaller_label(new_window, "Confirm password", 25, 160)

    username_var = tk.StringVar()
    username_entry = tk.Entry(new_window, width=25, fg="black", bg="white", border=0, textvariable=username_var)
    username_line = tk.Canvas(new_window, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
    username_entry.place(x=25, y=80)
    username_line.place(x=25, y=100)

    new_password_var = tk.StringVar()
    new_password_entry = tk.Entry(new_window, width=25, fg="black", bg="white", border=0, textvariable=new_password_var, show="*")
    new_password_line = tk.Canvas(new_window, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
    new_password_entry.place(x=25, y=130)
    new_password_line.place(x=25, y=150)

    confirm_var = tk.StringVar()
    confirm_entry = tk.Entry(new_window, width=25, fg="black", bg="white", border=0, textvariable=confirm_var, show="*")
    confirm_line = tk.Canvas(new_window, width=155, highlightthickness=0, relief=FLAT, height=1, bg="black")
    confirm_entry.place(x=25, y=180)
    confirm_line.place(x=25, y=200)


    def clear_data():
        username_entry.delete(0, 25)
        new_password_entry.delete(0, 25)
        confirm_entry.delete(0, 25)

    def change_password():

        conn = sqlite3.connect('Pyflora.db')
        c = conn.cursor()
        c.execute("SELECT * FROM UserData WHERE Username=?",
                  [username_entry.get()])

        result = c.fetchone()
        if result:
            c.execute("UPDATE UserData set Password=? WHERE Username=? ",
                      [new_password_entry.get(), username_entry.get()])
            messagebox.showinfo(
                "Success", "Successfully changed password, You can now login with new password!")

        else:
            messagebox.showerror(
                "Error", "Incorrect Username", parent=new_window)
            clear_data()

        conn.commit()
        

    def submit():

        if username_entry.get() == '' or new_password_entry.get() == '' or confirm_entry.get() == '':
            messagebox.showerror(
                "Error", "All field are required !", parent=new_window)
            clear_data()

        elif new_password_entry.get() != confirm_entry.get():
            messagebox.showerror(
                "Error", "Passwords doesn't match, please try again!", parent=new_window)
            clear_data()

        elif new_password_entry.get() == confirm_entry.get():
            change_password()

    submit_button = customtkinter.CTkButton(new_window, width=100, height=15, border_width=0, corner_radius=13, text="Submit", bg_color="white", command=submit)
    submit_button.place(x=50, y=220)

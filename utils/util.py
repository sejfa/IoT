import datetime as dt
from tkinter import Toplevel


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


def login(root, text, a, b, c, d):
    import tkinter as tk
    from tkinter import ttk

    name_var = tk.StringVar()
    name_Label = tk.Label(root, text=text,
                          fg=get_fg())
    name_Label.place(x=a, y=b)
    name_entry = ttk.Entry(
        root, textvariable=name_var, width=25)
    name_entry.place(x=c, y=d)


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


def create_frame(root, height, width):
    """"Function that creates Frame with arbitrary dimensions
    """
    import tkinter as ttk
    main_frame = ttk.Frame(root, height=height, width=width,
                           background="white", relief='solid')
    main_frame.place(x=300, y=100)


def get_label_font():
    font_style = 'Times New Roman', '15', 'bold italic'
    return font_style


def get_status_font():
    font_style = 'arial', '8'
    return font_style


def get_image(image_name, root):
    import tkinter as tk
    from PIL import Image, ImageTk

    root_folder_path = 'media'
    load = Image.open(f"{root_folder_path}/{image_name}")
    photo1 = ImageTk.PhotoImage(load)

    label_basil1 = tk.Label(root, image=photo1)
    label_basil1.image = photo1
    label_basil1.place(x=0, y=0)


def create_button(root, text, controller, page, width, x, y):
    from tkinter import ttk
    button = ttk.Button(root, text=text, width=width,
                        command=lambda: controller.show_frame(page))
    button.place(x=x, y=y)
    return button


def create_label(root, text, x, y):
    from tkinter import ttk
    label = ttk.Label(root, text=text, background="white",
                      foreground=get_foreground(), font=get_label_font())
    label.place(x=x, y=y)
    return label


def create_smaller_label(root, text, x, y):
    from tkinter import ttk
    label = ttk.Label(root, text=text, background='white',
                      foreground=get_foreground(), font=get_status_font())
    label.place(x=x, y=y)
    return label


def forgot_password():

    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    import sqlite3

    new_window = Toplevel(background="white")
    new_window.title("Reset password")
    new_window.geometry("210x260+300+200")

    create_label(new_window, "Reset password", 40, 20)

    username_var = tk.StringVar()
    create_smaller_label(new_window, "Username", 25, 60)
    username_entry = ttk.Entry(
        new_window, textvariable=username_var, width=25)
    username_entry.place(x=25, y=80)

    new_password_var = tk.StringVar()
    create_smaller_label(new_window, "New password", 25, 110)
    new_password_entry = ttk.Entry(
        new_window, textvariable=new_password_var, width=25, show="*")
    new_password_entry.place(x=25, y=130)

    confirm_var = tk.StringVar()
    create_smaller_label(new_window, "Confirm password", 25, 160)
    confirm_entry = ttk.Entry(
        new_window, textvariable=confirm_var, width=25, show="*")
    confirm_entry.place(x=25, y=180)

    def clear_data():
        username_entry.delete(0, 25)
        new_password_entry.delete(0, 25)
        confirm_entry.delete(0, 25)

    def change_password():

        conn = sqlite3.connect('Sensors.db')
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
        conn.close()

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

    submit_button = ttk.Button(
        new_window, text="Submit", width=12, command=submit)
    submit_button.place(x=60, y=220)

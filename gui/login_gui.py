import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from svi_crudovi.crud import get_image, get_foreground, get_label_font, get_fg
from gui import list_gui, basil_gui, hosta_gui, signin_gui


class LoginMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        get_image('pl.jpg', self)

        heading_label = tk.Label(self, text="Py Flora",
                                 foreground=get_foreground(), font=get_label_font())
        heading_label.place(x=350, y=100)

        username_var = tk.StringVar()
        username_Label = tk.Label(self, text="Username",
                                  fg=get_fg())
        username_Label.place(x=310, y=140)
        username_entry = ttk.Entry(
            self, textvariable=username_var, width=25)
        username_entry.place(x=310, y=160)

        password_var = tk.StringVar()
        password_Label = tk.Label(self, text="Password",
                                  fg=get_fg())
        password_Label.place(x=310, y=190)
        password_entry = ttk.Entry(
            self, textvariable=password_var, width=25, show="*")
        password_entry.place(x=310, y=210)

        no_account = tk.Label(self, text="Don't have an account?", foreground=get_foreground(), font=(
            'times', '8'))
        no_account.place(x=310, y=300)

        def log_in():
            if username_entry.get() == 'brucewayne' and password_entry.get() == '1234':
                controller.show_frame(list_gui.SecondPage)

            elif username_entry.get() == '' or password_entry.get() == '':
                messagebox.showerror("Error", "All fields are required !")

            else:
                messagebox.showerror("Error", "Invalid input!")

        login_button = ttk.Button(
            self, text="Log in", width=10, command=log_in)
        login_button.place(x=345, y=245)

        login_button = tk.Button(
            self, text="Sign up", font=('times', 8, 'bold underline'), bg='#E5E5E5', fg=get_foreground(), bd=0, activebackground='#E5E5E5', activeforeground='blue', command=lambda: controller.show_frame(signin_gui.SigninMenu))
        login_button.place(x=310, y=320)


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

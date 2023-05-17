import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk, HORIZONTAL
from gui.login_gui import LoginMenu
from utils.util import get_image
w=tk.Tk()

width_of_window = 800
height_of_window = 500
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=810,mode='determinate')

def new_win():
  # w.destroy()
    q=tk.Tk()
    q.title('Main window')
    q.geometry('427x250')
    l1=tk.Label(q,text='ADD TEXT HERE ',fg='grey',bg=None)
    l=('Calibri (Body)',24,'bold')
    l1.config(font=l)
    l1.place(x=80,y=100)

    #mojloginscreen = LoginMenu(q, objekt_s_funkcijom_showframe)
    
    q.mainloop()

def bar():

    l4=tk.Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=370,y=460)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.01)
        r=r+1
    
    w.destroy()
    new_win()
        
progress.place(x=-10,y=485)

a='#f1f1f1'

frame = tk.Frame(w,width=800,height=490,bg='#f1f1f1').place(x=0,y=0)  #249794
get_image('w.png',frame)
b1=tk.Button(w,width=10,height=1,text='Get Started',font= 10,command=bar,border=0,fg='#023020',bg=a, activebackground=a, activeforeground='#023020')
b1.place(x=350,y=410)

w.mainloop()







































######## Label

"""l1=tk.Label(w,text='SPLASH',fg='#023020',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=tk.Label(w,text='SCREEN',fg='#023020',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=155,y=82)

l3=tk.Label(w,text='PROGRAMMED',fg='#023020',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)
"""
  




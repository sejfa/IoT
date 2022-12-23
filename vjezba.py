from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import os

ws = Tk()
ws.title('Select Input Files')
ws.geometry('400x300') 


def open_file():
    file_path = askopenfile(initialdir='C:\Alem\Programiranje\python_vsc\Zavrsni_AS\media', mode='r', filetypes=[('*.jpg','*.png')])

    if file_path is not None:
        # this gets the full path of your selected file
        filename = file_path.name
        # this is only selecting the name with file extension
        filename = os.path.basename(filename)
        # to replace your Label you first have to destroy the other label
        up1.destroy()
        # then create a new label with the filename
        file_label = Label(ws, text=filename).grid(row=0, column=0, padx=10)
        # you can even change the title of your tkinter window if you want
        ws.title('Select Input Files -- ' + filename)

up1 = Label(
    ws, 
    text='sales_history_document '
    )
up1.grid(row=0, column=0, padx=10)

btn1 = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    )

btn1.grid(row=0, column=1)

up2 = Label(
    ws, 
    text='style_group_document '
    )
up2.grid(row=1, column=0, padx=10)

btn2 = Button(
    ws, 
    text ='Choose File ', 
    command = lambda:open_file()
    ) 
btn2.grid(row=1, column=1)

ws.mainloop()
import tkinter  as tk 
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import io
import sqlite3
my_w = tk.Tk()
my_w.geometry("400x250") 
my_w.title("www.plus2net.com")  # Adding a title
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError



conn = sqlite3.connect('another.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS student_profile (id,student,profile_photo)")
try:
    my_row=c.execute("SELECT student FROM student_profile")
    my_list = [r for r, in my_row]
except SQLAlchemyError as e:
  error=str(e.__dict__['orig'])
  print(error)    
options = tk.StringVar(my_w)
#options.set(my_list[0]) # default value

om1 =tk.OptionMenu(my_w, options, *my_list)
om1.grid(row=1,column=1,padx=30)
global name
def my_show(*args):  # on select function 
    global name
    for i in my_list:
        if i==options.get():
            display_data(i)
            name=i            
my_font=('times', 12, 'bold')
b2 = tk.Button(my_w, text='Upload File', 
   command = lambda:upload_file())
b2.grid(row=1,column=4) 
my_font1=('times', 18, 'bold')
b3 = tk.Button(my_w, text='Update',font=my_font1,
   command = lambda:update_data())
b3.grid(row=1,column=5,padx=10) 

global img2
images = [] # to manage garbage collection. 
def display_data(name):
    query="SELECT id,student,profile_photo FROM student_profile WHERE student=?"
    data=(name,)
    my_row=c.execute(query,data)
    student = my_row.fetchone()
    img = Image.open(io.BytesIO(student[2]))
    img = ImageTk.PhotoImage(img)
    
    l1=tk.Label(my_w,text=student[0])
    l1.grid(row=1,column=2,ipadx=10)
    l2=tk.Label(my_w,text=student[1])
    l2.grid(row=1,column=3)
    l3 = tk.Label(my_w,image=img )
    l3.grid(row=3,column=1) 
    images.append(img) # garbage collection 
global filename2
def upload_file(): # Image upload and display
    global filename2,img2
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename2 = filedialog.askopenfilename(filetypes=f_types)
    img2 = ImageTk.PhotoImage(file=filename2)
    b2 =tk.Button(my_w,image=img2) # using Button 
    b2.grid(row=3,column=2,columnspan=3)#display uploaded photo    
    images.append(img2) # garbage collection 
def update_data(): # Update data to MySQL table 
    global filename2 , name
    fob=open(filename2,'rb') # filename from upload_file()
    fob=fob.read()
    data=(fob,name) # tuple with data 
    c.execute("UPDATE student_profile set profile_photo=? WHERE student=?",data)
    
    my_w.destroy() # close window after adding data    
options.trace('w',my_show)
my_w.mainloop()
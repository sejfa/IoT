import tkinter as tk
import sqlite3
from tkinter import ttk

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS  table1 (Plant_id INTEGER PRIMARY KEY, Plant TEXT, Photo BLOB)')
cursor.execute('CREATE TABLE IF NOT EXISTS  table2 (Pot_id INTEGER PRIMARY KEY, Pot TEXT, Photo BLOB)')
# Retrieve data from table1
cursor.execute("SELECT * FROM table1")
data1 = cursor.fetchall()

# Retrieve data from table2
cursor.execute("SELECT * FROM table2")
data2 = cursor.fetchall()

# Create the Tkinter window and TabView widget
root = tk.Tk()
root.title("Data Viewer")
tabview = ttk.Notebook(root)

# Create the Frames for each tab
tab1_frame = tk.Frame(tabview)
tab2_frame = tk.Frame(tabview)

# Create Treeview widgets to display the data
tree1 = ttk.Treeview(tab1_frame)
tree2 = ttk.Treeview(tab2_frame)

# Insert the data into the Treeviews
for row in data1:
    tree1.insert("", "end", values=row)
    
for row in data2:
    tree2.insert("", "end", values=row)

# Pack the Frames into the TabView
tabview.add(tab1_frame, text="Table 1")
tabview.add(tab2_frame, text="Table 2")

tabview.pack(expand=1, fill="both")

root.mainloop()
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sqlite3
import datetime

from numpy import place


# Connect to the SQLite database
conn = sqlite3.connect('PyFlora.db')
cursor = conn.cursor()


# Get data for pie chart
cursor.execute('SELECT Value FROM Humidity')
value1 = cursor.fetchone()[0]
cursor.execute('SELECT Value FROM Temperature')
value2 = cursor.fetchone()[0]
cursor.execute('SELECT Value FROM Brightness')
value3 = cursor.fetchone()[0]
cursor.execute('SELECT Value FROM pH')
value4 = cursor.fetchone()[0]
cursor.execute('SELECT Value FROM Salinity')
value5 = cursor.fetchone()[0]

# Get data for line chart and histogram
time_values = [datetime.datetime(2023, 3, 3, hour=i).strftime('%H') for i in range(24)]

# Get data for line chart and histogram
cursor.execute('SELECT * FROM Humidity ORDER BY RANDOM() LIMIT 24')
data = cursor.fetchall()
value_values = [row[1] for row in data]


# Create the GUI
root = tk.Tk()
root.title('PyFlora Charts')
root.geometry('600x280')

# Create a notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create the first tab for the pie chart
tab1 = tk.Frame(notebook)
notebook.add(tab1, text='Pie Chart')

# Create the pie chart
fig1, axs1 = plt.subplots(figsize=(5, 5))
axs1.pie([value1, value2, value3, value4, value5], labels=['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity'])
axs1.set_title('Pie Chart')
axs1.legend(labels=['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity'])
canvas1 = FigureCanvasTkAgg(fig1, tab1)
canvas1.draw()
canvas1.get_tk_widget().pack(fill='both', expand=True)

# Create the second tab for the line chart
tab2 = tk.Frame(notebook)
notebook.add(tab2, text='Line Chart')

# Create the line chart
fig2, axs2 = plt.subplots(figsize=(5, 5))
axs2.plot(time_values, value_values)
axs2.set_xlabel('Time')
axs2.set_ylabel('Value')
axs2.set_title('Line Chart')
canvas2 = FigureCanvasTkAgg(fig2, tab2)
canvas2.draw()
canvas2.get_tk_widget().pack(fill='both', expand=True)


# Create the third tab for the histogram
tab3 = tk.Frame(notebook)
notebook.add(tab3, text='Histogram')

# Create the histogram
fig3, axs3 = plt.subplots(figsize=(5, 5))
axs3.hist(value_values)
axs3.set_xlabel('Value')
axs3.set_ylabel('Frequency')
axs3.set_title('Histogram')
canvas3 = FigureCanvasTkAgg(fig3, tab3)
canvas3.draw()
canvas3.get_tk_widget().pack(fill='both', expand=True)

axs1.legend(labels=['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity'],bbox_to_anchor=(1.62, 0.46), loc='upper center')
axs2.legend(labels=['Value'], loc='best')
axs3.legend(labels=['Value'], loc='best')

# Run the GUI
root.mainloop()
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Charts")
        self.root.geometry("500x300")

        # Generate some random data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        data = np.random.normal(size=1000)

        # Create a notebook with tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Create tabs for each chart type
        self.line_tab = ttk.Frame(self.notebook)
        self.pie_tab = ttk.Frame(self.notebook)
        self.hist_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.line_tab, text='Line Chart')
        self.notebook.add(self.pie_tab, text='Pie Chart')
        self.notebook.add(self.hist_tab, text='Histogram')

        # Line chart
        self.fig1, self.ax1 = plt.subplots(figsize=(6, 4))
        self.ax1.plot(x, y)
        self.ax1.set_title("Line chart")
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.line_tab)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Pie chart
        self.labels = ["A", "B", "C", "D"]
        self.sizes = np.random.randint(1, 10, size=len(self.labels))
        self.fig2, self.ax2 = plt.subplots(figsize=(6, 4))
        self.ax2.pie(self.sizes, labels=self.labels)
        self.ax2.set_title("Pie chart")
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.pie_tab)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Histogram
        self.fig3, self.ax3 = plt.subplots(figsize=(6, 4))
        self.ax3.hist(data, bins=30)
        self.ax3.set_title("Histogram")
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.hist_tab)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
gui = GUI(root)
root.mainloop()
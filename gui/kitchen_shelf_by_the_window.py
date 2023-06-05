import customtkinter
import tkinter as tk
import numpy as np
from tkinter import ttk
from gui import pot_list
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.util import get_image, create_label, create_smaller_label, get_background, create_button, bttn
from crud.crud_db import sensor_hum, sensor_temp, sensor_bright, sensor_sal, sensor_ph


class KitchenBasilPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        self.controller = controller
        self.displayed = False
        self.graphical_info_exists = False
        self.create_widgets()
        self.place_widgets()
        self.bind_widgets()


    def create_widgets(self):
        self.basil_info = tk.LabelFrame(self, background=get_background())
        self.header = create_label(self.basil_info, "Kitchen - shelf by the window - Basil", 15, 5)
        self.pic_frame = ttk.Frame(self)
        self.pic_frame_image = get_image('basil.jpg', self.pic_frame)
        self.sync_button = ttk.Button(self, text="Sync", width=15)
        #self.optimal_button = ttk.Button(self, text="Set to optimal",width=20)
        self.back = customtkinter.CTkButton(master=self, width=100, height=15, border_width=0, corner_radius=13, text="Back", bg_color="white")
        self.graphical_button = ttk.Button(self, text="Show graphical info", width=20)
        
        #bttn(self, 2, 230, ' S Y N C ', '#e6e6e6','light grey', self.display_data)
        #bttn(self, 257, 230, '  S E T   T O   O P T I M A L  ', '#e6e6e6','light grey', self.display_optimal_data)

    def place_widgets(self):
        self.basil_info.place(x=2, y=2, width=483, height=215,)
        self.pic_frame.place(x=485, y=2, width=313, height=215)
        self.sync_button.place(x=20, y=230)
        #self.optimal_button.place(x=20, y=280)
        self.graphical_button.place(x=20, y=330)
        self.back.place(x=20, y=450)

    def bind_widgets(self):
        self.sync_button.configure(command=self.display_data)
        #self.optimal_button.configure(command=self.display_optimal_data)
        self.graphical_button.configure(command=self.toggle_graphical_info)
        self.back.configure(command=self.back_button)
        
    def display_data(self):
        
        if not self.displayed:
            self.h= sensor_hum()
            self.hum = create_smaller_label(self.basil_info, self.h, 10, 45)
            self.t = sensor_temp()
            self.temp = create_smaller_label(self.basil_info, self.t, 10, 80)
            self.b = sensor_bright()
            self.bright = create_smaller_label(self.basil_info, self.b, 10, 115)
            self.p = sensor_ph()
            self.ph = create_smaller_label(self.basil_info, self.p, 10, 150)
            self.s = sensor_sal()
            self.sal = create_smaller_label(self.basil_info, self.s, 10, 185)
            self.displayed = True
        
    """def display_optimal_data(self):

        self.hum.destroy()
        self.temp.destroy()
        self.bright.destroy()
        self.ph.destroy()
        self.sal.destroy()
        self.basil_info.update()

        self.opt_hum = get_optimal_hum()
        self.optimal_hum = create_smaller_label(self.basil_info, self.opt_hum, 15, 45)
        self.opt_temp = get_optimal_temp()
        self.optimal_temp = create_smaller_label(self.basil_info, self.opt_temp, 15, 80)
        self.opt_bright = get_optimal_bright()
        self.optimal_bright = create_smaller_label(self.basil_info, self.opt_bright, 15, 115)
        self.opt_ph = get_optmal_ph()
        self.optimal_ph = create_smaller_label(self.basil_info, self.opt_ph, 15, 150)
        self.opt_sal = get_optimal_sal()
        self.optimal_sal = create_smaller_label(self.basil_info, self.opt_sal, 15, 185)
""" 


    def toggle_graphical_info(self):
        
        if self.graphical_info_exists:
            self.graphical_info.destroy()
            self.graphical_info_exists = False
        else:
            self.graphical_info_exists = True 
            self.graphical_info = tk.LabelFrame(self)
            self.notebook = ttk.Notebook(self.graphical_info)
            self.line_tab = ttk.Frame(self.notebook)
            self.pie_tab = ttk.Frame(self.notebook)
            self.hist_tab = ttk.Frame(self.notebook)
            self.notebook.add(self.line_tab, text='Line Chart')
            self.notebook.add(self.pie_tab, text='Pie Chart')
            self.notebook.add(self.hist_tab, text='Histogram')
            
            #chart_data = self.get_chart_data()
            self.hum_value = int(self.h.split()[4])
            self.temp_value = int(self.t.split()[4])
            self.bright_value = int(self.b.split()[3])
            self.ph_value = int(self.p.split()[3])
            self.sal_value = int(self.s.split()[3])
            
            
            # Line chart
            self.fig1, self.ax1 = plt.subplots(figsize=(8,5))
            self.ax1.set_title("Line chart")
            data = [self.hum_value, self.temp_value, self.bright_value, self.ph_value, self.sal_value]
            labels = ['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity']
            x = labels
            for i in range(len(data)):
                self.ax1.plot(x[i], data[i], marker='o')
            self.ax1.set_xlabel("Parameter")
            self.ax1.set_ylabel("Value")
            self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.line_tab)
            self.canvas1.draw()
            self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            # Pie chart
            self.fig2, self.ax2 = plt.subplots(figsize=(5, 5))
            self.ax2.pie(data, labels=['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity'])
            self.ax2.set_title('Pie Chart')
            self.canvas2 = FigureCanvasTkAgg(self.fig2, self.pie_tab)
            self.canvas2.draw()
            self.canvas2.get_tk_widget().pack(fill='both', expand=True)

            # Histogram
            self.fig3, self.ax3 = plt.subplots(figsize=(7, 5))
            labels = ['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity']
            colors = ['Blue', 'Red', 'Orange', 'Yellow', 'Green']
            bins = np.linspace(min(data), max(data), 30)
            for i in range(len(data)):
                self.ax3.hist(data[i], bins=bins, alpha=0.5, label=labels[i], color=colors[i], linewidth=4, histtype='bar')
            self.ax3.set_title("Histogram")
            self.ax3.legend()
            self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.hist_tab)
            self.canvas3.draw()
            self.canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


            self.graphical_info.place(x=200,y=220, width=600, height=280)
            self.notebook.pack(fill='both', expand=True)

            # Legends
            self.ax1.legend(labels=['Humidity','Temperature', 'Brightness', 'pH', 'Salinity'], loc='upper right',fontsize=8.5)
            self.ax2.legend(labels=['Humidity', 'Temperature', 'Brightness', 'pH', 'Salinity'],bbox_to_anchor=(1.62, 0.46), loc='upper center',fontsize=9.5)
            self.ax3.legend(labels=['Humidity','Temperature', 'Brightness', 'pH', 'Salinity'], loc='upper right',fontsize=8.6)

    def back_button(self):
        self.controller.show_frame(pot_list.PotList)
        
        
        
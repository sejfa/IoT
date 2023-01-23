import tkinter as tk
my_w = tk.Tk()
my_w.geometry("350x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_list = ["PHP","MySQL","Python","HTML","JQuery"]
options = tk.StringVar(my_w)
options.set(my_list[0]) # default value

om1 =tk.OptionMenu(my_w, options, *my_list)
om1.grid(row=2,column=5) 

b1 = tk.Button(my_w,  text='Remove All', command=lambda: my_remove() )  
b1.grid(row=1,column=2)

b2 = tk.Button(my_w,  text='Add All Opt', command=lambda: my_add() )  
b2.grid(row=2,column=2)

b3 = tk.Button(my_w,  text='Remove Selectd', command=lambda: my_remove_sel() )  
b3.grid(row=3,column=2)

def my_remove():
    options.set('') # remove default selection only, not the full list
    om1['menu'].delete(0,'end') # remove full list 
def my_add():
    my_remove() # remove all options 
    for opt in my_list: 
        om1['menu'].add_command(label=opt, command=tk._setit(options, opt))
    options.set(my_list[0]) # default value set 

def my_remove_sel():
    r_index=om1['menu'].index(options.get())
    om1['menu'].delete(r_index)
    options.set(om1['menu'].entrycget(0,"label")) # select the first one 
    
my_w.mainloop()

""""
class App():
    def __init__(self, parent):
        self.parent = parent
        self.options = ['one', 'two', 'three']

        self.om_variable = tk.StringVar(self.parent)
        self.om_variable.set(self.options[0])
        self.om_variable.trace('w', self.option_select)

        self.om = tk.OptionMenu(self.parent, self.om_variable, *self.options)
        self.om.grid(column=0, row=0)

        self.label = tk.Label(self.parent, text='Enter new option')
        self.entry = tk.Entry(self.parent)
        self.button = tk.Button(self.parent, text='Add option to list', command=self.add_option)

        self.label.grid(column=1, row=0)
        self.entry.grid(column=1, row=1)
        self.button.grid(column=1, row=2)

        #self.update_button = tk.Button(self.parent, text='Update option menu', command=self.update_option_menu)
        #self.update_button.grid(column=0, row=2)

     def update_option_menu(self):
            menu = self.om["menu"]
            menu.delete(0, "end")
            for string in self.options:
                menu.add_command(label=string, 
                                command=lambda value=string: self.om_variable.set(value))

    def add_option(self):
         self.options.append(self.entry.get())
         self.entry.delete(0, 'end')
         print (self.options)
         menu = self.om["menu"]
         menu.delete(-1)
         for string in self.options:
            menu.add_command(label=string, 
                             command=lambda value=string: self.om_variable.set(value))

    def option_select(self, *args):
        print (self.om_variable.get())


root = tk.Tk()
App(root)
root.mainloop()"""
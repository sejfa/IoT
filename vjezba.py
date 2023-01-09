import tkinter as tk

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        """A text widget that supports a <<TextChanged>> event"""
        tk.Text.__init__(self, *args, **kwargs)

        self.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # if the contents changed, generate an event we can bind to
                if {([lindex $args 0] in {insert replace delete})} {
                    event generate $widget <<TextModified>> -when tail
                }
                # return the result from the real widget command
                return $result
            }

        ''')

        # this replaces the underlying widget with the proxy
        self.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(self)))

def update_char_count(event):
    count = event.widget.count("1.0", "end-1c")
    # count is a tuple; the character count is the first element
    count = 0 if not count else count[0]
    label.configure(text=f"Characters: {count}")

root = tk.Tk()
text = CustomText(root)
label = tk.Label(root, anchor="w")
label.pack(side="bottom", fill="x")
text.pack(fill="both", expand=True)

text.bind("<<TextModified>>", update_char_count)
root.mainloop()
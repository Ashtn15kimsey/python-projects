# Author:   Ash Kimsey
#
# Purpose:  Phonebook Demo, Demonstration OOP, Tkinter, GUI module,
#           using Tkinter parent and Child relationship
#
# Testted OS:          This code was written and tested to work with windows 10.


from tkinter import *
import tkinter as tk

# Be sure to import our other module
# so we can have access to them
import phonebook_gui
import phonebook_func

# Frame is Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame* __init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minimize(500,300)#(Height, Width)
        self.master.maximize(500,300)
        # This CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#0F0F0F0")
        # This protcool method is tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on window os.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_function.ask_quit(self))
        arg = self.master

        # load in GUI widget from a seprate module,
        # keep your code comprementilized and clutter free
        phonebook_gui.load_gui(self)



        if __name__ == "__main__":
            root = tk.Tk()
            App = ParentWindow(root)
            root.mainloop()

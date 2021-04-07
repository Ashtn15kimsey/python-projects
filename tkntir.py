import tkinter
from tkinter import*

class parentwindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.ireversable(width=False, height=False)
        self.master.geomtry('{}x{}'.format(700, 400)
        self.master.title('Learning Tkinter!')
        






if __name__ "__main__":
    root = Tk()
    App = parentwidow(root)
    root.mainloop()
                      
                            

                            
    


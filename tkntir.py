import tkinter
from tkinter import*

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg= '#000')


        self.varffname = StringVar()
        self.varflname = StringVar()
        self.varFname.set('Ash')
        self.varfLname.set('kimsey')

        print(self.varfname.get())
        print(self.varlname.get())
        
            
        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
                      
                            

                            
    


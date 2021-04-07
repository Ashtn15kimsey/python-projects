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

        self.varFName = StringVar()
        self.varLName = StringVar()
        

        self.lblFName = Label(self.master, text='First Name: ', font=("Melvetica", 16), fg='black', bg='lightblue')
        self.lblFName.grid(row=0, column=0, padx=(10,0), pady=(30,0)

        self.lblLname = Label(self.master, text='Last Name: ', font=("Melvetica", 16), fg='black', bg='lightblue')
        self.lblLName.grid(row=1, column=0, padx=()30,0), pady=(30,0)

        self.txtLname = Entry(self.master, text=self.varFLame, font=("Melvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=0, column=1, padx=(30,0), pady=(30,0)                   

        self.txtLname = Entry(self.master, text=self.varFLame, font=("Melvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,  padx=(30,0), pady=(30,0)

        self.btnSubmit = Button(self.master, text="Submit")
        self.btnSubmit.grid()row=2, column=1,padx=(0,0), pady=(30,0, sticky=NE)

        self.btnCancel = Button(self.master, text="Submit")
        self.btnCancel.grid()row=2, column=1,padx=(0,0), pady=(30,0, sticky=NE) 


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
                      
                            

                            
    


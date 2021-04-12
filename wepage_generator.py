from tkinter import *
import webpage_GUI
import webbrowser



def userInput(self):
    userInput =  self.txt_body.get()

   
    with open("webPage_generator.html", "w") as file1:
        file1.write("""<html> 
                 <body> 
                    <h1>
                    """
                       + userInput +   
                    """</h1>
                 </body> 
            </html>""")
    
    # Reading from file
    with open("webPage_generator.html", "r+") as file1:
        print(file1.read())

    webbrowser.open_new_tab("webPage_generator.html")


if __name__ == "__main__":
    pass

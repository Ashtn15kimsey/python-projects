from tkinter import *
import webpage_GUI
import webbrowser



def UserInput(self):
    userInput =  self.txt_body.get()

    # Writing to file 
    with open("webPage_generator.html", "a") as file:
        f.write("""<html> 
                 <body> 
                    <h1>
                          Stay tuned for our amazing summer sale! 
                    </h1>
                 </body> 
            </html>""")
        f.write(userInput)
    # Reading from file
    with open("webPage_generator.html", "r+") as f:
        print(f.read())


if __name__ == "__main__":
    pass


from tkinter import *

root = Tk()

def myClick():
    # Creates a button
    myButton = root.Button(root, text="Sign in", command=myClick)
    myButton.pack()

     #Creates a label widget
    myLabel = Label(root, text="My Calendar")
    nxLabel = Label(root, text="Please Sign in")
    myLabel.pack()
    nxLabel.pack()
root.mainloop()
if __name__ == "__main__":
    print("Helo test")
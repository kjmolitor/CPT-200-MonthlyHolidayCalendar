# PythonTutorial "https://www.pythontutorial.net/tkinter/"
# Python Tkinter GUI "https://www.youtube.com/watch?v=TuLxsvK4svQ&t=1379s"

from tkinter import *
import os

# Variables
window_width = 250
window_height = 280

# On-click events
def loginClick():
    window.destroy()
    exec(open("quickstart.py").read())

def helpClick():
    exec(open("README.md").read())

# Window Properties
window = Tk()
window.title("Personal Calendar") # Window title
window.config(background="#b8ffea") # Background color

# Sets the window to appear in the center of the users screen
# - Gets users screen dimensions
# - Finds center point of screen
# - Sets window position to center of screen and disables resizing
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

# Changes window icon
icon = PhotoImage(file='Icon.png')
window.iconphoto(True,icon)

# Widget properties
mainLogo = PhotoImage(file='Logo.png')
logo = Label(window, image = mainLogo, borderwidth = 0)
logo.pack()

# Login button
loginButton = Button(window,
                     text = "Open",
                     font = ("Poppins bold", 12),
                     fg = "#1e3940",
                     bg = "#b8ffea",
                     activeforeground = "#1e3940",
                     activebackground = "#b8ffea",
                     command = loginClick)
loginButton.place(x = 100, y = 170)

# Help button
helpButton = Button(window,
                     text = "Help",
                     font = ("Poppins bold", 12),
                     fg = "#1e3940",
                     bg = "#b8ffea",
                     activeforeground = "#1e3940",
                     activebackground = "#b8ffea",
                    command = helpClick)
helpButton.place(x = 103, y = 210)

window.mainloop()
# PythonTutorial "https://www.pythontutorial.net/tkinter/"
# Python Tkinter GUI "https://www.youtube.com/watch?v=TuLxsvK4svQ&t=1379s"

from tkinter import *

import google.oauth2.credentials
import google_auth_oauthlib.flow


# Variables
window_width = 250
window_height = 280

# API Credentials to verify the use of the app

# Uses the credentials.json file to identify the app
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar'])
# Indicates where the API server will redirect the user after completing authorization flow
flow.redirect_uri = 'https://www.example.com/oauth2callback'
# Generate URL for request to Google's OAuth 2.0 server.
# Use kwargs to set optional request parameters.
authorization_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')


# On-click events
def loginClick():
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
                     text = "Login",
                     font = ("Berlin Sans FB", 12),
                     fg = "#1e3940",
                     bg = "#b8ffea",
                     activeforeground = "#1e3940",
                     activebackground = "#b8ffea",
                     command = loginClick)
loginButton.place(x = 100, y = 170)

# Help button
helpButton = Button(window,
                     text = "Help",
                     font = ("Berlin Sans FB", 12),
                     fg = "#1e3940",
                     bg = "#b8ffea",
                     activeforeground = "#1e3940",
                     activebackground = "#b8ffea",
                    command = helpClick)
helpButton.place(x = 103, y = 210)

window.mainloop()
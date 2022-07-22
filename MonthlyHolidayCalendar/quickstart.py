#code sourced from  Python Quickstart Step 2: Configure the sample https://developers.google.com/calendar/api/quickstart/python
#modules?
from __future__ import print_function

import datetime
import os.path
import tkinter as tk
from tkinter import *

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Events import list_AllEvents

root= tk.Tk()

#General app formatting
root.geometry("900x900")
root.title("Monthly Events calendar")
root.config(bg="white")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

tasks_frame = tk.Frame(master=root,
            relief=tk.RIDGE,
            borderwidth=1,
            background="#b8ffea")

label_frame = tk.Frame(master=tasks_frame, relief=SUNKEN, borderwidth=1, width=50, height=50, bg="white")



def button_clicked():
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    def main():

        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=8000)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                  maxResults=10, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            calendar = service.calendars().get(calendarId='primary').execute()

            print(calendar['summary'])

        except HttpError as error:
            print('An error occurred: %s' % error)



    if __name__ == '__main__':
        main()








cal_frame = Frame(root, height=50, width=100, background="white")





events_label = Button(master=label_frame, text="Events",font=("Times New Roman", 12), command=list_AllEvents)

month_label = Label(master=cal_frame, text="Month", font=("Times New Roman", 12))

#Temp solution to pull up the calendar when the {button__clicked} method is called
cal_button = Button(master=cal_frame, text="Open calendar", font=("Times New Roman", 12) , command=button_clicked)



month_up = Button(master=cal_frame, text="▶")
month_down = Button(master=cal_frame, text="◀")


cal_frame.grid(row=0, column=1,sticky="nsew")
tasks_frame.grid(row=0, column=0,sticky="ns")
label_frame.grid(row=0, column=0,sticky="ew", padx=20, pady=20)
events_label.grid(row=0, column=0)

cal_button.place(x=300, y=300)
month_up.place(x=200, y=0)
month_down.place(x=125,y=0)
month_label.place(x=150, y=0)






root.mainloop()

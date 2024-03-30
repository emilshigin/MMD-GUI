import tkinter as tk
import tkinter.ttk as ttk

def content(self,window,content_frame):
    self.window = window

    #Settings Layout Setup
    settings_frame = tk.Frame(content_frame,bd=2,relief="solid",)
    
    settings_frame.grid_rowconfigure(0,weight=1)
    settings_frame.grid_columnconfigure(0, weight=1)

    settings_frame.grid(column= 0, row= 0, sticky="news")

    settings_label = tk.Label(settings_frame,text="Settings Page",font=("Arial",25))
    settings_label.grid(row=0, column=0, sticky="new")

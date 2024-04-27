import tkinter as tk
import tkinter.ttk as ttk
import os
import json


def startup_submition(startup):
    print(startup)
    # Check if this is the current strart up
    # Update start up

def option_start_up(self,settings_frame):
     # startup Option
    startup_option_frame = tk.Frame(settings_frame,bd=2,relief="solid")
    startup_option_frame.grid(row=1, column=0, sticky= "new")
    startup_option_frame.grid_rowconfigure(1,weight=1)
    startup_option_frame.grid_columnconfigure(1, weight=1)

    startup_label = tk.Label(startup_option_frame,text="Startup Page")
    startup_label.grid(row=1, column=0, sticky="new")

    config_data = json.load(open(file="config.json"))

    # menu value
    option_list = {}
    basepath = 'ContentFrames/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file() and ".py" in entry.name :
                option_list[entry.name.replace("_content.py","").lower().capitalize()] = entry.name.replace(".py","")

    value_menu = tk.StringVar(self.window)
    ttk.Style()
    current_start_up = config_data["start_page"].replace("_content","").lower().capitalize()
    startup_select = ttk.OptionMenu(startup_option_frame, value_menu,current_start_up, *option_list)
    startup_select.grid(row=1, column=1, sticky="nws")

    # Submit
    startup_submit_button = tk.Button(startup_option_frame,text="SUBMIT", command=lambda:startup_submition(option_list[value_menu.get()]))
    startup_submit_button.config(relief='groove', font=(0,10),foreground="white",background="#3292e0")
    startup_submit_button.grid(row=1,column=2, sticky="nse",padx=15)

def content(self,window,content_frame):
    self.window = window
    
    #Settings Layout Setup
    settings_frame = tk.Frame(content_frame,bd=2,relief="solid")
    settings_frame.grid(column= 0, row= 0, sticky="news")
    settings_frame.grid_rowconfigure(1,weight=1)
    settings_frame.grid_columnconfigure(0, weight=1)

    #Top lable
    settings_label_frame = tk.Frame(settings_frame,bd=2,relief="solid")
    settings_label_frame.grid(row=0, column=0, sticky= "ns")
    settings_label = tk.Label(settings_label_frame,text="Settings Page:",font=("Arial",25))
    settings_label.grid(row=0, column=0)

    option_start_up(self,settings_frame)  
    


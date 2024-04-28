import tkinter.ttk as ttk
import tkinter as tk
from tkinter import filedialog

import os
import json

    
def startup_submition(startup,button):
    with open('startup_config.json', 'r') as file:
        data = json.load(file)
        data["start_page"] = startup
        newData = json.dumps(data, indent=4)

    with open('startup_config.json', 'w') as file:
        file.write(newData)
    
    button.configure(text="Submited",bg="green")
    return button.after(1000, lambda: button.configure(text="Submit",bg="#3292e0"))



    # Check if this is the current strart up
    # Update start up

def option_start_up(self,settings_frame):
    font_size = 1
     # startup Option
    startup_option_frame = tk.Frame(settings_frame,bd=2,relief="solid")
    startup_option_frame.grid(row=1, column=0, sticky= "new")
    startup_option_frame.grid_rowconfigure(1,weight=1)
    startup_option_frame.grid_columnconfigure(1, weight=1)

    startup_label = tk.Label(startup_option_frame,text="Startup Page:",font=font_size,pady=5)
    startup_label.grid(row=1, column=0, sticky="new")

    config_data = json.load(open(file="startup_config.json"))

    # menu value
    option_list = {}
    basepath = 'ContentFrames/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file() and ".py" in entry.name :
                option_list[entry.name.replace("_content.py","").lower().capitalize()] = entry.name.replace(".py","")

    value_menu = tk.StringVar(self.window)
    current_start_up = config_data["start_page"].replace("_content","").lower().capitalize()
    startup_select = ttk.OptionMenu(startup_option_frame, value_menu,current_start_up, *option_list)
    
    #Stylize dropdown
    startup_select["menu"].configure(font=font_size)
    ttk.Style().configure("TMenubutton",font=font_size)
    # Place Dropdown
    startup_select.grid(row=1, column=1, sticky="nws")

    # Submit Button
    startup_submit_button = tk.Button(startup_option_frame,text="Submit", command=lambda:startup_submition(option_list[value_menu.get()],startup_submit_button))
    startup_submit_button.config(relief='groove', font=font_size,foreground="white",background="#3292e0")
    startup_submit_button.grid(row=1,column=2, sticky="ne",padx=15)

# NoteBook

# Step 1: make copy of APK and File
# Step 2: Get a history of the Files
# Step 3: Select Current Apk  
def notebook_neo_3(frame):
    frame.grid(row=0, column=0, sticky="news")
    frame.grid_rowconfigure(1,weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # VF
    select_vf_label = tk.Label(frame, text="Selected VF APK:")
    select_vf_label.grid(row=0, column=0, sticky="news")

    # Button to telect file
    open_button = tk.Button(frame, text="Open File", command=lambda: filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
)    
    open_button.grid(row=0, column=1, sticky="news")


def notebook_G3(frame):
    frame.grid(row=0, column=0, sticky="news")
    frame.grid_rowconfigure(1,weight=1)
    frame.grid_columnconfigure(0, weight=1)


def notebook_frame(self,settings_frame):
    # Place Notebook
    notebook_frame = tk.Frame(settings_frame,pady=5)
    notebook_frame.grid(row=2, column=0, sticky= "new")
    notebook_frame.grid_rowconfigure(1,weight=1)
    notebook_frame.grid_columnconfigure(0, weight=1)
    
    # Add Label 
    startup_label = tk.Label(notebook_frame,text="APK Upload", font=(10))
    startup_label.grid(row=0, column=0, sticky="nw")

    #Notebook Setup
    notebook = ttk.Notebook(notebook_frame,height=225)
    notebook.enable_traversal()
    notebook.grid(row=2,column=0,sticky="new")
    
    # Create pages in Notebook
    neo_3_notebook_frame = ttk.Frame(notebook)
    g3_notebook_frame = ttk.Frame(notebook)
    
        # Place Content in Page   
    notebook_neo_3(neo_3_notebook_frame)
    notebook_G3(g3_notebook_frame)

    # Call the pages
    notebook.add(neo_3_notebook_frame, text = "Neo 3")
    notebook.add(g3_notebook_frame, text = "G3")
    


def content(self,window,content_frame):
    self.window = window
    
    #Settings Layout Setup
    settings_frame = tk.Frame(content_frame,bd=1,relief="solid")
    settings_frame.grid(column= 0, row= 0, sticky="news")
    settings_frame.grid_rowconfigure(2,weight=1)
    settings_frame.grid_columnconfigure(0, weight=1)

    #Top lable
    settings_label_frame = tk.Frame(settings_frame)
    settings_label_frame.grid(row=0, column=0, sticky= "ns")
    settings_label = tk.Label(settings_label_frame,text="Settings Page:",font=("Arial",25))
    settings_label.grid(row=0, column=0)

    option_start_up(self,settings_frame)  
    notebook_frame(self,settings_frame)
    


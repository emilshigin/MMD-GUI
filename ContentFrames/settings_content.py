import sys
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import filedialog

import shutil
import os
import json

def resource_path(*paths):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, *paths)


THIS_FILE_DIR = resource_path("ContentFrames")
ROOT_DIR =  resource_path()
CONFIG_PATH = resource_path('config.json')

print(THIS_FILE_DIR,ROOT_DIR,CONFIG_PATH)

with open(CONFIG_PATH, 'r') as f:
    BACKUP_CONFIG_DATA = json.load(f)


# Save Startup Selection
def startup_submition(startup,button):
    with open(CONFIG_PATH, 'r') as file:
        data = json.load(file)
        data["start_page"] = startup
        newData = json.dumps(data, indent=4)

    with open(CONFIG_PATH, 'w') as file:
        file.write(newData)
    
    button.configure(text="Submited",bg="#F27405")
    return button.after(800, lambda: button.configure(text="Submit",bg="#3292e0"))

# Startup Selection
# Step 1: Check start up  options
# Step 2: Update start up
def option_start_up(self,settings_frame):
    font_size = 1
     # startup Option
    startup_option_frame = tk.Frame(settings_frame,pady=10)
    startup_option_frame.grid(row=1, column=0, sticky= "new")
    startup_option_frame.grid_rowconfigure(1,weight=1)
    startup_option_frame.grid_columnconfigure(1, weight=1)

    startup_label = tk.Label(startup_option_frame,text="Startup Page:",font=font_size,pady=5)
    startup_label.grid(row=1, column=0, sticky="new")

    config_data = json.load(open(file=CONFIG_PATH))

    # menu value
    option_list = {}
    basepath=resource_path('ContentFrames')
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

################################################################
#                                                              #
#                         NoteBook                             #
#                                                              #
################################################################

# Step 1: Open Folder and select file 
# Step 2: Make copy of File if not in local dir
# Step :  Save the current APK to Use as defualt
# Step 3: Give Visual Feadback that option was saved 
# [[Error]] Thrown when closing filedialog.askopenfilename
def file_upload(button: tk.Button,Label: tk.Label ,Backup_Folder_Name, Upload_Type,Prefix = None ):
    #  Get File Loction
    backup_file_location = resource_path("Backup",Backup_Folder_Name)
    file_location = filedialog.askopenfilename(
        title=f"Select {Upload_Type} For {Backup_Folder_Name}",
        initialdir=backup_file_location ,
        filetypes=[("Andriod APK", "*.apk"), ("All files", "*.*")]
        )
    if not file_location:
        return  # Cancelled

    file_name = os.path.basename(file_location)
    
    target_path = resource_path(backup_file_location, file_name)
    print('Copy new file: ',file_location,target_path)
    # Only copy if it's not already the same file
    if not os.path.exists(target_path) or not os.path.samefile(file_location,target_path):
        os.makedirs(backup_file_location, exist_ok=True)
        shutil.copy2(file_location, target_path)
        file_location = target_path
    else:
        file_location = target_path  # Already where it should be
    
    print("File Location of APK: ", file_location)

    # Convert to relative path
    relative_path = os.path.relpath(file_location, THIS_FILE_DIR)[3:]
    relative_path = relative_path.replace("\\", "/")

    with open(CONFIG_PATH, 'r') as file:
        data = json.load(file)
        data[Backup_Folder_Name][Upload_Type]['Path'] = relative_path
        newData = json.dumps(data, indent=4)

    with open(CONFIG_PATH, 'w') as file:
        file.write(newData)

    # Update Label
    Label.config(text='...'+relative_path[-35:])

    # Visual Feed Back Turn button Orange
    button.configure(text="Submited",bg="#F27405")
    return button.after(400, lambda: button.configure(text="Open File",bg="#3292e0"))

# Content On each Tab 
def row_bg(count: int):
    return 'white' if count %2 else "#f0f0f0"

def notebook_content(frame: ttk.Frame,device_name: str):
    # Read Json File
    data = json.load(open(file=CONFIG_PATH))
    device_upload_list = list(data[device_name].keys())
    
    # Set up frame
    frame.grid(row=0, column=0, sticky="news")

    # grid_rowconfigure will cause the rows to not be in order
    frame.grid_columnconfigure(0, weight=1)

    # Generate Each Row
    row = []

    # Item in each rowm
    item_name = []
    path_name = []
    button_submit = []
    
    for count, item in enumerate(device_upload_list):
        # Create Row
        row.append(tk.Frame(frame,pady=10,background=row_bg(count)))
        row[count].grid(row=count, column=0, sticky="new")
        row[count].grid_rowconfigure(0,weight=1)
        row[count].grid_columnconfigure(0, weight=1)

        # Name of Catagory
        item_name.append(tk.Label(row[count], text=item,background=row_bg(count)))
        item_name[count].grid(row=count, column=0, sticky="nws")

        # File Path 
        filepath = str(data[device_name][item]['Path'])[-35:]
        path_name.append(tk.Label(row[count], text="..."+filepath,background=row_bg(count)))
        path_name[count].grid(row=count, column=1, padx= 15, sticky="nes")

        # Button
        button_submit.append(tk.Button(row[count],text="Open File", command=lambda i = count, item = item: file_upload(button = button_submit[i],Label = path_name[i],Prefix ="Current" ,Backup_Folder_Name = device_name,Upload_Type= item)))    
        button_submit[count].config(relief='groove',foreground="white",background="#3292e0")
        button_submit[count].grid(row=count, column=2,padx=10, sticky="nes")            

# Templet tab:


def templet_content(frame: ttk.Frame):
    data = json.load(open(file=CONFIG_PATH))
    # Set up frame
    frame.grid_columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="news")

    # Create Rows
    row = []
    count = 0
    
    # Message
    row.append(tk.Frame(frame,pady=10,background=row_bg(count),bd=2,relief="solid"))
    row[count].grid(row=count, column=0, sticky="new")
    row[count].grid_columnconfigure(0, weight=1)
    row[count].grid_columnconfigure(1, weight=1)
    row[count].grid_columnconfigure(2, weight=1)
    row[count].grid_columnconfigure(3, weight=1)

    device_name_label = tk.Label(row[count], text="Feture Work In Progress",background=row_bg(count))
    device_name_label.grid(row=count, column=0, sticky="nws",padx=10)

    # row 0 what the name of device
     # Name of Catagory
    count += 1
    row.append(tk.Frame(frame,pady=10,background=row_bg(count),bd=2,relief="solid"))
    row[count].grid(row=count, column=0, sticky="new")
    row[count].grid_rowconfigure(0,weight=1)
    row[count].grid_columnconfigure(0, weight=1)
    row[count].grid_columnconfigure(1, weight=1)
    row[count].grid_columnconfigure(2, weight=1)
    row[count].grid_columnconfigure(3, weight=1)

    device_name_label = tk.Label(row[count], text="Device Name",background=row_bg(count))
    device_name_label.grid(row=count, column=0, sticky="nws",padx=10)

    device_name_input = tk.Entry(row[count],background=row_bg(count))
    device_name_input.grid(row=count, column=1, columnspan=2, sticky="news",padx=10)
    

    # row 1 [row text] do you want to [push,install] a file
    count += 1
    row.append(tk.Frame(frame,pady=10,background=row_bg(count),bd=2,relief="solid"))
    row[count].grid(row=count, column=0, sticky="new")
    row[count].grid_columnconfigure(0, weight=1)
    row[count].grid_columnconfigure(1, weight=1)
    row[count].grid_columnconfigure(2, weight=1)
    row[count].grid_columnconfigure(3, weight=1)


    file_name_label = tk.Label(row[count], text="File Name",background=row_bg(count))
    file_name_label.grid(row=count, column=0, sticky="nws",padx=10)

    file_name_input = tk.Entry(row[count],background=row_bg(count))
    file_name_input.grid(row=count, column=1,columnspan=2, sticky="news",padx=10)

    option_list = ["none","install","push"]
    value_menu = tk.StringVar(frame)
    value_menu.set("Type of File")
    select_file_type = ttk.OptionMenu(frame,value_menu,option_list[0],*option_list)
    select_file_type.grid(row=count, column=2, sticky="news",padx=10)


    # row 2 do you want to Submit or add another row
    count += 1
    row.append(tk.Frame(frame,pady=10,background=row_bg(count),bd=2,relief="solid"))
    row[count].grid(row=count, column=0, sticky="new")
    row[count].grid_columnconfigure(0, weight=1)
    row[count].grid_columnconfigure(1, weight=1)
    row[count].grid_columnconfigure(2, weight=1)
    row[count].grid_columnconfigure(3, weight=1)

    button_add_row = tk.Button(frame,text="Add Row",)
    button_add_row.config(relief='groove',foreground="white",background="#3292e0")
    button_add_row.grid(row=count,column=0, sticky="news",padx=15)
    
    button_submit = tk.Button(frame,text="Submit")
    button_submit.config(relief='groove',foreground="white",background="#3292e0")
    button_submit.grid(row=count,column=1, sticky="news",padx=15)
    

# Frame that hold the Notebook  
def notebook_frame(self,settings_frame):
    # Place Notebook
    notebook_frame = tk.Frame(settings_frame,pady=5)
    notebook_frame.grid(row=2, column=0, sticky= "new")
    notebook_frame.grid_rowconfigure(0,weight=1)
    notebook_frame.grid_columnconfigure(0, weight=1)
    
    # Add Label 
    startup_label = tk.Label(notebook_frame,text="APK Upload", font=(10))
    startup_label.grid(row=0, column=0, sticky="nw")

    #Notebook Setup
    notebook = ttk.Notebook(notebook_frame)
    notebook.enable_traversal()
    notebook.grid(row=2,column=0,sticky="news")
    
    # [Todo] Make a function to  loop this and dynamicly add more frames
    # Create pages in Notebook
    neo_3_notebook_frame = ttk.Frame(notebook)
    g3_notebook_frame = ttk.Frame(notebook)
    neo_2_notebook_frame = ttk.Frame(notebook)
    g2_notebook_frame = ttk.Frame(notebook)

    # Place Content in Page   
    notebook_content(neo_3_notebook_frame,"Pico Neo 3 Pro Eye")
    notebook_content(g3_notebook_frame,"PICO G3")
    notebook_content(neo_2_notebook_frame,"Pico Neo 2 Eye")
    notebook_content(g2_notebook_frame,"G2 4K")

    # Call the pages
    notebook.add(neo_3_notebook_frame, text = "Neo 3")
    notebook.add(g3_notebook_frame, text = "G3")
    notebook.add(neo_2_notebook_frame, text = "Neo 2")
    notebook.add(g2_notebook_frame, text = "G2")

    # Add the templet maker
    templet_notebook_frame = ttk.Frame(notebook)
    templet_content(templet_notebook_frame)
    notebook.add(templet_notebook_frame, text = "+")

    
# Layout for setting page
def content(self,window,content_frame):
    self.window = window

    # Settings Layout Setup
    settings_frame = tk.Frame(content_frame,bd=1,relief="solid")
    settings_frame.grid(column= 0, row= 0, sticky="news")
    settings_frame.grid_rowconfigure(2,weight=1)
    settings_frame.grid_columnconfigure(0, weight=1)
    
    # Top lable
    settings_label_frame = tk.Frame(settings_frame)
    settings_label_frame.grid(row=0, column=0, sticky= "ns")
    settings_label = tk.Label(settings_label_frame,text="Settings Page",font=("Arial",25))
    settings_label.grid(row=0, column=0)

    # Render Layout 
    option_start_up(self,settings_frame)  
    notebook_frame(self,settings_frame)
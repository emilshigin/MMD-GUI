import tkinter.ttk as ttk
import tkinter as tk
from tkinter import filedialog

import shutil
import os
import json

THIS_FILE_DIR = os.path.dirname( os.path.dirname(__file__)).replace("\\","/")
CONFIG_PATH = (THIS_FILE_DIR+'/config.json')
BACKUP_CONFIG_DATA = json.load(open(file=CONFIG_PATH))

def startup_submition(startup,button):
    with open(CONFIG_PATH, 'r') as file:
        data = json.load(file)
        data["start_page"] = startup
        newData = json.dumps(data, indent=4)

    with open(CONFIG_PATH, 'w') as file:
        file.write(newData)
    
    button.configure(text="Submited",bg="#F27405")
    return button.after(800, lambda: button.configure(text="Submit",bg="#3292e0"))



    # Check if this is the current strart up
    # Update start up

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
    basepath = THIS_FILE_DIR+'/ContentFrames/'
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

# Step 1: Open Folder and select file 
# Step 2: Make copy of File if not in local dir
# Step :  Save the current APK to Use as defualt
# Step 3: Give Visual Feadback that option was saved 
def file_upload(button: tk.Button,Label: tk.Label ,Backup_Folder_Name, Upload_Type,Prefix = None ):
    #  Get File Loction
    initialdir_str = THIS_FILE_DIR+'/Backup'
    file_location = filedialog.askopenfilename(title=f"Select {Upload_Type} For {Backup_Folder_Name}",initialdir=initialdir_str ,filetypes=[("Andriod APK", "*.apk"), ("All files", "*.*")])
    file_name = file_location.split("/")[-1]
    print("Current path:",THIS_FILE_DIR)
    backup_file_location = THIS_FILE_DIR+'/Backup'
    
    # Write Current File 
    if backup_file_location.upper() not in file_location.upper():
        print("Not In backup:",file_location)
        backup_file_location = backup_file_location+"/"+Backup_Folder_Name
        print(f"Make copy in {backup_file_location} folder")
        shutil.copy2(file_location,backup_file_location)
        file_location = backup_file_location+"/"+file_name
    
    print("File Location of APK: ", file_location)
    with open(CONFIG_PATH, 'r') as file:
        data = json.load(file)
        data[Backup_Folder_Name][Prefix+" "+ Upload_Type] = file_location
        newData = json.dumps(data, indent=4)

    with open(CONFIG_PATH, 'w') as file:
        file.write(newData)

    # Update Label
    Label.config(text='...'+file_location[-35:])

    # Visual Feed Back Turn button Orange
    button.configure(text="Submited",bg="#F27405")
    return button.after(400, lambda: button.configure(text="Open File",bg="#3292e0"))

    
def notebook_neo_3(frame):
    frame.grid(row=0, column=0, sticky="news")
    frame.grid_rowconfigure(3,weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Row One
    frame_row_1 = tk.Frame(frame,pady=10,background='white',relief='ridge')
    frame_row_1.grid(row=0, column=0, sticky="news")
    frame_row_1.grid_rowconfigure(1,weight=1)
    frame_row_1.grid_columnconfigure(0, weight=1)

    # VF APK Label
    current_vf_label = tk.Label(frame_row_1, text="Current VF APK:",background='white')
    current_vf_label.grid(row=0, column=0, sticky="nws")

    # VF APK path
    current_vf_label = tk.Label(frame_row_1, text="..."+BACKUP_CONFIG_DATA["Pico Neo 3"]["Current VF APK"][-35:],background='white')
    current_vf_label.grid(row=0, column=1, padx= 15, sticky="nes")

    # Button to telect file
    open_button_vf = tk.Button(frame_row_1, text="Open File", command=lambda:file_upload(open_button_vf,current_vf_label,Prefix ="Current" ,Backup_Folder_Name = "Pico Neo 3",Upload_Type= "VF APK"))    
    open_button_vf.config(relief='groove',foreground="white",background="#3292e0")
    open_button_vf.grid(row=0, column=2,padx=10, sticky="nes")
    
    # Row Two
    frame_row_2 = tk.Frame(frame,pady=10,relief='ridge')
    frame_row_2.grid(row=1, column=0, sticky="news")
    frame_row_2.grid_rowconfigure(1,weight=1)
    frame_row_2.grid_columnconfigure(0, weight=1)

    # AM APK Label
    current_am_label = tk.Label(frame_row_2, text="Current App Manager APK:")
    current_am_label.grid(row=0, column=0, sticky="nws")

    # AM APK path
    current_am_label = tk.Label(frame_row_2, text="..."+BACKUP_CONFIG_DATA["Pico Neo 3"]["Current App Manager APK"][-35:])
    current_am_label.grid(row=0, column=1, padx= 15, sticky="nes")

    # Button to Select file
    open_button_am = tk.Button(frame_row_2, text="Open File", command=lambda:file_upload(open_button_am,current_am_label,Prefix ="Current" ,Backup_Folder_Name = "Pico Neo 3",Upload_Type= "App Manager APK"))    
    open_button_am.config(relief='groove',foreground="white",background="#3292e0")
    open_button_am.grid(row=0, column=2,padx=10, sticky="nes")

    # Row 3
    frame_row_3 = tk.Frame(frame,pady=10,background='white',relief='ridge')
    frame_row_3.grid(row=2, column=0, sticky="news")
    frame_row_3.grid_rowconfigure(1,weight=1)
    frame_row_3.grid_columnconfigure(0, weight=1)

    # PM APK Label
    current_pm_label = tk.Label(frame_row_3,background='white', text="Current PM APK:")
    current_pm_label.grid(row=0, column=0, sticky="nws")

    # PM APK path
    current_pm_label = tk.Label(frame_row_3,background='white', text="..."+BACKUP_CONFIG_DATA["Pico Neo 3"]["Current PM APK"][-35:])
    current_pm_label.grid(row=0, column=1, padx= 15, sticky="nes")

    # Button to Select file
    open_button_pm = tk.Button(frame_row_3, text="Open File", command=lambda:file_upload(open_button_pm,current_pm_label,Prefix ="Current" ,Backup_Folder_Name = "Pico Neo 3",Upload_Type= "PM APK"))    
    open_button_pm.config(relief='groove',foreground="white",background="#3292e0")
    open_button_pm.grid(row=0, column=2,padx=10, sticky="nes")

    # Row 4
    frame_row_4 = tk.Frame(frame,pady=10,relief='ridge')
    frame_row_4.grid(row=3, column=0, sticky="news")
    frame_row_4.grid_rowconfigure(1,weight=1)
    frame_row_4.grid_columnconfigure(0, weight=1)

    # DA Calib Label
    current_da_label = tk.Label(frame_row_4, text="Current DA Calib:")
    current_da_label.grid(row=0, column=0, sticky="nws")

    # DA Calib path
    current_da_label = tk.Label(frame_row_4, text="..."+BACKUP_CONFIG_DATA["Pico Neo 3"]["Current DA Calib"][-35:])
    current_da_label.grid(row=0, column=1, padx= 15, sticky="nes")

    # Button to Select file
    open_button_da = tk.Button(frame_row_4, text="Open File", command=lambda:file_upload(open_button_da,current_da_label,Prefix ="Current" ,Backup_Folder_Name = "Pico Neo 3",Upload_Type= "DA Calib"))    
    open_button_da.config(relief='groove',foreground="white",background="#3292e0")
    open_button_da.grid(row=0, column=2,padx=10, sticky="nes")

    




def notebook_G3(frame):
    frame.grid(row=0, column=0, sticky="news")
    frame.grid_rowconfigure(3,weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Row One
    frame_row_1 = tk.Frame(frame,pady=10,background='white',relief='ridge')
    frame_row_1.grid(row=0, column=0, sticky="news")
    frame_row_1.grid_rowconfigure(1,weight=1)
    frame_row_1.grid_columnconfigure(0, weight=1)

    # VF APK Label
    current_vf_label = tk.Label(frame_row_1, text="Current VF APK:",background='white')
    current_vf_label.grid(row=0, column=0, sticky="nws")

    # VF APK path
    current_vf_label = tk.Label(frame_row_1, text="..."+BACKUP_CONFIG_DATA["PICO G3"]["Current VF APK"][-35:],background='white')
    current_vf_label.grid(row=0, column=1, padx= 15, sticky="nes")

    # Button to telect file
    open_button_vf = tk.Button(frame_row_1, text="Open File", command=lambda:file_upload(open_button_vf,current_vf_label,Prefix ="Current" ,Backup_Folder_Name = "PICO G3",Upload_Type= "VF APK"))    
    open_button_vf.config(relief='groove',foreground="white",background="#3292e0")
    open_button_vf.grid(row=0, column=2,padx=10, sticky="nes")
    
    # Row Two
    frame_row_2 = tk.Frame(frame,pady=10,relief='ridge')
    frame_row_2.grid(row=1, column=0, sticky="news")
    frame_row_2.grid_rowconfigure(1,weight=1)
    frame_row_2.grid_columnconfigure(0, weight=1)

    # AM APK Label
    current_am_label = tk.Label(frame_row_2, text="Current App Manager APK:")
    current_am_label.grid(row=0, column=0, sticky="nws")

    # AM APK path
    current_am_label = tk.Label(frame_row_2, text="..."+BACKUP_CONFIG_DATA["PICO G3"]["Current App Manager APK"][-35:])
    current_am_label.grid(row=0, column=1, padx= 15, sticky="nes")

    # Button to Select file
    open_button_am = tk.Button(frame_row_2, text="Open File", command=lambda:file_upload(open_button_am,current_am_label,Prefix ="Current" ,Backup_Folder_Name = "PICO G3",Upload_Type= "App Manager APK"))    
    open_button_am.config(relief='groove',foreground="white",background="#3292e0")
    open_button_am.grid(row=0, column=2,padx=10, sticky="nes")


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
    


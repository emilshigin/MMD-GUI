import tkinter as tk
import tkinter.ttk as ttk

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


    # Settings Option
    settings_option_frame = tk.Frame(settings_frame,bd=2,relief="solid")
    settings_option_frame.grid(row=1, column=0, sticky= "new")
    settings_option_frame.grid_rowconfigure(1,weight=1)
    settings_option_frame.grid_columnconfigure(1, weight=1)

    # Lable - Option
    settings_label = tk.Label(settings_option_frame,text="Settings Page")
    settings_label.grid(row=1, column=0, sticky="new")
    
    option_list = ["1","2","3"]
    value_menu = tk.StringVar(window)
    # value_menu.set("Pick One")
    ttk.Style()
    settings_label = ttk.OptionMenu(settings_option_frame, value_menu,"defualt", *option_list)
    settings_label.grid(row=1, column=1, sticky="nws")
    


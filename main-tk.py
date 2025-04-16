import tkinter as tk
import json
import tkinter.ttk as ttk
import os
from ContentFrames import production_content
from ContentFrames import settings_content

# Change \\MMD-GUI if file name changes
THIS_FILE_DIR = os.path.dirname( os.path.dirname(__file__)).replace("\\","/")+'/MMD-GUI'


# credit: https://stackoverflow.com/questions/66858214/tkinter-side-bar
# Menu Frame Movement
def config_data() -> json:
     config_path = (THIS_FILE_DIR+'/config.json')
     data = json.load(open(file=config_path))
     return data

def enter_menu_frame() -> None:
    global menu_frame_curremt_width,menu_frame_expanded
    menu_frame_curremt_width += 10
    repeat = window.after(3,enter_menu_frame)
    menu_frame.config(width=menu_frame_curremt_width)
    if menu_frame_curremt_width >= menu_frame_max_width:
        menu_frame_expanded = True
        window.after_cancel(repeat)
        menu_frame_fill()

#   Minumize Side Menu  
def leave_menu_frame() -> None:
    global menu_frame_curremt_width,menu_frame_expanded
    menu_frame_curremt_width -= 10
    repeat = window.after(5,leave_menu_frame)
    menu_frame.config(width=menu_frame_curremt_width)
    if menu_frame_curremt_width <= menu_frame_min_width:
        menu_frame_expanded = False
        window.after_cancel(repeat)
        menu_frame_fill()

# Updates Side Menu bar 
def menu_frame_fill() -> None:
    global menu_frame_expanded,menu_frame_curremt_width
    if menu_frame_expanded:
        menu_production_button.config(text="🏭 Production",font=(0,16), command=lambda:content_handler("production_content"))
        menu_settings_button.config(text="⚙️ Settings",font=(0,16),command=lambda:content_handler("settings_content"))
    else:
        menu_production_button.config(text="🏭",font=(0,16))
        menu_settings_button.config(text="⚙️",font=(0,16))

# switch_to: string file name from ContentFrames Folder 
def content_handler(switch_to = None) -> exec:
        if switch_to is not None:
             return exec(switch_to+".content(window,window,content_frame)")
        print("\nNo valad string was given to function content_handler\nThe function was given",switch_to)
        
        
if __name__ == '__main__':
    config_data = config_data()

    # Window defualts
    window = tk.Tk()
    window.title('MMD Software')
    window.geometry('660x400')
    icon_path = os.path.join(THIS_FILE_DIR,'images','mmd_logo.png')
    window.iconphoto(False,tk.PhotoImage(file=icon_path))
    window.minsize(width=660, height=500)
    window.maxsize(width=800, height=500)
    window.update()

    # Frames defualts

    menu_frame_min_width = 60
    menu_frame_max_width = 150
    menu_frame_curremt_width = menu_frame_min_width
    menu_frame_expanded = False
    window_bottom_bar_hieght = 15

    # Sections on the window
    body_frame = tk.Frame(window, background = "blue", width = window.winfo_width() ,height=window.winfo_height()-window_bottom_bar_hieght)
    window_bottom_bar = tk.Frame(window,background="#99BFF2",height=window_bottom_bar_hieght) # Baby Blue
    content_frame = tk.Frame(body_frame,background="#F2EFDC", width=window.winfo_width() , height=window.winfo_height()-window_bottom_bar_hieght) # Bage
    menu_frame =  tk.Frame(body_frame, background = "#515759", width = menu_frame_min_width , height=window.winfo_height()-window_bottom_bar_hieght) # Dark Gray

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    body_frame.grid_rowconfigure(0,weight=1)
    body_frame.grid_columnconfigure(1, weight=1)

    content_frame.grid_rowconfigure(0,weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    body_frame.grid(column=0, row = 0 , sticky="news")
    window_bottom_bar.grid(column=0, row = 1 , sticky="ews")
    menu_frame.grid(column= 0, row = 0 ,sticky="news")
    content_frame.grid(column= 1, row = 0 ,sticky="news")

    # Update Content Frame
    content_handler(config_data["start_page"])


    # Menu Content
    menu_production_button = tk.Button(menu_frame, relief='flat',text="🏭",background="#515759",foreground='white',pady=5, font=(0,16))
    menu_settings_button = tk.Button(menu_frame,relief='flat',text="⚙️",background="#515759",foreground='white',pady=5, font=(0,16))

    menu_production_button.grid(column=0, row = 0 , sticky="new")
    menu_settings_button.grid(column=0, row = 1 , sticky="ews")

    menu_frame.bind('<Enter>', lambda e: enter_menu_frame())
    menu_frame.bind('<Leave>', lambda e: leave_menu_frame())
    menu_frame.grid_propagate(False)

    #run
    window.mainloop()

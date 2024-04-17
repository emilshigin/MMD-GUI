import tkinter as tk
import json
import tkinter.ttk as ttk
from ContentFrames import production_content
from ContentFrames import settings_content

# credit: https://stackoverflow.com/questions/66858214/tkinter-side-bar
# Menu Frame Movement
def config_data():
     data = json.load(open(file="config.json"))
     return data

def enter_menu_frame():
    global menu_frame_curremt_width,menu_frame_expanded
    menu_frame_curremt_width += 10
    repeat = window.after(3,enter_menu_frame)
    menu_frame.config(width=menu_frame_curremt_width)
    if menu_frame_curremt_width >= menu_frame_max_width:
        menu_frame_expanded = True
        window.after_cancel(repeat)
        menu_frame_fill()
 
def leave_menu_frame():
    global menu_frame_curremt_width,menu_frame_expanded
    menu_frame_curremt_width -= 10
    repeat = window.after(5,leave_menu_frame)
    menu_frame.config(width=menu_frame_curremt_width)
    if menu_frame_curremt_width <= menu_frame_min_width:
        menu_frame_expanded = False
        window.after_cancel(repeat)
        menu_frame_fill()

def menu_frame_fill():
    global menu_frame_expanded,menu_frame_curremt_width
    if menu_frame_expanded:
        menu_production_button.config(text="Production",font=(0,15), command=lambda:content_handler("production_content"))
        menu_settings_button.config(text="Settings",font=(0,15),command=lambda:content_handler("settings_content"))
    else:
        menu_production_button.config(text="Prod",font=(0,15))
        menu_settings_button.config(text="Set",font=(0,15))


def content_handler(switch_to = None):
        if switch_to is not None:
             return exec(switch_to+".content(window,window,content_frame)")
        print("\nNo valad string was given to function content_handler\nThe function was given",switch_to)
        
        

# TODO: device info needs to update if headset is unplaged and repluged or a new headset is plugged in Use the device scan button
# TODO: make better gui by reading pythonguis.com

if __name__ == '__main__':
    config_data = config_data()

    # Window defualts
    window = tk.Tk()
    window.title('layout')
    window.geometry('600x400')
    window.update()

    # Frames defualts
    menu_frame_min_width = 50
    menu_frame_max_width = 100
    menu_frame_curremt_width = menu_frame_min_width
    menu_frame_expanded = False
    window_bottom_bar_hieght = 15

    # Sections on the window
    body_frame = tk.Frame(window, background = "blue", width = window.winfo_width() ,height=window.winfo_height()-window_bottom_bar_hieght)
    window_bottom_bar = tk.Frame(window,background="green",height=window_bottom_bar_hieght)
    content_frame = tk.Frame(body_frame,background="gray", width=window.winfo_width() , height=window.winfo_height()-window_bottom_bar_hieght)
    menu_frame =  tk.Frame(body_frame, background = "red", width = menu_frame_min_width , height=window.winfo_height()-window_bottom_bar_hieght)

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
    # content_handler() # For Tests


    # Menu Content
    menu_production_button = tk.Button(menu_frame, relief='flat',text="Prod", font=(0,15))
    menu_settings_button = tk.Button(menu_frame,relief='flat',text="Sett", font=(0,15))

    menu_production_button.grid(column=0, row = 0 , sticky="new")
    menu_settings_button.grid(column=0, row = 1 , sticky="ews")

    menu_frame.bind('<Enter>', lambda e: enter_menu_frame())
    menu_frame.bind('<Leave>', lambda e: leave_menu_frame())
    menu_frame.grid_propagate(False)

    #run
    window.mainloop()

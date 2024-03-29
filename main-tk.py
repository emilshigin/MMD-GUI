import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
import adb_connection

# TODO: device info needs to update if headset is unplaged and repluged or a new headset is plugged in Use the device scan button
# TODO: make better gui by reading pythonguis.com
# TODO: Seperate the Production Conttent into individual file

device_info = adb_connection.get_device_info()
THIS_FILE_DIR = os.path.dirname(__file__)

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
content_frame.grid_columnconfigure(1, weight=1)


body_frame.grid(column=0, row = 0 , sticky="news")
window_bottom_bar.grid(column=0, row = 1 , sticky="ews")
menu_frame.grid(column= 0, row = 0 ,sticky="news")
content_frame.grid(column= 1, row = 0 ,sticky="news")

# Menu Content
menu_production_button = tk.Button(menu_frame, relief='flat',text="Prod", font=(0,15))
menu_settings_button = tk.Button(menu_frame,relief='flat',text="Sett", font=(0,15))

menu_production_button.grid(column=0, row = 0 , sticky="new")
menu_settings_button.grid(column=0, row = 1 , sticky="ews")


# credit: https://stackoverflow.com/questions/66858214/tkinter-side-bar
# Menu Frame Movement
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
        menu_production_button.config(text="Production",font=(0,15))
        menu_settings_button.config(text="Settings",font=(0,15))
    else:
        menu_production_button.config(text="Prod",font=(0,15))
        menu_settings_button.config(text="Set",font=(0,15))


menu_frame.bind('<Enter>', lambda e: enter_menu_frame())
menu_frame.bind('<Leave>', lambda e: leave_menu_frame())

menu_frame.grid_propagate(False)

#######################################################
# Production Content

# Copy the text to the clipboard
def copy_address(item):
    window.clipboard_clear()
    window.clipboard_append(item.cget("text"))
    window.update()  # Required on macOS

#Production Layout Setup
production_frame = tk.Frame(content_frame,bd=2,relief="solid")

production_frame.grid_rowconfigure(0,weight=1)
production_frame.grid_columnconfigure(1, weight=1)

production_frame.grid(column= 0, row= 0, sticky="news")
production_frame.grid(column= 1, row= 0, sticky="news")

left_production_frame = ttk.Frame(production_frame, padding = (5,5,10,0))
left_production_frame.grid(column=0,row=0,sticky="news")

right_production_frame = ttk.Frame(production_frame, padding = (5,5,10,0), borderwidth=4, )
right_production_frame.grid(column=1,row=0,sticky="news")

# Left Column
# Device Image
Neo_3_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FILE_DIR,"images\\Neo_3.jpeg")).resize((200,180)))
Neo_3_image_label = tk.Label(left_production_frame,image=Neo_3_image, bd=2, relief="solid")
Neo_3_image_label.grid(column=0,row=0,sticky="news")

#Mac Address
mac_address_frame = ttk.Frame(left_production_frame,padding=(3,3,12,12))
mac_address = tk.Label(mac_address_frame, text="Mac Address:")
mac_address_responce = tk.Button(mac_address_frame, text=device_info['MAC Address'],relief="flat",command=lambda:copy_address(mac_address_responce))

mac_address_frame.grid(column=0,row=1,sticky="news")
mac_address.grid(column=0,row=0)
mac_address_responce.grid(column=1,row=0)

#Bluetooth Address
bluetooth_address_frame = tk.Frame(left_production_frame)
bluetooth_address = tk.Label(bluetooth_address_frame, text="Bluetooth Address:")
bluetooth_address_responce = tk.Button(bluetooth_address_frame, text=device_info['Bluetooth Adress'], relief="flat",command=lambda:copy_address(bluetooth_address_responce))

bluetooth_address_frame.grid(column=0,row=2,sticky="news")
bluetooth_address.grid(column=0,row=0)
bluetooth_address_responce.grid(column=1,row=0)

# Right Column

#sync device top
def finding_devices():
    print("non found yet")

device_sync_top = tk.Frame(right_production_frame,bd=2,relief="solid")

device_scan_label = tk.Label(device_sync_top,text=device_info['name'])
device_scan_button = tk.Button(device_sync_top, text="Device Scan",command=lambda:finding_devices())

device_sync_top.grid_columnconfigure(0,weight=1)
device_sync_top.grid(column=0,row=0,columnspan=1,sticky="news")
device_scan_label.grid(column=0,row=0)
device_scan_button.grid(column=1,row=0)

# Cheack list 
device_check_list = tk.Frame(right_production_frame,bd=2,relief="solid")
is_mac_check_label = tk.Label(device_check_list,text="mac adress")
is_bluetooth_check_label = tk.Label(device_check_list,text="bluetooth adress")
is_app_installed_label = tk.Label(device_check_list,text="app installed")

device_check_list.grid_columnconfigure(0,weight=1)
device_check_list.grid_columnconfigure(1,weight=2)

# Check List Lables
device_check_list.grid(column=0,row=1,columnspan=1,sticky="nsew")
is_mac_check_label.grid(column=1,row=0, sticky="w")
is_bluetooth_check_label.grid(column=1,row=1,sticky="w")
is_app_installed_label.grid(column=1,row=2,sticky="w")

#run
window.mainloop()

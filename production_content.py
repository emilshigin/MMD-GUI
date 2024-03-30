import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
import adb_connection
import production_content

THIS_FILE_DIR = os.path.dirname(__file__)
device_info = adb_connection.get_device_info()

#######################################################
# Production Content

# Copy the text to the clipboard
def copy_address(window,item):
    window.clipboard_clear()
    window.clipboard_append(item.cget("text"))
    window.update()  # Required on macOS

#sync device top
def finding_devices():
    print("non found yet")



def content(self,window,content_frame):
    self.window = window

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
    self.Neo_3_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FILE_DIR,"images\\Neo_3.jpeg")).resize((200,180)))
    self.Neo_3_image_label = tk.Label(left_production_frame,image=self.Neo_3_image, bd=2, relief="solid")
    self.Neo_3_image_label.grid(column=0,row=0,sticky="news")

    #Mac Address
    mac_address_frame = ttk.Frame(left_production_frame,padding=(3,3,12,12))
    mac_address = tk.Label(mac_address_frame, text="Mac Address:")
    mac_address_responce = tk.Button(mac_address_frame, text=device_info['MAC Address'],relief="flat",command=lambda:copy_address(window,mac_address_responce))

    mac_address_frame.grid(column=0,row=1,sticky="news")
    mac_address.grid(column=0,row=0)
    mac_address_responce.grid(column=1,row=0)

    #Bluetooth Address
    bluetooth_address_frame = tk.Frame(left_production_frame)
    bluetooth_address = tk.Label(bluetooth_address_frame, text="Bluetooth Address:")
    bluetooth_address_responce = tk.Button(bluetooth_address_frame, text=device_info['Bluetooth Adress'], relief="flat",command=lambda:copy_address(window,bluetooth_address_responce))

    bluetooth_address_frame.grid(column=0,row=2,sticky="news")
    bluetooth_address.grid(column=0,row=0)
    bluetooth_address_responce.grid(column=1,row=0)

    # Right Column
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
    

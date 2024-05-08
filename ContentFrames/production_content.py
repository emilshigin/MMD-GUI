import threading
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
from adb_connection import device

THIS_FILE_DIR = os.path.dirname( os.path.dirname(__file__))
usb_device = device()
device_info = usb_device.get_device_info()


#######################################################
# Production Content

# Copy the text to the clipboard
def copy_address(window,item) -> None:
    window.clipboard_clear()
    window.clipboard_append(item.cget("text"))
    window.update()  # Required on macOS


# Device Scan button
# Used for when a new device is pluged in
# Get and Updates the displayed info
def finding_devices(self,device_scan_label,mac_address_responce,bluetooth_address_responce,isn_responce,device_image_label) -> None:
    # Get the new Info
    usb_device = device()
    device_info = usb_device.get_device_info()
    print(device_info)
    # Update display of new info
    device_scan_label.config(text=device_info['name'])
    mac_address_responce.config(text=device_info['MAC Address'])
    bluetooth_address_responce.config(text=device_info['Bluetooth Adress'])
    isn_responce.config(text=device_info['Internal SN'])
    # Update Image
    update_device_photo(self,device_image_label,device_info['name'])
    usb_device.push_to_device(device_info['name'])

def update_device_photo(self,device_image_label,device_info_name):
    self.device_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FILE_DIR,"images","defualt_device.jpg")).resize((200,140)))
    if(device_info_name == 'Pico Neo 3 Pro Eye'):
        print("set Neo 3 image")
        self.device_image= ImageTk.PhotoImage(Image.open(os.path.join(THIS_FILE_DIR,"images","Neo_3.jpg")).resize((200,140)))
    elif(device_info_name == 'PICO G3'):
        print("set G3 image")
        self.device_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FILE_DIR,"images","G3.jpg")).resize((200,140)))
    device_image_label.config(image=self.device_image)
    device_image_label.image=self.device_image
    

def content(self,window,content_frame) -> None:
    self.window = window

    #Production Layout Setup
    production_frame = tk.Frame(content_frame,bd=2,relief="solid")

    production_frame.grid_rowconfigure(0,weight=1)
    production_frame.grid_columnconfigure(1, weight=1)

    production_frame.grid(column= 0, row= 0, sticky="news")

    
    left_production_frame = ttk.Frame(production_frame, padding = (25,5,25,0),relief="solid")
    left_production_frame.grid(column=0,row=0,sticky="news")

    right_production_frame = ttk.Frame(production_frame, padding = (20,5,40,0),relief="solid")
    right_production_frame.grid(column=1,row=0,sticky="news")


    # Left Column
    # Device Image
    self.device_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FILE_DIR,"images","defualt_device.jpg")).resize((200,140)))
    device_image_label = tk.Label(left_production_frame,image=self.device_image, bd=2, relief="solid")
    device_image_label.grid(column=0,row=0,sticky="news")
    update_device_photo(self,device_image_label,device_info['name'])

    #Mac Address
    mac_address_frame = ttk.Frame(left_production_frame,padding=(3,3,0,0))
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

    #Internal SN (ISN)
    isn_frame = tk.Frame(left_production_frame)
    isn = tk.Label(isn_frame, text="Internal SN:")
    isn_responce = tk.Button(isn_frame, text=device_info['Internal SN'], relief="flat",command=lambda:copy_address(window,isn_responce))

    isn_frame.grid(column=0,row=3,sticky="news")
    isn.grid(column=0,row=0)
    isn_responce.grid(column=1,row=0)

    # Right Column
    device_sync_top = tk.Frame(right_production_frame,bd=2,relief="solid")

    device_scan_label = tk.Label(device_sync_top,text=device_info['name'],padx=10)
    device_scan_button = tk.Button(device_sync_top, text="Device Scan",command=lambda:threading.Thread(target=finding_devices, args=(self,device_scan_label,mac_address_responce,bluetooth_address_responce,isn_responce,device_image_label)).start())

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


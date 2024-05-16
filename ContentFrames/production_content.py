import threading
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
from adb_connection import device

THIS_FILE_DIR = os.path.dirname( os.path.dirname(__file__)).replace("\\","/")
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
def finding_devices(self,device_scan_label,mac_address_responce,bluetooth_address_responce,isn_responce,device_image_label,device_check_list: tk.Frame) -> None:
    # Get the new Info
    usb_device = device()
    device_info = usb_device.get_device_info()
    print(device_info)

    print("Frames dystroyed")
    # Clear Frame
    for widgets in device_check_list.winfo_children():
      widgets.destroy()


    #Make Device Chacklist Label
    order_counter = 0
    checked_device_name = tk.Label(device_check_list,text='Checked Device Name')
    checked_mac_address = tk.Label(device_check_list,text='Checked Mac Address')
    checked_bluetooth_address = tk.Label(device_check_list,text='Checked Bluetooth Address')
    checked_isn = tk.Label(device_check_list,text='Checked ISN Number')

    # Update display of new info
    device_scan_label.config(text=device_info['name'])
    checked_device_name.grid(row=order_counter, column=0,sticky='we')

    order_counter+=1
    mac_address_responce.config(text=device_info['MAC Address'])
    checked_mac_address.grid(row=order_counter, column=0,sticky='we')
    
    order_counter+=1
    bluetooth_address_responce.config(text=device_info['Bluetooth Adress'])
    checked_bluetooth_address.grid(row=order_counter, column=0,sticky='we')

    order_counter+=1
    isn_responce.config(text=device_info['Internal SN'])
    checked_isn.grid(row=order_counter, column=0,sticky='we')

    # Update Image
    update_device_photo(self,device_image_label,device_info['name'])

    #Push Device 
    usb_device.push_to_device(device_info['name'],order_counter,device_check_list)

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
    production_frame.grid_columnconfigure(0, weight=1)
    production_frame.grid(column= 0, row= 0, sticky="news")
    
    left_production_frame = ttk.Frame(production_frame, padding = (25,5,25,0),relief="solid")
    left_production_frame.grid(column=0,row=0,sticky="news")

    right_production_frame = ttk.Frame(production_frame,padding = (20,5,15,0),relief="solid")
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

    # Cheack list 
    device_check_list = tk.Frame(right_production_frame,bd=2,relief="solid")
    device_check_list.grid_columnconfigure(0,weight=1)
    device_check_list.grid(column=0,row=10,columnspan=1,sticky="nsew")

    # Top Bar
    device_sync_top = tk.Frame(right_production_frame,bd=2,relief="solid")

    device_scan_label = tk.Label(device_sync_top,text=device_info['name'],width=20)
    device_scan_button = tk.Button(device_sync_top, text="Device Scan",command=lambda:threading.Thread(target=finding_devices, args=(self,device_scan_label,mac_address_responce,bluetooth_address_responce,isn_responce,device_image_label,device_check_list)).start())

    device_sync_top.grid_columnconfigure(0,weight=1)
    device_sync_top.grid(column=0,row=0,columnspan=1,sticky="news")
    device_scan_label.grid(column=0,row=0)
    device_scan_button.grid(column=1,row=0)

    
    


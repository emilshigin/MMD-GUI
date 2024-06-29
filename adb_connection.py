# adb commands: https://github.com/GhettoGeek/ADB 
import json
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os
import re
import tkinter as tk


THIS_FILE_DIR = os.path.dirname(__file__)
CONFIG_PATH = (THIS_FILE_DIR+'/config.json')


class device:

    def __init__(self):
        try:
            self.usb = AdbDeviceUsb()
        except:
            pass

    def get_adb_key():
        adbkey = THIS_FILE_DIR+'\\adbkey'
        with open(adbkey) as f:
            priv = f.read()
        with open(adbkey + '.pub') as f:
            pub = f.read()
        return PythonRSASigner(pub, priv)

    # Get Device info
    # Steps:
        # Check adbkey is avalable
        # Stop ADB Server
        # Try to connect USB Device
    # Return: 
    #   dictionary of device info name,internal SN,MAC Address, Bluetooth Adress 
    def get_device_info(self):
        if(os.path.isfile(THIS_FILE_DIR+"\\adbkey.pub") == False):
            keygen(THIS_FILE_DIR+'\\adbkey')
        
        try:
            adb_kill_str = os.system("adb kill-server")
            if "is not recognized" == adb_kill_str:
                print("ADB not recognuized")
                
        except Exception as e :
            print("ADB may not be installed or configured as a windows $PATH","\n",e,'\n\n')

        try:    
            self.usb.connect(rsa_keys=[device.get_adb_key()], auth_timeout_s=0.1)
        except:
            return {
                "name" : "No Device Found",
                "Internal SN" : "#################",
                "MAC Address" : "##:##:##:##:##:##",     
                "Bluetooth Adress" : "##:##:##:##:##:##",
            }
        return {
            "name" : self.usb.shell('getprop pxr.vendorhw.product.model').strip(),
            "Internal SN" : self.usb.shell('getprop ro.serialno').strip(),
            "MAC Address" : re.search(
                '[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]',
                self.usb.shell("ip address show wlan0").strip()
                ).group(),
            "Bluetooth Adress" : self.usb.shell("settings get secure bluetooth_address").strip()
        }

    def push_to_device(self,device_name,order_counter,device_check_list):   
        
        try:
            self.usb.close()
        except:
            pass

        data = json.load(open(file=CONFIG_PATH))
        
        print("Push to devices: ",device_name)
        if(device_name == 'Pico Neo 3 Pro Eye'):
            column = []

            device_upload_list = list(data[device_name].keys())
            
            count = 0
            for upload_list in device_upload_list:
                if data[device_name][upload_list]['Want'] == "1":
                    # Message: command in progress
                    text_appened = data[device_name][upload_list]['Text']
                    column.append(tk.Label(device_check_list, text = text_appened))
                    column[count].grid()
                    count += 1

                    # Command implementation
                    command = data[device_name][upload_list]['ADP command']
                    path = '"'+data[device_name][upload_list]['Path']+'"'

                    device_storage_path = ""
                    if('Device Storage Path' in data[device_name][upload_list]):
                       device_storage_path = '"'+data[device_name][upload_list]['Device Storage Path']+'"'

                    os.system(f'adb {command} {path} {device_storage_path}')

                    
            
            #Make Device Chacklist Label
            
            # pushing_da = tk.Label(device_check_list,text='Pushing DA Calib')
            # install_am = tk.Label(device_check_list,text='Installing App Manager')
            # install_pm = tk.Label(device_check_list,text='Installing PM APK')
            # install_vf = tk.Label(device_check_list,text='Installing VF APK')
            
            # # Push Files
            # # DA Calabration
            # order_counter+=1
            # pushing_da.grid(row=order_counter, column=0,sticky='we')
            # temp_str = data["Pico Neo 3"]["Current DA Calib"]
            # os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')


            #     # App Manager
            # order_counter+=1
            # install_am.grid(row=order_counter, column=0,sticky='we')
            # temp_str = data["Pico Neo 3"]["Current App Manager APK"]
            # os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            # os.system(f'adb install "{temp_str}"')

            #     # Puplometer
            # order_counter+=1
            # install_pm.grid(row=order_counter, column=0,sticky='we')
            # temp_str = data["Pico Neo 3"]["Current PM APK"] 
            # os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            # os.system(f'adb install "{temp_str}"')

            #     # VF2000
            # order_counter+=1
            # install_vf.grid(row=order_counter, column=0,sticky='we')
            # temp_str = data["Pico Neo 3"]["Current VF APK"]
            # os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            # os.system(f'adb install "{temp_str}"')

        elif ( device_name == "PICO G3"):
            install_am = tk.Label(device_check_list,text='Installing App Manager')
            install_vf = tk.Label(device_check_list,text='Installing VF APK')


            # Push Files
            #   # App Manager
            order_counter+=1
            install_am.grid(row=order_counter, column=0,sticky='we')
            temp_str = data["PICO G3"]["Current App Manager APK"] 
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')
            
            #   # VF2000
            order_counter+=1
            install_vf.grid(row=order_counter, column=0,sticky='we')
            temp_str = data["PICO G3"]["Current VF APK"] 
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')
            
        else:
            print("Devices No Yet Setup: ",device_name)

        # Add the last line in feedback loop
        column.append(tk.Label(device_check_list,text='All Porcesses Finished'))
        column[count].grid()

  


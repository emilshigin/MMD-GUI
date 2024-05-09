# adb commands: https://github.com/GhettoGeek/ADB 
import json
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os
import re
import tkinter as tk


THIS_FILE_DIR = os.path.dirname(__file__)

class device:

    def __init__(self):
        try:
            self.usb = AdbDeviceUsb()
        except:
            print('No device found')

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
            # Neo 3[Before Update]: pxr.vendorhw.product.model
            "name" : self.usb.shell('getprop pxr.vendorhw.product.model').strip(),
            "Internal SN" : self.usb.shell('getprop ro.serialno').strip(),
            "MAC Address" : re.search(
                '[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]',
                self.usb.shell("ip address show wlan0").strip()
                ).group(),
            "Bluetooth Adress" : self.usb.shell("settings get secure bluetooth_address").strip()
        }

    def push_to_device(self,device_name,order_counter,device_check_list):   
        self.usb.close()

        data = json.load(open(file="config.json"))
        data["Pico Neo 3"]["Current VF APK"]
        
        print("Push to devices: ",device_name)
        if(device_name == 'Pico Neo 3 Pro Eye'):
            #Make Device Chacklist Label
            pushing_da = tk.Label(device_check_list,text='Pushing DA Calib')
            install_am = tk.Label(device_check_list,text='Installing App Manager')
            install_pm = tk.Label(device_check_list,text='Installing PM APK')
            install_vf = tk.Label(device_check_list,text='Installing VF APK')

            # Push Files
            # DA Calabration
            order_counter+=1
            pushing_da.grid(row=order_counter, column=0,sticky='we')
            temp_str = data["Pico Neo 3"]["Current DA Calib"]
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')


                # App Manager
            order_counter+=1
            install_am.grid(row=order_counter, column=0,sticky='we')
            temp_str = data["Pico Neo 3"]["Current App Manager APK"]
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')

                # Puplometer
            order_counter+=1
            install_pm.grid(row=order_counter, column=0,sticky='we')
            temp_str = data["Pico Neo 3"]["Current PM APK"] 
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')

                # VF2000
            order_counter+=1
            install_vf.grid(row=order_counter, column=0,sticky='we')
            temp_str = data["Pico Neo 3"]["Current VF APK"]
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')

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

        done = tk.Label(device_check_list,text='All Porcesses Finished')
        order_counter+=1
        done.grid(row=order_counter, column=0,sticky='we')

    # List od adb commands
    # https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8
    # python uninstall uninstall com.MMD.VR2KN3
    # Neo2 [pxr.vendorhw.product.model]: [Pico Neo 2 Eye]

    # Push files and apg
    # push apk mmd manager
    # install apk  
  


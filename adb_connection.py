# adb commands: https://github.com/GhettoGeek/ADB 
import json
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os
import re
import sys
from subprocess import run
import tkinter as tk
import time

THIS_FILE_DIR = os.path.dirname(__file__)
# print("File path of adb_connection: ",THIS_FILE_DIR)
# File path of adb_connection:  D:\GitHub\MMD-GUI
CONFIG_PATH = os.path.join(THIS_FILE_DIR,'config.json')
ADB_PATH = os.path.join(os.path.dirname(__file__), "adb_tools", "adb.exe")

# Get absolute path to resource, works for dev and PyInstaller
def resource_path(*paths):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, *paths)

class device:
    def __init__(self):
        try:
            self.usb = AdbDeviceUsb()
            self.initialized = True
        except Exception as e:
            print("Failed to initialize ADB USB device:\n\t",e)
            self.initialized = False

    def get_adb_key():
        adb_key_path  = resource_path('adbkey')
        with open(adb_key_path, 'r' ) as f:
            priv = f.read()
        with open(adb_key_path  + '.pub','r') as f:
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
        if not self.initialized:
            return self._default_device_info("No device plugged in")
        
        #Check ADB Key
        adb_pub_key = resource_path('adbkey.pub')

        if not os.path.isfile(adb_pub_key):
            keygen(resource_path("adbkey"))

        def try_connect():
            try:
                print("Attempting USB ADB connection...")
                self.usb.connect(rsa_keys=[device.get_adb_key()], auth_timeout_s=0.1)
                print("✅ USB Connected")
                return True
            except Exception as e:
                print("❌ USB Connection failed:", e)
                return False

       
        if not try_connect():
            os.system("adb kill-server")
            time.sleep(.5)
            if not try_connect(): 
                return self._default_device_info("USB connection failed after 2 attempts")
     
        try:
            model = self.usb.shell('getprop pxr.vendorhw.product.model').strip()
            serial = self.usb.shell('getprop ro.serialno').strip(),
            mac_address = re.search(r'([0-9a-f]{2}:){5}[0-9a-f]{2}',self.usb.shell("ip address show wlan0").strip()).group(),
            bluetooth_address = self.usb.shell("settings get secure bluetooth_address").strip()

            return {
                "name": model,
                "Internal SN": serial,
                "MAC Address": mac_address,
                "Bluetooth Address": bluetooth_address
            }

        except Exception as e:
            print("Failed to fetch device info:", e)
            return self._default_device_info("Error retrieving properties")
    
    
    def _default_device_info(self, reason="Unknown"):
        print(f"[INFO] Returning default device info due to: {reason}")
        return {
            "name": "No Device Found",
            "Internal SN": "#################",
            "MAC Address": "##:##:##:##:##:##",
            "Bluetooth Address": "##:##:##:##:##:##",
        }

    def push_to_device(self,device_name,device_check_list):   
        try:
            self.usb.close()
        except:
            pass
        
        try:
            with open(CONFIG_PATH,"r") as f:
                data = json.load(f)
        except Exception as e:
            print("Failed to read config:", e)
            return
        
        print("Push to devices: ",device_name)
        
        for key, item in data[device_name].items():
            if item.get("Want") != "1":
                continue

            # Display status in GUI
            label = tk.Label(device_check_list, text=item.get("Text", "Processing..."))
            label.grid()

            command = item.get("ADP command", "push")
            path = resource_path(item.get("Path", ""))
            path_target = item.get("Path Target", "")
            device_storage_path = item.get("Device Storage Path", "")

            # Sanitize paths
            path = f'"{path}"' if path else ""
            path_target = f'"{path_target}"' if path_target else ""
            device_storage_path = f'"{device_storage_path}"' if device_storage_path else ""

            adb_command = f'{ADB_PATH} {command} {path} {device_storage_path} {path_target}'
            print(f"[ADB] {adb_command}")

            try:
                result = run(adb_command, shell=True, capture_output=True, text=True)
                if result.returncode != 0:
                    print("ADB command failed:", result.stderr)
                else:
                    print("ADB command succeeded:", result.stdout)
            except Exception as e:
                print("Failed to run adb command:", e)

        # Final message
        tk.Label(device_check_list, text='All Processes Finished').grid()
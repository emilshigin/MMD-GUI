# adb commands: https://github.com/GhettoGeek/ADB 
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os
import re


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

    def push_to_device(self,device_name):   
        self.usb.close()
        
        print("Push to devices: ",device_name)
        if(device_name == 'Pico Neo 3 Pro Eye'):
            # Push Files
            # DA Calabration
            temp_str = THIS_FILE_DIR+'\\Backup\\Pico Neo 3\\DA_Calib_DoNotDelete.txt'
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
                # App Manager
            temp_str = THIS_FILE_DIR+'\\Backup\\Pico Neo 3\\\\MMD_AppManager_3.apk'
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')
                # Puplometer
            temp_str = THIS_FILE_DIR+'\\Backup\\Pico Neo 3\\PM2000_1.1.8.apk'
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')

                # VF2000
            temp_str = THIS_FILE_DIR+'\\Backup\\Pico Neo 3\\VR2KN3_1_4_12.apk'
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')

        if ( device_name == "PICO G3"):
             # Push Files
                # App Manager
            temp_str = THIS_FILE_DIR+'\\Backup\\Pico G3\\\\MMD_AppManager_3.apk'
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')
                # VF2000
            temp_str = THIS_FILE_DIR+'\\Backup\\Pico Neo 3\\VR2KN3_1_4_12.apk'
            os.system(f'adb push "{temp_str}" /storage/emulated/0/Download')
            os.system(f'adb install "{temp_str}"')

        else:
            print("Devices No Yet Setup: ",device_name)

    # List od adb commands
    # https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8
    # python uninstall uninstall com.MMD.VR2KN3
    # Neo2 [pxr.vendorhw.product.model]: [Pico Neo 2 Eye]

    # Push files and apg
    # push apk mmd manager
    # install apk  
  


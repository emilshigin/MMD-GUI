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
            "name" : self.usb.shell('getprop sys.pxr.product.name').strip(),
            "Internal SN" : self.usb.shell('getprop ro.serialno').strip(),
            "MAC Address" : re.search(
                '[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]',
                self.usb.shell("ip address show wlan0").strip()
                ).group(),
            "Bluetooth Adress" : self.usb.shell("settings get secure bluetooth_address").strip()
        }

    def push_to_device(self):   
        self.usb.close()
        print("push to device")

        # Push Files
        # DA Calabration
        os.system('adb push "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\DA_Calib_DoNotDelete.txt" /storage/emulated/0/Download')
        # # App Manager
        os.system('adb push "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\MMD_AppManager_3.apk" /storage/emulated/0/Download')
        # # Puplometer
        os.system('adb push "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\PM2000_1.1.8.apk" /storage/emulated/0/Download')
        # # VF2000
        os.system('adb push "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\VR2KN3_1_4_12.apk" /storage/emulated/0/Download')

        # Install Updates
        os.system('adb install "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\MMD_AppManager_3.apk"')
        os.system('adb install "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\PM2000_1.1.8.apk"')
        os.system('adb install "C:\\Users\\emil\\Desktop\\VF2000 Software\\Current realease\\Neo 3_CurCon\\VR2KN3_1_4_12.apk"')


    # List od adb commands
    # https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8
    # python uninstall uninstall com.MMD.VR2KN3
    # Neo2 [pxr.vendorhw.product.model]: [Pico Neo 2 Eye]

    # Push files and apg
    # push apk mmd manager
    # install apk  
  


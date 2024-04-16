# adb commands: https://github.com/GhettoGeek/ADB 
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os
import re

THIS_FILE_DIR = os.path.dirname(__file__)
 
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
def get_device_info():
    if(os.path.isfile(THIS_FILE_DIR+"\\adbkey.pub") == False):
        keygen(THIS_FILE_DIR+'\\adbkey')
    
    try:
        adb_kill_str = os.system("adb kill-server")
        if "is not recognized" in adb_kill_str:
            print("ADB may not be installed or configured as a windows $PATH")
    except Exception :
        print("ADB may not be installed or configured as a windows $PATH")

    try:    
        device = AdbDeviceUsb()
        device.connect(rsa_keys=[get_adb_key()], auth_timeout_s=0.1)
    except:
        return {
            "name" : "No Device Found",
            "Internal SN" : "#################",
            "MAC Address" : "##:##:##:##:##:##",     
            "Bluetooth Adress" : "##:##:##:##:##:##",
        }
    return {
        "name" : device.shell('getprop sys.pxr.product.name').strip(),
        "Internal SN" : device.shell('getprop ro.serialno').strip(),
        "MAC Address" : re.search(
            '[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]:[0-9a-z][0-9a-z]',
            device.shell("ip address show wlan0").strip()
            ).group(),
        "Bluetooth Adress" : device.shell("settings get secure bluetooth_address").strip()
    }

# Functions for testing
def new_device_info():
    try:    
        device = AdbDeviceUsb()
        device.connect(rsa_keys=[get_adb_key()], auth_timeout_s=0.1)
    except:
        return print("error no device found")
    print(device.shell('getprop '))

def uninstall_apk():
    try:    
        device = AdbDeviceUsb()
        device.connect(rsa_keys=[get_adb_key()], auth_timeout_s=0.1)
    except:
        return print("error no device found")
    print(device.shell('uninstall com.MMD.VR2KN3'))


# List od adb commands
# https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8
# python uninstall uninstall com.MMD.VR2KN3
# Neo2 [pxr.vendorhw.product.model]: [Pico Neo 2 Eye]

# if __name__ == '__main__':
#     uninstall_apk()
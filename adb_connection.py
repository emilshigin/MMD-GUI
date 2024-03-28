# adb commands: https://github.com/GhettoGeek/ADB 
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os
import re

THIS_FILE_DIR = os.path.dirname(__file__)
 
    
def get_adb_key():
    # Load the public and private keys
    adbkey = THIS_FILE_DIR+'\\adbkey'
    with open(adbkey) as f:
        priv = f.read()
    with open(adbkey + '.pub') as f:
        pub = f.read()
    return PythonRSASigner(pub, priv)


#Neo info check with other device
def get_device_info():
    if(os.path.isfile(THIS_FILE_DIR+"\\adbkey.pub") == False):
        keygen(THIS_FILE_DIR+'\\adbkey')
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

# print(get_device_info())

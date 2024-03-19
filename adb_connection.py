# adb commands: https://github.com/GhettoGeek/ADB 
from adb_shell.adb_device import  AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen
import os

THIS_FILE_DIR = os.path.dirname(__file__)
global signer 


def get_adb_key():
    # Load the public and private keys
    adbkey = 'path/to/adbkey'
    with open(adbkey) as f:
        priv = f.read()
    with open(adbkey + '.pub') as f:
        pub = f.read()
    signer = PythonRSASigner(pub, priv)

def generate_adb_key():
    print("print 1")
    print("Dir:",THIS_FILE_DIR )
    keygen(THIS_FILE_DIR)
    print("step 2")

if(os.path.isfile(THIS_FILE_DIR+"\adbkey.pub") == False):
    generate_adb_key()
    print("adb key generated")

# # Connect via USB (package must be installed via `pip install adb-shell[usb])`
# device2 = AdbDeviceUsb()
# device2.connect(rsa_keys=[signer], auth_timeout_s=0.1)

# # Send a shell command
# response2 = device2.shell('echo TEST2')
# Description
## Objective:
* Get information from VR Headset Devices 
* Push files onto the headset

## Technology
* Python
* TKinter
* adb-shell[usb]

# Demos And Features
## Production Page
### Fetures:
* Supports hot swapping devices for multiple device configurations. 
* Clicking on any of the Address puts the address into the Clipboard to record device info.
  
### Scan Button Fetures:
Press "Device Scan" after pluging in a device to computer to get:
* MAC Address 
* Bluetooth Address 
* Internal Serial Number 
* Installs Apks and Pushes files (Configured in the Settings page) 

### *Device Scan Button Demo:*  
<img src="https://github.com/emilshigin/MMD-GUI/assets/71671062/1cc1a295-69fb-4ad1-841c-d7dfab3f72a7" alt="GIF of pressing device scan and retreaving info from diffrent devices" width="600">

At the start of the demo no devices was pluged in. \
Between pressing "Device Scan" a new device was plugged in. 

After the demo, new features were added that are not represented in the demo. \
Feedback to the user was placed under the device scan. \
Feedback lists contain the current process that was being done. \
Last entry is always "All Porcesses Finished" 

## Settings Page 
### *Changing Start Up Page* 
<img src="https://github.com/emilshigin/MMD-GUI/assets/71671062/4c48c3b5-f7b6-46dd-85f6-672466bf31c8" alt="GIF of how to changing stratup page in the settings options " width="600">

### *Selecting Folder to Upload* 
![Settings uploading](https://github.com/emilshigin/MMD-GUI/assets/71671062/584168d6-d7e8-4008-a620-7568227dcbe7) 
* When a selected file is not in the backup directory a copy is made
* Device specific tabs
  

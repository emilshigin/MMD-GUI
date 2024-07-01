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
<img src="https://github.com/emilshigin/MMD-GUI/assets/71671062/e541daf6-b7ff-42ad-9b50-b1875b07b654" alt="GIF of pressing device scan and retreaving info from diffrent devices" width="600">

At the start of the demo no devices was pluged in. \
Between pressing "Device Scan" a new device was plugged in. 
Feedback to the user is placed under the device scan. \
The feedback is in real time. \
Last entry is always "All Porcesses Finished". \
We end the demo by copying the device information into notepad. 

## Settings Page 
### *Changing Start Up Page* 
<img src="https://github.com/emilshigin/MMD-GUI/assets/71671062/4c48c3b5-f7b6-46dd-85f6-672466bf31c8" alt="GIF of how to changing stratup page in the settings options " width="600">

### *Selecting Folder to Upload* 
<img src="https://github.com/emilshigin/MMD-GUI/assets/71671062/584168d6-d7e8-4008-a620-7568227dcbe7" alt="GIF of how to set upload files " width="600">

* When a selected file is not in the backup directory a copy is made
* Select the device tabs to update what files are installed  
  
### Set Up Application:
* Remenber to install all the dependencies from the dependancies.txt
* In the backup folder make a folder for each device w\ the device name 
* For git
#### Not track config.json :  
``` git update-index --assume-unchanged config.json ```
#### Start tracking config.json again :  
``` git update-index --no-assume-unchanged config.json ```


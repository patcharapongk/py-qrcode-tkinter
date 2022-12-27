# py-qrcode-tkinter
QR Code tools using Python + Tkinter GUI 


![program preview](https://raw.githubusercontent.com/patcharapongk/py-qrcode-tkinter/main/readme_img/main-program.jpg)
<p align="center"> Program Preview </p>

![GUI mode](https://github.com/patcharapongk/py-qrcode-tkinter/blob/main/readme_img/open-dialogue.jpg?raw=true)
<p align="center"> Open File via GUI</p>


#### Features
- Read QR image from GUI dialogue
- Read QR image from CLI argument
- Show current decoding image path
---
#### Dependencies
- pyzbar
- pillow
- tkinter
- dotenv (optional)
---
#### Version History
- v0.1a test decode QR code using pyzbar 
- v0.1b test open file using tkinter dialouge
- v0.2 combined both 0.1a 0.1b
- v0.3 added CLI argument support (bypass UI)
- v0.4 separated decode logic into its own button
- v0.5 added clearable textbox
- v0.6 added currrent image path on label and window title

- v1.0 added support for multiple QR in one image
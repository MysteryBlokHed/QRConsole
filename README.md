# QRConsole
A library to display QR codes in console.

## Requirements
**Pillow>=7.0.0** - Download using `python` or `python3 -m pip install "Pillow>=7.0.0"`

## Installation
### PyPI
To get the module through PyPi: `pip install qrconsole`.  
### GitHub (Pulled Repo)
To install the module by pulling the repo: `python setup.py install`.  

## How to use
QRConsole is pretty straight-forward. Provide an image, and it will return a string with the console-ified version.  
The image provided must be black-and-white. If there are greys, they will be turned into white or black depending on which they are closer to.  
A good site for creation is [this one](https://www.the-qrcode-generator.com/), since there is no rounding or styling, just b&w pixels.  
**It is recommended to keep the images as small as possible, since every pixel of the image is two characters in the console. The example image is 65x65 px.**  

## Use
1. Initialize
```python
from qrconsole import QRConsole
qr = QRConsole(char="@") # char = The character to use for white in the QR Code. Must have a length of 1.
```
2. Console-ify image
```python
print(qr.consoleify(qr_img="example_code.png")) # qr_img = The path to the QR Code image.
```
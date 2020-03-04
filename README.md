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
### In a project
1. Initialize  
```python
from qrconsole import QRConsole
qr = QRConsole(char="@") # char = The character to use for white in the QR Code. Must have a length of 1.
```
2. Console-ify image  
There are two ways to do this. The first way is to provide a path to the image:  
```python
print(qr.consoleify(qr_img="path_to_code.png", resize_factor=1))
# `qr_img: str` - The path to the QR Code image.
# `resize_factor: float` - How much to shrink/grow the image by (`width/resize_factor`, `height/resize_factor`)
```  
And the second way is to provide a Pillow Image object:  
```python
from PIL import Image
img = Image.open("path_to_code.png")
print(qr.consoleify(qr_img=img, resize_factor=1))
# `qr_img: Image` - A Pillow Image object.
# `resize_factor: float` - How much to shrink/grow the image by (`width/resize_factor`, `height/resize_factor`)
```
Some libraries (for example the `qrcode` library) can turn codes into Images natively, so this method would be easier to use to avoid unnecessary file-writing.
### Through `python -m`
It is also possible to use QRConsole as a command line tool. After installing the package, run `python` or `python3 -m qrconsole <image path> <resize factor (optional)>`.
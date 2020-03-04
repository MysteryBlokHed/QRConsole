# Created by Adam Thompson-Sharpe on 02/03/2020.
# Licensed under MIT.
from qrconsole import QRConsole

qr = QRConsole()
img = input("Target image (example_code.png): ")
if img == "":
    img = "example_code.png"
resize_factor = input("Resize factor (how much to downscale image by) (3.5): ")
if resize_factor == "":
    resize_factor = 3.5
resize_factor = float(resize_factor)

print(qr.consoleify(img, resize_factor))

# Created by Adam Thompson-Sharpe on 02/03/2020.
# Licensed under MIT.
from qrconsole import QRConsole

qr = QRConsole()
img = input("Target image (example_code.png): ")
if img == "":
    img = "example_code.png"
print(qr.consoleify(img))

# Created by Adam Thompson-Sharpe on 02/03/2020.
# Licensed under MIT.
import sys
from .qrconsole import QRConsole

qr = QRConsole()
# See if the last argv is a float
try:
    resize_factor = float(sys.argv[-1])
    img = sys.argv[-2]
# If not, use the default resize_factor
except ValueError:
    resize_factor = 1
    img = sys.argv[-1]

print(qr.consoleify(img, resize_factor))

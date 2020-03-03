# Created by Adam Thompson-Sharpe on 02/03/2020.
# Licensed under MIT.
import sys
from .qrconsole import QRConsole

qr = QRConsole()
# Use last argument as image path
print(qr.consoleify(sys.argv[-1:][0]))

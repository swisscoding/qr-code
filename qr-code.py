#!/usr/local/bin/python3

import pyqrcode
import colored

print(colored.stylize("\n---- | Create QR-Code | ----\n", colored.fg("red")))

url = input("Type in the URL: ")
print()

qrCode = pyqrcode.create(url, error="L", version=3)
qrCode.png('QR-Code.png', scale=20)
qrCode.show()

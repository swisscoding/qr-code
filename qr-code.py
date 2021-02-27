#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

import pyqrcode, colored

print(colored.stylize("\n---- | Create QR-Code | ----\n", colored.fg("red")))

# url for the qr code
url = input("Type in the URL: ")
print()

# creation
qrCode = pyqrcode.create(url, error="L", version=3)
qrCode.png("QR-Code.png", scale=20)
qrCode.show()

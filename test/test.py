#! /usr/bin/env python3
import os

devices = []
devices=os.system("python3 ../RaspCode/Bl_Scripts/ListBL.py")
#" ".join(devices)
print('Les appareils sont : ' + str(devices))

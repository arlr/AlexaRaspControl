#! /usr/bin/env python3
import os


devices=os.system("python3 ../RaspCode/Bl_Scripts/ListBL.py")

print("Les appareils sont : %s", devices)

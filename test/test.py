#! /usr/bin/env python3
#https://www.developpez.net/forums/d956151/autres-langages/python-zope/general-python/recuperer-resultat-commandes-shell/
import os
import subprocess

devices = subprocess.Popen(["python3", "../RaspCode/Bl_Scripts/ListBL.py"],stdout=subprocess.PIPE)
stdout_value=devices.communicate()
devices.kill()
print(stdout_value)
#" ".join(devices)
print('Les appareils sont : ' + str(stdout_value))

#! /usr/bin/env python3
#https://www.developpez.net/forums/d956151/autres-langages/python-zope/general-python/recuperer-resultat-commandes-shell/
import os
import subprocess

devices = subprocess.run(["python3", "../RaspCode/Bl_Scripts/ListBL.py"],stdout=subprocess.PIPE)

stdout_value=devices.stdout.decode('utf-8')
#devices.kill()
#print(stdout_value)
print('Les appareils sont : ' + stdout_value)

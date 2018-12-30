#! /usr/bin/env python3
#https://www.developpez.net/forums/d956151/autres-langages/python-zope/general-python/recuperer-resultat-commandes-shell/
import os
import subprocess

subprocess.run(["python3", "../RaspCode/Bl_Scripts/ScanBL.py", "&"])

#print(stdout_value)



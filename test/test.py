#! /usr/bin/env python3
#https://www.developpez.net/forums/d956151/autres-langages/python-zope/general-python/recuperer-resultat-commandes-shell/

import sys ,subprocess
subprocess.call(['python3', 'ScanBL.py', '&'], cwd='../RaspCode/Bl_Scripts')
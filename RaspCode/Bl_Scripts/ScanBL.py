#!/usr/bin/env python3

#Fonction de recherche Testé & Validé !

# simple inquiry example
import bluetooth
import sys
device = []

nearby_devices = bluetooth.discover_devices(lookup_names=True)
#print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    device.append(name)
  #  print("  %s - %s" % (addr, name))
    

#print(device)   #Affiche la liste dans la quelle se trouve les nom des interfaces
SaveFile = open("BlSave.txt", "x")
SaveFile.write(str(device))
SaveFile.close()

#sys.exit(device)    #Retourne la liste des appareils
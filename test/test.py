#! /usr/bin/env python3
#https://www.developpez.net/forums/d956151/autres-langages/python-zope/general-python/recuperer-resultat-commandes-shell/
#import bluetooth
import sys ,os
#device = ['Galaxy S9', '[TV] UE50JU6800']
SizeList = 0
last = ""
result = ""

nearby_devices = bluetooth.discover_devices(lookup_names=True)
#print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    device.append(name)
  #  print("  %s - %s" % (addr, name))
    

#print(device)   #Affiche la liste dans la quelle se trouve les nom des interfaces

#Mise en forme string
SizeList = len(device)
last=device[-1]
device.remove(last)

",".join(device)

result = str(device)
result = result.replace("['",' ')
result = result.replace("']",' ')

result = result + " et " + str(last)
SaveFile = open("BlSave.txt", "w")
SaveFile.write(str(result))
SaveFile.close()

print(result)
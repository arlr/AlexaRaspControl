#!/usr/bin/env python3

#Fonction de recherche Testé & Validé !

# simple inquiry example
import bluetooth
import sys ,os
device = []
SizeList = 0
last = ""
result = ""


nearby_devices = bluetooth.discover_devices(lookup_names=True)
#print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    device.append(name)
  #  print("  %s - %s" % (addr, name))
    

#Mise en forme string
SizeList = len(device)
if SizeList > 1 :
    last=device[-1]
    device.remove(last)

    ",".join(device)

    result = str(device)
    result = result.replace("['",' ')
    result = result.replace("']",' ')

    result = result + " et " + str(last)
else:
    result = str(device)
    result = result.replace("['",' ')
    result = result.replace("']",' ')

SaveFile = open("./BlSave.txt", "w")
SaveFile.write(str(result))
SaveFile.close()

#print(result)
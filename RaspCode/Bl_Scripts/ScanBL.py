#!/usr/bin/env python3

#Fonction de recherche Testé & Validé !

# simple inquiry example
import bluetooth
import sys ,os
device = []

last = ""
result = ""


nearby_devices = bluetooth.discover_devices(lookup_names=True)
#print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    device.append(name)
  #  print("  %s - %s" % (addr, name))
    

#print(device)   #Affiche la liste dans la quelle se trouve les nom des interfaces
last=device[-1]
device.remove(last)

",".join(device)

result = str(device)
result = result.replace("['",' ')
result = result.replace("']",' ')
#Cas liste vide
result = result.replace("[",' ')
result = result.replace("]",' ')
result = result + " et " + str(last)

SaveFile = open("BlSave.txt", "w")
SaveFile.write(str(result))
SaveFile.close()

print(result)

#sys.exit(device)    #Retourne la liste des appareils
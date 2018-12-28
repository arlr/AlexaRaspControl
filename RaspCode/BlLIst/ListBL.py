#!/usr/bin/env python3

#Fonction de recherche Testé & Validé !

# simple inquiry example
import bluetooth

device = []
i = 0
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    device[i] = name
    print("  %s - %s" % (addr, name))
    i = i + 1

print(device)

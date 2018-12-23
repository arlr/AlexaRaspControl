#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Source : https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3

import bluetooth

#Cherches appareils bluetooth
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))

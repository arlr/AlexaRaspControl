#!/usr/bin/env python3

#Source : https://stackoverflow.com/questions/37465157/pairing-bluetooth-devices-with-passkey-password-in-python-rfcomm-linux
#       : https://people.csail.mit.edu/albert/bluez-intro/x232.html

import sys

device = sys.argv[1]    #Le nom de l'appareil a se conecter est donné en 1er Argument (L'argument 0 est le nom du script python)
addr = sys.argv[2]  #Adress bluetooth de l'appareil
passwd = sys.argv[3]    #Le mot de passe est passé en 3eme argument

# kill any "bluetooth-agent" process that is already running
subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

# Start a new "bluetooth-agent" process where XXXX is the passkey
status = subprocess.call("bluetooth-agent " + passwd + " &",shell=True)



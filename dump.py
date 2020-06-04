#!/usr/bin/python3.7

from __future__ import unicode_literals
from prompt_toolkit import prompt
import os
from termcolor import colored
from time import sleep

	

print('Enter the Interface >> ')
interface = prompt()
print("Enter the target MAC Address [BSSID] >> ")
bssid = prompt()
print("Enter the name [ESSID] >> ")
essid = prompt()
#station = raw_input("Enter the station of the network : ")
print("Enter the channel number that the wireless network is currently running on [CH] >> ")
channel = prompt()

airodump2 = 'airodump-ng --ignore-negative-one -c {0} --bssid {1} -w {2} {3}'.format(channel, bssid, essid, interface +'mon')
os.system(airodump2)

sleep(5)



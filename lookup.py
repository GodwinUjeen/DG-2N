#!/usr/bin/python3.7
from requests import get
from termcolor import colored


def nslookup(ns_inp):
	try:
		result = get('http://api.hackertarget.com/dnslookup/?q=' + ns_inp).text
		print('\n' + result)
	except:
		print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))

def geo_ip(inp):
	try:
		result = get("https://api.hackertarget.com/geoip/?q=" + inp).text
		print('\n' + result)
	except:
		print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))
	
def nmap(inp):
	try:
		result = get("https://api.hackertarget.com/nmap/?q=" + inp).text
		print('\n' + result)
	except:
		print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))
	
def whois(url):
	try:
		result = get('http://api.hackertarget.com/whois/?q=' + url).text
		print('\n'+ result + '\n')
	except:
		print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))


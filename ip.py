#!/usr/bin/python3.7

from requests import get
import shodan
import json
from termcolor import colored

api = shodan.Shodan("")


def shodan_host(IP):
    try:
        host = api.host(IP)
        print("\n"+ colored("[",'blue') + colored('+','red') + colored("] Gathering IP Address Information from [shodan]\n",'blue'))
        print("IP Address ----> " + str(host['ip_str']))
        print("Country -------> " + str(host['country_name']))
        print("City ----------> " + str(host['city']))
        print("Organization --> " + str(host['org']))
        print("ISP -----------> " + str(host['isp']))
        print("Open ports ----> " + str(host['ports']))
    except:
        print("\n"+ colored("[",'blue') + colored('+','red') + colored("] Gathering IP Address Information from [shodan]",'blue'))
        print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))


def shodan_IP(IP):
    try:
        host = api.host(IP)
        print("\n"+ colored("[",'blue') + colored('+','red') + colored("] Gathering Domain Information from [shodan]\n",'blue'))
        print("IP Address ----> " + str(host['ip_str']))
        print("Country -------> " + str(host['country_name']))
        print("City ----------> " + str(host['city']))
        print("Organization --> " + str(host['org']))
        print("ISP -----------> " + str(host['isp']))
        print("Open ports ----> " + str(host['ports']))
    except:
        print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))

def censys_ip(IP):
    try:
        dirty_response = get('https://censys.io/ipv4/%s/raw' % IP).text
        clean_response = dirty_response.replace('&#34;', '"')
        x = clean_response.split('<code class="json">')[1].split('</code>')[0]
        censys = json.loads(x)

        print("\n"+ colored("[",'blue') + colored('+','red') + colored("] Gathering Location Information from [censys]\n",'blue'))
        print("Country -------> "+str(censys["location"]["country"]))
        print("Continent -----> "+str(censys["location"]["continent"]))
        print("Country Code --> "+str(censys["location"]["country_code"]))
        print("Latitude ------> "+str(censys["location"]["latitude"]))
        print("Longitude -----> "+str(censys["location"]["longitude"]))
    except:
        print(colored("\n[",'red') + '-' + colored("] Unavailable",'red'))




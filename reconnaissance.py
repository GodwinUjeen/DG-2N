#!/usr/bin/python3.7

from __future__ import unicode_literals
from prompt_toolkit import prompt
from dns_lookup import dnslookup
import dns_lookup
import socket
import pyfiglet
import ip
from ip import shodan_host
from ip import shodan_IP
from ip import censys_ip
from lookup import nslookup
from lookup import whois
from lookup import geo_ip
from lookup import nmap
import os
from termcolor import colored


def start():

    font = colored(pyfiglet.figlet_format(
        "RECONNAISSANCE", font='slant'), 'red', attrs=['bold'])
    print (font)

    return("""

ENTER 0 - 7 TO SELECT OPTIONS

1. IP                Enumerate  information  from  IP Address
2. URL               Gather  information  about given Website
3. WHOIS             Gather domain  registration  information
4. DNS LOOKUP        Map DNS  records associated  with target
5. NMAP              Performs NMAP scan on the target(for discovering ports)
6. NS LOOKUP         Obtain domain name or IP address mapping
7. GEO LOCATION      Gives the location of the IP Address

0. EXIT              Exit( Reconnaissance)
       """)


def project():
    while 1:

        os.system('clear')
        print(colored(start(), attrs=['bold']))
        print (colored('\n\n[Enter 8 for Main Menu]', 'cyan', attrs=['bold']))
        print(colored("Enter a number >> ", 'blue', attrs=['bold']))
        user_input = prompt()
        try:
            if len(user_input) != 1:
                os.system('clear')
                print(colored("ENTER CORRECT CHOICE\n", 'red', attrs=['bold']))
                continue
        except (TypeError, NameError, ValueError):
            os.system('clear')
            print(colored("ENTER CORRECT CHOICE\n", 'red', attrs=['bold']))
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print(colored("ENTER CORRECT CHOICE\n", 'red', attrs=['bold']))
            continue

        if choice == 1:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "IP INFO", font="slant"), 'blue', attrs=['bold'])
            print(font)
            while 1:
                print(colored("TARGET (IP) >> ", 'red', attrs=['bold']))
                ip = prompt()
                break
            shodan_host(ip)
            censys_ip(ip)
            try:

                input(colored("\nPress Enter To Continue.....",
                              'yellow', attrs=['blink']))
                os.system('clear')
            except SyntaxError:
                pass

        elif choice == 2:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "URL INFO", font="slant"), 'blue', attrs=['bold'])
            print(font)
            while 1:
                print(colored("TARGET (URL) >> ", 'red', attrs=['bold']))
                url_inp = prompt()
                break
            try:
                url = socket.gethostbyname(url_inp)
                shodan_IP(url)
                try:
                    input(colored("\nPress Enter To Continue.....",
                                  'yellow', attrs=['blink']))
                except SyntaxError:
                    pass

            except:
                print('\n' + colored('[', 'red', attrs=['bold']) + colored('!!!', 'cyan',
                                                                           attrs=['bold']) + colored('] Uavailable', 'red', attrs=['bold']))

        elif choice == 3:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "WHO IS", font="slant"), 'blue', attrs=['bold'])
            print(font)

            while 1:
                print(colored("TARGET (URL) >> ", 'red', attrs=['bold']))
                whois_inp = prompt()
                break
            whois(whois_inp)
            try:
                input(colored("\nPress Enter To Continue.....",
                              'yellow', attrs=['blink']))
            except SyntaxError:
                pass

        elif choice == 4:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "DNS LOOKUP", font="slant"), 'blue', attrs=['bold'])
            print(font)

            while 1:
                print(colored("TARGET (URL) >> ", 'red', attrs=['bold']))
                url = prompt()
                break
            dnslookup(url)
            try:
                input(colored("\nPress Enter To Continue.....",
                              'yellow', attrs=['blink']))
            except SyntaxError:
                pass

        elif choice == 5:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "SCAN", font="slant"), 'blue', attrs=['bold'])
            print(font)

            while 1:
                print(colored("TARGET (URL/IP) >> ", 'red', attrs=['bold']))
                nmap_inp = prompt()
                break
            nmap(nmap_inp)
            try:
                input(colored("\nPress Enter To Continue.....",
                              'yellow', attrs=['blink']))
            except SyntaxError:
                pass

        elif choice == 6:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "NS LOOKUP", font="slant"), 'blue', attrs=['bold'])
            print(font)

            while 1:
                print(colored("TARGET (URL) >> ", 'red', attrs=['bold']))
                ns_inp = prompt()
                break
            nslookup(ns_inp)
            try:
                input(colored("\nPress Enter To Continue.....",
                              'yellow', attrs=['blink']))
            except SyntaxError:
                pass

        elif choice == 7:
            os.system('clear')
            font = colored(pyfiglet.figlet_format(
                "GEO INFO", font="slant"), 'blue', attrs=['bold'])
            print(font)

            while 1:
                print(colored("TARGET (IP) >> ", 'red', attrs=['bold']))
                inp = prompt()
                break
            geo_ip(inp)
            try:
                input(colored("\nPress Enter To Continue.....",
                              'yellow', attrs=['blink']))
            except SyntaxError:
                pass

        elif choice == 8:
            os.system('clear')
            print(colored(start(), attrs=['bold']))

        elif choice == 0:
            os.system('clear')
            exit(0)

try:
    os.system('clear')
    project()

except KeyboardInterrupt:
    os.system('clear')
    quit("")

#!/usr/bin/python3.7


import os
import sys
import pyfiglet
from termcolor import colored


def begin():
    font = colored(pyfiglet.figlet_format(
        "DG^2N", font='slant'), 'red', attrs=['bold'])
    print (font)


    return("\nENTER YOUR CHOICE\n1.Reconnaissance\t\tFor information gathering of websites\n2.WiFi-Hacking\t\t\tFor hacking & cracking wifi\n\n0.EXIT\t\t\t\tExit")


def main():
    while 1:
        print(colored(begin(), attrs=['bold']))
        print (colored('\n\n[Enter 5 for Main Menu]', 'cyan', attrs=['bold']))

        user_input = input(
            colored('Enter Your Choice >> ', 'blue', attrs=['bold']))

        if len(user_input) != 1:
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
            while 1:
                pwd = os.getcwd()
                os.system("$pwd ./reconnaissance.py")
                break
            continue

        elif choice == 2:
            os.system('clear')
            while 1:
                os.system("$pwd ./mon.py")
                break
            continue

        elif choice == 5:
            os.system('clear')
          

        elif choice == 0:
            os.system('clear')
            exit(colored(pyfiglet.figlet_format(
                '\nBye , See u again..............', font="slant"), 'magenta', attrs=['bold']))


try:
    os.system('clear')
    main()
except KeyboardInterrupt:
    os.system('clear')
    quit("")

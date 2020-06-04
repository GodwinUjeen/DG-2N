# DG-N
A Simple Python Project for Information Gathering and  Aircrack-ng automation

The tool is made with Python 3.
It requires Sys, OS, Pyfiglet, Termcolor modules

You can install the requirements by using the requirements.txt

python3 -m pip install -r requirements.txt

You will get 2 options in the main menu 
            1. Reconainsance
            2. Wifi-Hacking

If you r using kali inux you will have a inbuilt xfce-terminal and Aircrack-ng... which is required in wifi hacking.

In Reconaissance(For Information Gathering) you will get 7 options

1. IP                Enumerate  information  from  IP Address
2. URL               Gather  information  about given Website
3. WHOIS             Gather domain  registration  information
4. DNS LOOKUP        Map DNS  records associated  with target
5. NMAP              Performs NMAP scan on the target(for discovering ports)
6. NS LOOKUP         Obtain domain name or IP address mapping
7. GEO LOCATION      Gives the location of the IP Address

Enter Your Shodan api in the ip.py file 
api = shodan.Shodan("Your api here")

In Wifi Hacking You can Just use that just like normal Aircrack tool.
The difference is here you want only to type only the required details.. Not the entire Commands.
At last the password will be saved in a txt file.
The Network Interface will be broughtback after the completion of the process.



This tool was developed by Godwin.U and Godwin Joy for our Mini Project in our 2nd Year
          

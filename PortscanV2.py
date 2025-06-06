import pyfiglet 
import sys
import os
import socket
from datetime import datetime
import importlib
from pystyle import Colors, Colorate, Center

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[1;34m'
    RESET = '\033[0m'

os.system("title 777 PORT SCANNER │ V2 │ PRIVATE VERSION")
target = input(bcolors.BLUE + "Ip To Scan > ")

os.system("cls")
 
print(bcolors.BLUE + "Scanning: " + target)  
print(bcolors.BLUE + "Scanning started at: " + str(datetime.now()))
print("\n")  
print(bcolors.BLUE + "This May Take A While...")  
print(bcolors.BLUE + "_" * 50)  

try:
    for port in range(1, 65536):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Print open port
        result = s.connect_ex((target, port))
        if result == 0:
            print(bcolors.BLUE + "[!] Port {} is open".format(port))  
        s.close()

except KeyboardInterrupt:
    print(bcolors.RESET + "\nExiting :(")  
    sys.exit()

except socket.error:
    print(bcolors.RED + "Host not responding :O")  
    sys.exit()

if exit:
    print(bcolors.RESET + 'Goodbye')

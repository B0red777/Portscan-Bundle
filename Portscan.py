import socket
import whois
import requests
import ipaddress
import subprocess
import time
import sys
import os
import platform
from scapy.all import *
from termcolor import colored
from tqdm import tqdm
from colorama import Fore, init
from pystyle import Colors, Colorate, Center

init(autoreset=True)

black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"

os.system("title 777 PORT SCAN │ V1 │ PRIVATE VERSION")

def scan_ports(ip, ports=[21, 22, 25, 53, 80, 443, 3306, 8080]):
    open_ports = []
    for port in tqdm(ports, desc=colored("Scanning Ports", "yellow")):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def get_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None

def get_whois(ip):
    try:
        return whois.whois(ip)
    except:
        return "WHOIS information not available"

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "No DNS associated"

def traceroute_ip(ip):
    if platform.system() == "Windows":
        command = ["tracert", ip]
    else:
        command = ["traceroute", ip]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return "Traceroute command not found on this system"

def check_vulns(ip, open_ports):
    vulns = {}
    for port in open_ports:
        if port == 21:
            vulns[port] = "FTP: Check for anonymous login (CVE-XXXX)"
        elif port == 22:
            vulns[port] = "SSH: Check for brute-force and outdated versions"
        elif port in [80, 443]:
            vulns[port] = "HTTP/HTTPS: Scan with Nikto"
        elif port == 3306:
            vulns[port] = "MySQL: Check for root access without password"
    return vulns

def save_results(ip, open_ports, banners, whois_info, dns, traceroute, vulns):
    filename = f"result {ip}.txt"
    with open(filename, "w") as f:
        f.write(f"Scanning Results for {ip}\n\n")
        f.write(f"Open Ports: {open_ports}\n\n")
        for port, banner in banners.items():
            f.write(f"Banner on {port}: {banner}\n")
        f.write(f"\nWHOIS Information:\n{whois_info}\n")
        f.write(f"\nReverse DNS: {dns}\n")
        f.write(f"\nTraceroute:\n{traceroute}\n")
        f.write(f"\nVulnerabilities:\n{vulns}\n")
    print(colored(f"Results saved to {filename}", "green"))

def loading_animation(text, duration=3):
    print(colored(text, "yellow"), end="", flush=True)
    for _ in range(duration):
        time.sleep(1)
        print(colored(".", "yellow"), end="", flush=True)
    print()

def main(ip):
    if not ipaddress.ip_address(ip):
        print(colored("Invalid IP address", "blue"))
        return
    
    loading_animation("\nInitializing scan")
    open_ports = scan_ports(ip)
    print(colored(f"\nOpen ports:\n{open_ports}\n", "blue"))
    
    banners = {}
    for port in open_ports:
        banner = get_banner(ip, port)
        if banner:
            bannersport = banner
            print(colored(f"Banner on {port}: {banner}\n", "blue"))
    
    whois_info = get_whois(ip)
    print(colored("WHOIS Information:", "blue"))
    print(whois_info)
    
    dns = reverse_dns(ip)
    print(colored("\nReverse DNS:", "blue"))
    print(dns)
    
    traceroute = traceroute_ip(ip)
    print(colored("\nTraceroute:", "blue"))
    print(traceroute)
    
    vulns = check_vulns(ip, open_ports)
    print(colored("\nVulnerability Check:", "blue"))
    vulns = Center.XCenter(vulns)
    print(vulns)
    
    print(colored("""\n                                               ┌─────────────────────────────┐
                                               │ Saving Results To Directory │
                                               └─────────────────────────────┘
""", "blue"))
    time.sleep(5)
    
    save_results(ip, open_ports, banners, whois_info, dns, traceroute, vulns)

if __name__ == "__main__":
    os.system('cls')
    
    print(Fore.BLUE + '''
                                            ███████╗███████╗███████╗                    
                                            ╚════██║╚════██║╚════██║                    
                                                ██╔╝    ██╔╝    ██╔╝                    
                                               ██╔╝    ██╔╝    ██╔╝                     
                                               ██║     ██║     ██║                      
                                               ╚═╝     ╚═╝     ╚═╝                      
                                                            
		                                 Made By Bored <3
                                                  .gg/byrdegEPXY
                                                            
    ''')
    
    target_ip  = input(f"{Fore.BLUE} [{Fore.LIGHTWHITE_EX}+{Fore.BLUE}]{Fore.LIGHTWHITE_EX} {Fore.BLUE}Enter IP To Lookup > ")
    main(target_ip)
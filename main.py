from time import sleep
import os

def in_sudo_mode():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()
        
def main():
    ps = input("enter packet size (enter 0 for maximum) >>> ")
    sleep(1)
    ip = input("enter ip address >>> ")
    os.system("nmap {ip}")
    sleep(1)
    if ps == "0":
        os.system("ping -s 65507 -f {ip}")    
    else:
        os.system("ping -s {ps} -f {ip}")
        
        
if __name__ == "main":
    main()

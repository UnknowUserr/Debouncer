import subprocess, time, win32console
from sys import executable

"""
--------------------@XeroxOnTop-------------------

Date of releases : 27/11/2022
Original creator : https://github.com/XeroxOnTop

--------------------@XeroxOnTop-------------------
"""

requirements = [
    ["colorama", "colorama"],
    ["pystyle", "pystyle"],
    ["phonenumbers", "phonenumbers"]
]

for module in requirements:
    try: __import__(module[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {module[1]}", shell=True)
        time.sleep(3)

win32console.SetConsoleTitle("Debouncer ~ @XeroxOnTop")

xerox = r"""

              _.===========================._
            .'`  .-  - __- - - -- --__--- -.  `'.
        __ / ,'`     _|--|_________|--|_     `'. \
      /'--| ;    _.'\ |  '         '  | /'._    ; |
     //   | |_.-' .-'.'    -  -- -    '.'-. '-._| |
    (\)   \"` _.-` /                     \ `-._ `"/
    (\)    `-`    /      .---------.      \    `-`
    (\)           |      ||1||2||3||      |
   (\)            |      ||4||5||6||      |
  (\)             |      ||7||8||9||      |
 (\)           ___|      ||*||0||#||     |
 (\)          /.--|      '---------'      |
  (\)        (\)  |\_  _  __   _   __  __/|
 (\)        (\)   |                       |
(\)_._._.__(\)    |                       |
 (\\\\\\\\\)      '.___________________.'
  '-'-'-'--'

"""[1:].replace('m','0')

from pystyle import Anime, Colors, Center, Colorate
from colorama import Fore

Anime.Fade(text=Center.Center(xerox), color=Colors.black_to_green, mode=Colorate.Vertical, time=2)

print(Center.XCenter("Debouncer ~ @XeroxOnTop"))
print(Fore.LIGHTBLACK_EX + "[+] License : MIT License" + Fore.RESET)

import os, threading, json, phonenumbers, time, subprocess, win32console
from random import choice
from json import loads
from phonenumbers import geocoder, carrier

def leT():
    let = input("\n\n[?] Threads : ")
    XeroxOnTop = open('config.json', 'w')
    dikt = {
    "Threads"  : f"{let}"
}
    json_string = json.dumps(dikt)
    XeroxOnTop.write(json_string)

def Main():
        while True : 

            t = "+337"+"".join(choice("3698521470") for x in range(8))
            os.makedirs("Results/",exist_ok=True)
            y = phonenumbers.parse(t)

            if phonenumbers.is_valid_number(y):
                LeFournisseur = carrier.name_for_number(y, 'fr')
                LePaysDeFou = geocoder.description_for_number(y, "fr")
                print(f"{Fore.GREEN}[+] {Fore.RESET}" + f"Valid   : {t}")
                with open(f"Results/" + f"{LeFournisseur}.txt" , 'a+') as file :
                    file.write(t + '\n')
                    file.close()
            else: 
                print(f"{Fore.RED}[-] {Fore.RESET}" + f"Invalid : {t}")

check = loads(open('config.json', 'r').read())
thread = check['Threads']

if __name__ == '__main__':
    leT()
    for i in range(int(thread)):
        th = threading.Thread(target=Main)
        th.start()

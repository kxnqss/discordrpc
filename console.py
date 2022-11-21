import os 
import sys 
import psutil
import time
import requests
import webbrowser
from pystyle import *
from colorama import *

class appsettings():
    usingwrite = False

class logos: 
    discordrpclogo = """

 /$$$$$$$  /$$                                               /$$ /$$$$$$$  /$$$$$$$   /$$$$$$ 
| $$__  $$|__/                                              | $$| $$__  $$| $$__  $$ /$$__  $$
| $$  \ $$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/
| $$  | $$| $$ /$$_____/ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$| $$$$$$$/| $$$$$$$/| $$      
| $$  | $$| $$|  $$$$$$ | $$      | $$  \ $$| $$  \__/| $$  | $$| $$__  $$| $$____/ | $$      
| $$  | $$| $$ \____  $$| $$      | $$  | $$| $$      | $$  | $$| $$  \ $$| $$      | $$    $$
| $$$$$$$/| $$ /$$$$$$$/|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$| $$  | $$| $$      |  $$$$$$/
|_______/ |__/|_______/  \_______/ \______/ |__/       \_______/|__/  |__/|__/       \______/ 
                                                                                              
        """

    help = """

                                           /$$       /$$                 /$$          
                                          /$$/      | $$                | $$          
  /$$$$$$   /$$$$$$   /$$$$$$$           /$$/       | $$$$$$$   /$$$$$$ | $$  /$$$$$$ 
 /$$__  $$ /$$__  $$ /$$_____/          /$$/        | $$__  $$ /$$__  $$| $$ /$$__  $$
| $$  \__/| $$  \ $$| $$               /$$/         | $$  \ $$| $$$$$$$$| $$| $$  \ $$
| $$      | $$  | $$| $$              /$$/          | $$  | $$| $$_____/| $$| $$  | $$
| $$      | $$$$$$$/|  $$$$$$$       /$$/           | $$  | $$|  $$$$$$$| $$| $$$$$$$/
|__/      | $$____/  \_______/      |__/            |__/  |__/ \_______/|__/| $$____/ 
          | $$                                                              | $$      
          | $$                                                              | $$      
          |__/                                                              |__/      
          
"""    

def write(phrase, speed):
    if appsettings.usingwrite == False: 
        phraseBackspace = phrase.replace("\n", "")
        print(phraseBackspace)
    else: 
        for char in phrase:
            time.sleep(speed)
            sys.stdout.write(char)
            sys.stdout.flush()  

github = "https://github.com/Kingssxd/discordrpc"    
bs = 0.0000000000001
version = 2.1
verifiedsymbol = "✓"
currentuser = os.getlogin()
kingss = Colorate.Horizontal(Colors.blue_to_purple, "Kingss", 2)
user = Colorate.Horizontal(Colors.blue_to_purple, f"{currentuser}", 2)

nodefile = "node.exe"
currentdirectory = os.getcwd()

if appsettings.usingwrite == True:
    os.system("title DiscordRPC")
else: 
    os.system("title D")
    time.sleep(bs)
    os.system("title Di")
    time.sleep(bs)
    os.system("title Dis")
    time.sleep(bs)
    os.system("title Disc")
    time.sleep(bs)
    os.system("title Disco")
    time.sleep(bs)
    os.system("title Discor")
    time.sleep(bs)
    os.system("title Discord")
    time.sleep(bs)
    os.system("title DiscordR")
    time.sleep(bs)
    os.system("title DiscordRP")
    time.sleep(bs)
    os.system("title DiscordRPC")

class commands(): 
    launch = "launch"
    configure = "config"
    help = "help"
    invisiblelaunch = "invislaunch"
    stop = "stop"
    library = "libinstall"
    github = "github"
    settings = "settings"
    update = "update"

def settings(): 
    os.system("cls")
    write(Fore.WHITE + "Ready for some configuration?", bs)
    time.sleep(1)
    os.system("notepad settings.py")
    input(Fore.WHITE + "\nPress enter to continue")
    main()    

def githubi(): 
    os.system("cls")
    write(Fore.WHITE + f"GitHub: {github}", bs)
    write(Fore.WHITE + "\nPress 1 to open link, press enter to cotinue.", bs)
    choice = input("\n > ")
    if int(choice) == 1:
        os.system(f"start \"\" {github}")
        main()
    else: 
        time.sleep(0.1)
        main()
    
def libinstall(): 
    print(" ")
    os.system("title DiscordRPC ^| Installing libraries")
    os.system("pip install psutil")
    os.system("pip install pystyle")
    os.system("pip install colorama")
    time.sleep(3)
    main()

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def stopinvis(): 
    print(" ")
    stopping = (Colorate.Horizontal(Colors.purple_to_blue, "Stopping...", 2))
    write(Fore.WHITE + f"» [{Fore.GREEN}❌{Fore.WHITE}] {stopping}", bs)
    for proc in psutil.process_iter():
        if proc.name() == nodefile:
            proc.kill()
    time.sleep(1)
    main()

def invislaunch(): 
    script = currentdirectory + "\invisible.vbs"
    invisrunbatch = currentdirectory + "\invisrun.bat"
    launching = (Colorate.Horizontal(Colors.purple_to_blue, "Invis Launching...", 2))
    print(" ")
    write(Fore.WHITE + f"» [{Fore.GREEN}{verifiedsymbol}{Fore.WHITE}] {launching}", bs)
    os.system(f"wscript.exe {script} {invisrunbatch}")
    time.sleep(3)
    main()

def configure(): 
    print(" ")
    text = (Colorate.Horizontal(Colors.purple_to_blue, "configuration?", 2))
    write(Fore.WHITE + f"» [⚙️] Ready for some {text}", bs)
    time.sleep(1)
    os.system("notepad discordrpc.js")
    time.sleep(1)
    main()

def helpfnc():
    os.system("cls")
    launch = (Colorate.Horizontal(Colors.purple_to_blue, "launch:", 2))
    configure = (Colorate.Horizontal(Colors.purple_to_blue, "config:", 2))
    invislaunch = (Colorate.Horizontal(Colors.purple_to_blue, "invislaunch:", 2))
    stop = (Colorate.Horizontal(Colors.purple_to_blue, "stop:", 2))
    libinstall = (Colorate.Horizontal(Colors.purple_to_blue, "libinstall:", 2))
    github = (Colorate.Horizontal(Colors.purple_to_blue, "github:", 2))
    print(Colorate.Vertical(Colors.purple_to_blue, logos.help, 2))
    write(Fore.RESET + f"[{Fore.CYAN}-{Fore.WHITE}] Here's a command list for you! ^^", bs)
    print(" ")
    write(Fore.RESET + f"» {launch}{Fore.RESET} Launches the DiscordRPC, giving it to life!", bs)
    write(Fore.RESET+ f"» {configure}{Fore.RESET} Configures the DiscordRPC, give it a personality!", bs)
    write(Fore.RESET + f"» {invislaunch}{Fore.RESET} launch the program with no cmd, in background!", bs)
    write(Fore.RESET + f"» {stop}{Fore.RESET} quit running cmd in background", bs)
    write(Fore.RESET + f"» {libinstall}{Fore.RESET} install required python libraries", bs)
    write(Fore.RESET + f"» {github}{Fore.RESET} open DiscordRPC github repository", bs)
    print(" ")
    input(Fore.RESET + f"[{Fore.RED}!{Fore.WHITE}] Waiting for enter key..")
    main()

def launch():
    launching = (Colorate.Horizontal(Colors.purple_to_blue, "Launching...", 2))
    stop = (Colorate.Horizontal(Colors.purple_to_blue, "stop!", 2))
    os.system("cls")
    print(Colorate.Vertical(Colors.purple_to_blue, logos.discordrpclogo, 2))
    write(Fore.WHITE + f"» [{Fore.CYAN}-{Fore.WHITE}] Welcome to DiscordRPC! Here you can customize your discord profile with whatever you want! ^^", bs)
    write(Fore.WHITE + f"\n» [{Fore.GREEN}{verifiedsymbol}{Fore.WHITE}] RPC Status: " + Colorate.Horizontal(Colors.blue_to_purple, "Running", 2), bs)
    write(Fore.WHITE + f"\n» [{Fore.CYAN}-{Fore.WHITE}] Current version: " + Colorate.Horizontal(Colors.blue_to_purple, str(version), 2), bs)
    write(Fore.WHITE + f"\n» [{Fore.GREEN}?{Fore.WHITE}] Don't know what to do? Run " + Colorate.Horizontal(Colors.blue_to_purple, "help", 2), bs)
    write(Fore.WHITE + "\n» [" +  Colorate.Horizontal(Colors.blue_to_purple, "♥", 2) + f"] {Fore.WHITE}by {kingss}{Fore.WHITE} for {user}", bs)  
    print(" ")
    write(Colorate.Horizontal(Colors.blue_to_purple, "rpc » ", 2) + Fore.WHITE + "launch", bs)
    time.sleep(0.5)
    try: 
        print(" ")
        write(Fore.WHITE + f"» [{Fore.GREEN}{verifiedsymbol}{Fore.WHITE}] {launching}", bs)
        write(Fore.WHITE + f"» [{Fore.GREEN}⚙️{Fore.WHITE}] Press CTRL + C to {stop}", bs)
        os.system("node discordrpc.js")
        write(Fore.LIGHTBLUE_EX + "\nFailed to launch.", bs)
        input(Fore.LIGHTBLUE_EX + "Press enter to continue")
        time.sleep(0.5)
        main()
    except:
        main()

def consoleMain():
    if commandline == commands.help:
        helpfnc()
    if commandline == commands.stop: 
        stopinvis()
    if commandline == commands.library: 
        libinstall()     
    if commandline == commands.launch: 
        launch()         
    if commandline == commands.github: 
        githubi()
    if commandline == commands.settings:
        settings()
    if commandline == commands.configure:
        configure() 
    if commandline == commands.invisiblelaunch:
        invislaunch()                             
    else:
        print(" ")
        write((Colorate.Horizontal(Colors.purple_to_blue, "This command doesn't exist", 2)), bs)
        time.sleep(1)
        main()    

def main():
    os.system("cls")
    os.system("title DiscordRPC")
    global commandline
    print(Colorate.Vertical(Colors.purple_to_blue, logos.discordrpclogo, 2))
    write(Fore.WHITE + f"» [{Fore.CYAN}-{Fore.WHITE}] Welcome to DiscordRPC! Here you can customize your discord profile with whatever you want! ^^", bs)
    if checkIfProcessRunning("node.exe"):
        write(Fore.WHITE + f"\n» [{Fore.GREEN}{verifiedsymbol}{Fore.WHITE}] RPC Status: " + Colorate.Horizontal(Colors.blue_to_purple, "Running", 2), bs)
    else:
        write(Fore.WHITE + f"\n» [{Fore.RED}❌{Fore.WHITE}] RPC Status: " + Colorate.Horizontal(Colors.blue_to_purple, "Offline", 2), bs) 
    write(Fore.WHITE + f"\n» [{Fore.CYAN}-{Fore.WHITE}] Current version: " + Colorate.Horizontal(Colors.blue_to_purple, str(version), 2), bs)
    write(Fore.WHITE + f"\n» [{Fore.GREEN}?{Fore.WHITE}] Don't know what to do? Run " + Colorate.Horizontal(Colors.blue_to_purple, "help", 2), bs)
    write(Fore.WHITE + "\n» [" +  Colorate.Horizontal(Colors.blue_to_purple, "♥", 2) + f"] {Fore.WHITE}by {kingss}{Fore.WHITE} for {user}", bs)
    if appsettings.usingwrite == False: 
        print(" ")
    else: 
        print(" ")
        print(" ")
    commandline = input(Colorate.Horizontal(Colors.blue_to_purple, "rpc » ", 2) + Fore.WHITE)    
    consoleMain()    

main()
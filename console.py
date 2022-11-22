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
    disdeveloperportal = "devportal"
    update = "update"
    

def developerPortal(): 
    devportalUrl = "https://discord.com/developers/applications"
    print(" ")
    text = (Colorate.Horizontal(Colors.purple_to_blue, "Discord Developer Portal: ", 2))
    write(Fore.RESET + f"[{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] {text}: {devportalUrl}", bs)
    print(Fore.RESET + f"[{Fore.RED}!{Fore.RESET}] Waiting for any key..")
    os.system("pause > nul")
    main()
    
def settings(): 
    print(" ")
    text = (Colorate.Horizontal(Colors.purple_to_blue, "configuration?", 2))
    usingWriteSetting = (Colorate.Horizontal(Colors.purple_to_blue, "using-write: ", 2))
    write(Fore.RESET + f"» [{Fore.GREEN}⚙️{Fore.RESET}] Ready for some {text}{Fore.RESET}", bs)
    time.sleep(0.2)
    write(Fore.RESET + f"{Fore.RESET}» [{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] Current Settings:", bs)
    write(Fore.RESET + f"» [{Fore.CYAN}-{Fore.RESET}] {usingWriteSetting}{Fore.RESET}{appsettings.usingwrite}", bs)
    print(Fore.RESET + f"» [{Fore.RED}!{Fore.RESET}] Waiting for any key..")
    os.system("pause > nul")
    main() 

def githubi(): 
    print(" ")
    text = (Colorate.Horizontal(Colors.purple_to_blue, "GitHub: ", 2))
    n1 = (Colorate.Horizontal(Colors.purple_to_blue, "1", 2))
    write(Fore.RESET + f"[{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] {text}: {github}", bs)
    print(Fore.RESET + f"[{Fore.RED}!{Fore.RESET}] Waiting for any key..")
    os.system("pause > nul")
    main()
    
def libinstall(): 
    print(" ")
    text = (Colorate.Horizontal(Colors.purple_to_blue, "» Installing libraries...", 2))
    write(Fore.RESET + f"[{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] {text}{Fore.RESET}", bs)
    write(f"{Fore.RESET}--------------------------------------------------------------------------------", bs)
    os.system("pip install psutil")
    os.system("py -m pip install psutil")
    os.system("pip install pystyle")
    os.system("py -m pip install pystyle")
    os.system("pip install colorama")
    os.system("py -m pip install colorama")
    write(f"{Fore.RESET}--------------------------------------------------------------------------------", bs)
    time.sleep(1)
    print(Fore.RESET + f"[{Fore.RED}!{Fore.RESET}] Waiting for any key..")
    os.system("pause > nul")
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
    write(Fore.RESET + f"» [{Fore.GREEN}❌{Fore.RESET}] {stopping}", bs)
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
    write(Fore.RESET + f"» [{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] {launching}", bs)
    os.system(f"wscript.exe {script} {invisrunbatch}")
    time.sleep(3)
    main()

def configure(): 
    print(" ")
    text = (Colorate.Horizontal(Colors.purple_to_blue, "configuration?", 2))
    applicationIDtext = (Colorate.Horizontal(Colors.purple_to_blue, "ApplicationID: ", 2))
    detailscontentText = (Colorate.Horizontal(Colors.purple_to_blue, "Details Content: ", 2))
    largeimgText = (Colorate.Horizontal(Colors.purple_to_blue, "Large Image: ", 2))
    largetextText = (Colorate.Horizontal(Colors.purple_to_blue, "Large Text: ", 2))
    button1Texttext = (Colorate.Horizontal(Colors.purple_to_blue, "Button 1 Text: ", 2))
    button1Urltext = (Colorate.Horizontal(Colors.purple_to_blue, "Button 1 URL: ", 2))
    write(Fore.RESET + f"» [⚙️] Ready for some {text}{Fore.RESET}", bs)
    print(" ")
    write(Fore.RESET + f"» {applicationIDtext}{Fore.RESET} Your application ID, you can get it at discord dev portal", bs)
    write(Fore.RESET + f"» {detailscontentText}{Fore.RESET} Your description", bs)
    write(Fore.RESET + f"» {largeimgText}{Fore.RESET} Your image (must be uploaded to your application resources)", bs)
    write(Fore.RESET + f"» {largetextText}{Fore.RESET} Your text", bs)
    write(Fore.RESET + f"» {button1Texttext}{Fore.RESET} The text of your button", bs)
    write(Fore.RESET + f"» {button1Urltext}{Fore.RESET} The link of your button", bs)
    print(" ")
    time.sleep(1.2)
    os.system("notepad discordrpc.js")
    print(Fore.RESET + f"[{Fore.RED}!{Fore.RESET}] Waiting for any key..")
    os.system("pause > nul")
    main()

def helpfnc():
    os.system("cls")
    launch = (Colorate.Horizontal(Colors.purple_to_blue, "launch:", 2))
    configure = (Colorate.Horizontal(Colors.purple_to_blue, "config:", 2))
    invislaunch = (Colorate.Horizontal(Colors.purple_to_blue, "invislaunch:", 2))
    stop = (Colorate.Horizontal(Colors.purple_to_blue, "stop:", 2))
    libinstall = (Colorate.Horizontal(Colors.purple_to_blue, "libinstall:", 2))
    devportal = (Colorate.Horizontal(Colors.purple_to_blue, "devportal:", 2))
    github = (Colorate.Horizontal(Colors.purple_to_blue, "github:", 2))
    print(Colorate.Vertical(Colors.purple_to_blue, logos.help, 2))
    write(Fore.RESET + f"[{Fore.CYAN}-{Fore.RESET}] Here's a command list for you! ^^", bs)
    print(" ")
    write(Fore.RESET + f"» {launch}{Fore.RESET} Launches the DiscordRPC, giving it to life!", bs)
    write(Fore.RESET+ f"» {configure}{Fore.RESET} Configures the DiscordRPC, give it a personality!", bs)
    write(Fore.RESET + f"» {invislaunch}{Fore.RESET} launch the program with no cmd, in background!", bs)
    write(Fore.RESET + f"» {stop}{Fore.RESET} quit running cmd in background", bs)
    write(Fore.RESET + f"» {libinstall}{Fore.RESET} install required python libraries", bs)
    write(Fore.RESET + f"» {devportal}{Fore.RESET} open discord developer portal", bs)
    write(Fore.RESET + f"» {github}{Fore.RESET} open DiscordRPC github repository", bs)
    print(" ")
    print(Fore.RESET + f"[{Fore.RED}!{Fore.RESET}] Waiting for any key..")
    os.system("pause > nul")
    main()

def launch():
    launching = (Colorate.Horizontal(Colors.purple_to_blue, "Launching...", 2))
    stop = (Colorate.Horizontal(Colors.purple_to_blue, "stop!", 2))
    os.system("cls")
    print(Colorate.Vertical(Colors.purple_to_blue, logos.discordrpclogo, 2))
    write(Fore.RESET + f"» [{Fore.CYAN}-{Fore.RESET}] Welcome to DiscordRPC! Here you can customize your discord profile with whatever you want! ^^", bs)
    write(Fore.RESET + f"\n» [{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] RPC Status: " + Colorate.Horizontal(Colors.blue_to_purple, "Running", 2), bs)
    write(Fore.RESET + f"\n» [{Fore.CYAN}-{Fore.RESET}] Current version: " + Colorate.Horizontal(Colors.blue_to_purple, str(version), 2), bs)
    write(Fore.RESET + f"\n» [{Fore.GREEN}?{Fore.RESET}] Don't know what to do? Run " + Colorate.Horizontal(Colors.blue_to_purple, "help", 2), bs)
    write(Fore.RESET + "\n» [" +  Colorate.Horizontal(Colors.blue_to_purple, "♥", 2) + f"] {Fore.RESET}by {kingss}{Fore.RESET} for {user}", bs)  
    print(" ")
    write(Colorate.Horizontal(Colors.blue_to_purple, "rpc » ", 2) + Fore.RESET + "launch", bs)
    time.sleep(0.5)
    try: 
        print(" ")
        write(Fore.RESET + f"» [{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] {launching}", bs)
        write(Fore.RESET + f"» [{Fore.GREEN}⚙️{Fore.RESET}] Press CTRL + C to {stop}", bs)
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
    if commandline == commands.disdeveloperportal:
        developerPortal()
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
    write(Fore.RESET + f"» [{Fore.CYAN}-{Fore.RESET}] Welcome to DiscordRPC! Here you can customize your discord profile with whatever you want! ^^", bs)
    if checkIfProcessRunning("node.exe"):
        write(Fore.RESET + f"\n» [{Fore.GREEN}{verifiedsymbol}{Fore.RESET}] RPC Status: " + Colorate.Horizontal(Colors.blue_to_purple, "Running", 2), bs)
    else:
        write(Fore.RESET + f"\n» [{Fore.RED}❌{Fore.RESET}] RPC Status: " + Colorate.Horizontal(Colors.blue_to_purple, "Offline", 2), bs) 
    write(Fore.RESET + f"\n» [{Fore.CYAN}-{Fore.RESET}] Current version: " + Colorate.Horizontal(Colors.blue_to_purple, str(version), 2), bs)
    write(Fore.RESET + f"\n» [{Fore.GREEN}?{Fore.RESET}] Don't know what to do? Run " + Colorate.Horizontal(Colors.blue_to_purple, "help", 2), bs)
    write(Fore.RESET + "\n» [" +  Colorate.Horizontal(Colors.blue_to_purple, "♥", 2) + f"] {Fore.RESET}by {kingss}{Fore.RESET} for {user}", bs)
    if appsettings.usingwrite == False: 
        print(" ")
    else: 
        print(" ")
        print(" ")
    commandline = input(Colorate.Horizontal(Colors.blue_to_purple, "rpc » ", 2) + Fore.RESET)    
    consoleMain()    

main()
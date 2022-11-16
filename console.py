import os 
import sys 
import psutil
import logo
import time

def write(phrase, speed):
    for char in phrase:
      time.sleep(speed)
      sys.stdout.write(char)
      sys.stdout.flush()  

BYELLOW = '\033[93m'
GREEN  = '\33[92m'
RED = '\33[32m'
CBLUE   = '\33[94m'
bs = 0.000000001

nodefile = "node.exe"
currentdirectory = os.getcwd()

os.system("title DiscordRPC")

class commands(): 
    launch = "launch"
    configure = "configure"
    help = "help"
    invisiblelaunch = "invislaunch"
    stop = "stop"


def stopinvis(): 
    for proc in psutil.process_iter():
        if proc.name() == nodefile:
            proc.kill()
    time.sleep(2)
    main()

def invislaunch(): 
    invisiblepath = currentdirectory + "\invisible.vbs"
    invisrunbatch = currentdirectory + "\invisrun.bat"
    os.system("cls")
    print(CBLUE + logo.logos.invislaunch)
    write(BYELLOW + "Launching....", bs)
    os.system("wscript.exe " + invisiblepath +  " " + invisrunbatch)
    time.sleep(3)
    main()

def configure(): 
    os.system("cls")
    print(CBLUE + logo.logos.configure)
    write(BYELLOW + "Ready for some configuration?", bs)
    time.sleep(2)
    os.system("notepad index.js")
    input(BYELLOW + "Press enter to continue")
    main()
    
def helpfnc():
    os.system("cls")
    print(CBLUE + logo.logos.help)
    write(BYELLOW + "Here's a command list for you! ^^", bs)
    print(" ")
    write(CBLUE + "\n- launch: Launches the DiscordRPC, giving it to life!", bs)
    write(CBLUE + "\n- configure: Configures the DiscordRPC, give it a personality!", bs)
    write(CBLUE + "\n- invislaunch: launch the program with no cmd")
    print(" ")
    input(BYELLOW + "\nPress enter to continue:D")
    main()

def launch():
    os.system("cls")
    print(CBLUE + logo.logos.launch)
    write(BYELLOW + "Launching...", bs)
    time.sleep(1)
    try: 
        os.system("node discordrpc.js")
        write(CBLUE + "\nFailed to launch.", bs)
        input(CBLUE + "Press enter to continue")
        time.sleep(0.5)
        main()
    except:
        write(RED + "Something went wrong... Make sure to have done file configuration!", bs) 
        input()

def main():
    os.system("cls")
    global commandline
    print(CBLUE + logo.logos.discordrpclogo)
    write(BYELLOW + "Welcome to DiscordRPC! Here you can customize your discord profile with whatever you want! ^^", bs) 
    write(BYELLOW + "\nDon't know what to do? Run" + GREEN + " 'help'", bs)
    print(" ")
    print(" ")
    commandline = input(BYELLOW + "DiscordRPC > ")
    if commandline == commands.help:
        helpfnc()
    if commandline == commands.launch: 
        launch()
    if commandline == commands.configure:
        configure()
    if commandline == commands.invisiblelaunch:
        invislaunch()
    if commandline == commands.stop: 
        stopinvis()
    else:
        print("wrong command")
        time.sleep(1)
        main()        
    
main()
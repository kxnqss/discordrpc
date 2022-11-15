import os 
import sys 
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

os.system("title DiscordRPC")

class commands(): 
    launch = "launch"
    configure = "configure"
    help = "help"

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
    print(" ")
    input(BYELLOW + "\nPress enter to continue:D")
    main()

def launch():
    os.system("cls")
    print(CBLUE + logo.logos.launch)
    write(BYELLOW + "Launching...", bs)
    time.sleep(1)
    try: 
        os.system("node index.js")
        write(GREEN + "\nLaunched succesfully!", bs)
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
    else:
        print("wrong command")
        time.sleep(1)
        main()        
    
main()
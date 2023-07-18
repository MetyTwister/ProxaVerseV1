import tkinter as tk
import customtkinter as ctk
import subprocess
import time
import getpass
import sys
import tkinter.messagebox
import os
from multiprocessing import Process

os.system("clear")

print("     ____                            _    __                       _    __ ___")
print("    / __ \ _____ ____   _  __ ____ _| |  / /___   _____ _____ ___ | |  / /<  /")
print("   / /_/ // ___// __ \ | |/_// __ `/| | / // _ \ / ___// ___// _ \| | / / / /")
print("  / ____// /   / /_/ /_>  < / /_/ / | |/ //  __// /   (__  )/  __/| |/ / / /")
print(" /_/    /_/    \____//_/|_| \__,_/  |___/ \___//_/   /____/ \___/ |___/ /_/")
print("                                                                           ")




time.sleep(0.5)
pwd = getpass.getpass(prompt = "Enter password:")

if pwd != "admin":
    print("Access denied, closing soon!")
    time.sleep(1)
    print("You can now close this window.")
    sys.exit("EX1")

else:
    print("Access Granted!")
    print("")
    time.sleep(0.5)
    print("Select view mode:")
    print("")
    print("Terminal         ter")
    print("GUI              gui")
    InputMode = input("")

    if InputMode == "ter":
        print("terminal1")
        InputFruit = input("type your favourite fruit")
        print("your favourite fruit is: ", InputFruit)

    elif InputMode == "gui":
        os.system("/usr/local/bin/python3 /Users/Maty/Desktop/MATYHO/Pocitace/python/TkinterDemo/appGUI.py &")
        sys.exit("EX1")

    else:
        print("Invalid option!")
        sys.exit("EX1")
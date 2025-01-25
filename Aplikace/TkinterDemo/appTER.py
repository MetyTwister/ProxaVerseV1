#import tkinter as tk
#import customtkinter as ctk
import subprocess
import time
import getpass
import sys
import tkinter.messagebox
import os
from multiprocessing import Process
import requests

#For windows use hashed alternatives ex. (os.system("clear")).

def genName():
    response = requests.get("https://randomuser.me/api")

    first_name = response.json()["results"][0]["name"]["first"]
    last_name = response.json()["results"][0]["name"]["last"]

    os.system("clear")
    #os.system("cls")

    print(first_name + " " + last_name)

    #l = tk.Label(root, text = first_name + " " + last_name)
    #l.config(font =("Courier", 14))
    #l.pack()

os.system("clear")
#os.system("cls")

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
    sys.exit("EX1")

else:
    print("Access Granted!")
    print("")
    time.sleep(0.5)
    os.system("clear")
    #os.system("cls")

    while True:
        print("ProxaVerse Terminal - Type help to list all available commands")
        InputMode = input("")
        if InputMode == "ter":
            os.system("clear")
            #os.system("cls")
            time.sleep(1)
            print("Type gen to generate a random name or exit to quit the app!")

            while True:
                user_input = input("")
                print("")
                if user_input == "gen":
                    genName()
                elif user_input == "help":
                    print("gen - Generate a random name")
                    print("exit - Quit the application")
                    print("help - List all available commands")
                elif user_input == "exit":
                    os.system("clear")
                    #os.system("cls")
                    break
                else:
                    os.system("clear")
                    #os.system("cls")
                    print("Unknown command, try help to list all commands!")

        elif InputMode == "gui":
            subprocess.Popen(["python3", "/Users/miroslavbaloun/Documents/Matyho/ProxaVerseV1-main/Aplikace/TkinterDemo/appGUI.py"], start_new_session=True)
            #subprocess.Popen(["python3", "C:/Users/Maty/Desktop/MATYHO/Pocitace/ProxaVerseV1/Aplikace/TkinterDemo"], start_new_session=True)
            sys.exit("EX1")

        elif InputMode == "exit":
            os.system("clear")
            #os.system("cls")
            print("Are you sure you want to exit? (yes/no)")
            exit_conf = input("")
            while True:
                if exit_conf == "yes":
                    sys.exit("EX1")
                else:
                    break
        elif InputMode == "help":
            os.system("clear")
            #os.system("cls")
            print("gui - View app in GUI")
            print("ter - View app in terminal")
            print("exit - Quit the application")
            print("help - List all available commands")
            print("")

        else:
            os.system("clear")
            #os.system("cls")
            print("Invalid command!")
            print("")
        
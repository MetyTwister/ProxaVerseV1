import tkinter as tk
import customtkinter as ctk
import subprocess
import time
import getpass
import sys
import tkinter.messagebox
import os
import requests


root = ctk.CTk()

root.title("ProxaVerseV1")
#NEFUNGUJE-->root.iconbitmap("./pvico.ico")

#Velikost a pozice okna-->
#root.resizable(False, False)

window_width = 750
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")



#Tlačítko a funkce-->
def StartApp():
     subprocess.call("/Applications/Python 3.12/IDLE.app/Contents/MacOS/IDLE")

def ExitApp():
    out = tk.messagebox.askquestion('Prompt', 'Do you want to exit now?')
    if out == 'yes':
        sys.exit("EX1")

def genName():

    response = requests.get("https://randomuser.me/api")

    first_name = response.json()["results"][0]["name"]["first"]
    last_name = response.json()["results"][0]["name"]["last"]

    #os.system("clear")
    #os.system("cls")

    #print(first_name + " " + last_name)

    name = tk.Label(root, text = first_name + " " + last_name)
    name.config(font =("Courier", 14))
    name.place(relx=0.5, rely=0.2,anchor="center")
    name.pack()



Button1 = ctk.CTkButton(root, text="Gen app", command=genName)
Button1.place(relx=0.5, rely=0.7, anchor="center")

Button2 = ctk.CTkButton(root, text="Start App", command=StartApp)
Button2.place(relx=0.5, rely=0.8, anchor="center")

Button3 = ctk.CTkButton(root, text="Exit app", command=ExitApp)
Button3.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()
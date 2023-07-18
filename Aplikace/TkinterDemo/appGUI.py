import tkinter as tk
import customtkinter as ctk
import subprocess
import time
import getpass
import sys
import tkinter.messagebox



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
def StartWorkspace():
     subprocess.call('/Applications/Visual Studio Code.app/Contents/MacOS/Electron')

def ExitApp():
    out = tk.messagebox.askquestion('Prompt', 'Do you want to exit now?')
    if out == 'yes':
        sys.exit("EX1")


Button2 = ctk.CTkButton(root, text="Start Workspace", command=StartWorkspace)
Button2.place(relx=0.5, rely=0.8, anchor="center")

Button3 = ctk.CTkButton(root, text="Exit app", command=ExitApp)
Button3.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()
import subprocess
import tkinter as tk
from tkinter import *
import pyuac
from tkinter.messagebox import askyesno, askquestion
import customtkinter
import win32serviceutil

customtkinter.set_appearance_mode("Dark")
options = [] 

def GetPrinters():
    win32serviceutil.RestartService("Spooler", ".")
    data=subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')
    data=data[1:]
    for line in data:
        entries = []
        for printername in line.split("  "):
            if(printername!=""):
                entries.append(printername)
        # There is a universal truth where every printer will have a line that will always have 4 elements, and if not greater
        if(len(entries)==4):
            options.append(entries[0])
        if(len(entries)>4):
            options.append(entries[1])

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        GetPrinters()
        self.geometry( "500x150" ) 
        self.iconbitmap('OIP.ico')
        self.title("APOPrinter")
        # How to make custom font: custom_font =("Times",10,'bold')
        self.textbox =  customtkinter.CTkTextbox(self, width=450,height=50,text_color="#ffffff")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","Welcome to the APOTECA Printer Assistant, Please select the printer model you would like to fix")
        def optionmenu_callback(choice):
            self.qm = askyesno(title='Confirmation', message='Are you sure that you want to clear {}'.format(choice))
            if self.qm:
                # What is interesting is that even when we restart the service, and clear the queue, it doesnt finish the process to print the test page
                subprocess.run(r"Status.bat"+" "+ choice)
        self.dropbox = customtkinter.CTkOptionMenu(master=self , values=options , command=optionmenu_callback,button_color="#aa1c2d",button_hover_color="#ba747e",fg_color="#ffffff",text_color="#100c08") 
        self.textbox.pack()
        self.dropbox.pack(padx=20, pady=20) 

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
        app = App()
        app.mainloop()
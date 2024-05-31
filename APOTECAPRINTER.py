import subprocess
import tkinter as tk
from tkinter import *
import pyuac
from tkinter.messagebox import askyesno, askquestion
import customtkinter
# We set dark mode
customtkinter.set_appearance_mode("Dark")
# Dropdown menu options 
options = [] 

# This function allows us to acquire the list of printers
def GetPrinters():
    data=subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')
    #  We then ignore th first line
    data=data[1:]
    # This is the iterative loop which will allow us go through each line
    for line in data:
        # Each line will start with a fresh entry list
        entries = []
        # We then append the list with each entry in the line
        for printername in line.split("  "):
            if(printername!=""):
                entries.append(printername)
        # There is a universal truth where every printer will have a line that will always have 4 elements, and if not greater
        if(len(entries)==4):
            options.append(entries[0])
        if(len(entries)>4):
            options.append(entries[1])

# We set the App Class
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
            sol = choice
            confirmation(sol)
        self.dropbox = customtkinter.CTkOptionMenu(master=self , values=options , command=optionmenu_callback,button_color="#aa1c2d",button_hover_color="#ba747e",fg_color="#ffffff",text_color="#100c08") 

        self.textbox.pack()
        self.dropbox.pack(padx=20, pady=20) 

def confirmation(name):
    qm = askyesno(title='Confirmation', message='Are you sure that you want to clear {}'.format(name))
    if qm:
        subprocess.run(r"Status.bat"+" "+ name)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
        app = App()
        app.mainloop()
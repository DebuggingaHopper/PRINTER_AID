import subprocess
import tkinter as tk
from tkinter import *
import pywin32_system32
import pyuac
from tkinter.messagebox import askyesno, askquestion
import customtkinter
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


def main():
    # We initialize the options list
    GetPrinters()
    # We create the root tkinter object
    root = customtkinter.CTk(fg_color="#333333") 

    # Adjust size 
    root.geometry( "500x150" ) 
    # Set the original text
    custom_font =("Times",10,'bold')
    greeting = customtkinter.CTkLabel(master=root, text="Welcome to the APOTECA Printer Assistant, Please select the printer model you would like to fix", font=custom_font, text_color="white")
    # Change the label text and confirmation window
        
    # datatype of menu text 
    clicked = StringVar() 
    # initial menu text 
    clicked.set("Click me to find your printer") 
    # Create Dropdown menu 
    def optionmenu_callback(choice):
        sol = choice
        confirmation(sol)
    drop = customtkinter.CTkOptionMenu(master=root , values=options , command=optionmenu_callback ) 
    greeting.pack()
    drop.pack(padx=20, pady=20) 
    # Create button, it will change label text 
    # button = customtkinter.CTkButton( master=root , text = "click Me" , command = show ).pack() 
    # Execute tkinter 
    root.mainloop()


def confirmation(name):
    qm = askyesno(title='Confirmation', message='Are you sure that you want to clear {}'.format(name))
    if qm:
        subprocess.run(r"Status.bat"+" "+ name)

        

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
        main() 

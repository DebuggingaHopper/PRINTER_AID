import subprocess
import tkinter as tk
from tkinter import *
import pyuac
from tkinter.messagebox import askyesno, askquestion
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
    root = Tk() 
    # Adjust size 
    root.geometry( "600x600" ) 
    # Set the original text
    greeting = tk.Label(text="Welcome to the APOTECA Printer Assistant, Please select the printer model you would like to fix")
    # Change the label text and confirmation window
    def show(): 
        sol = clicked.get()
        confirmation(sol)
        
    # datatype of menu text 
    clicked = StringVar() 
    # initial menu text 
    clicked.set("Click me to find your printer") 
    # Create Dropdown menu 
    drop = OptionMenu( root , clicked , *options ) 
    greeting.pack()
    drop.pack() 
    # Create button, it will change label text 
    button = Button( root , text = "click Me" , command = show ).pack() 
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

import subprocess
import tkinter as tk
from tkinter import *
import pyuac

def main():

    root = Tk() 
  
    # Adjust size 
    root.geometry( "200x200" ) 
    
    # Set the original text
    greeting = tk.Label(text="Welcome to the APOTECA Printer Assistant, Please select the printer model you would like to fix")
    # Change the label text 
    def show(): 
        sol = clicked.get()
        if(sol == options[0]):
            subprocess.run(r"Status.bat")
        
    # Dropdown menu options 
    options = [ 
        "PDFPrinter", 
        "Acquire PS Info"
    ] 
  
    # datatype of menu text 
    clicked = StringVar() 
    
    # initial menu text 
    clicked.set( "What would you like to select?" ) 
    
    # Create Dropdown menu 
    drop = OptionMenu( root , clicked , *options ) 
    drop.pack() 
    
    # Create button, it will change label text 
    button = Button( root , text = "click Me" , command = show ).pack() 

    
    # Execute tkinter 
    root.mainloop() 

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main() 

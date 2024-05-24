import subprocess
from tkinter import *
import pyuac

def main():

    root = Tk() 
  
    # Adjust size 
    root.geometry( "200x200" ) 
    
    # Change the label text 
    def show(): 
        sol = clicked.get()
        if(sol == options[0]):
            subprocess.run(r"Status.bat")
        
    # Dropdown menu options 
    options = [ 
        "Fix Printer", 
        "Acquire PS Info"
    ] 
  
    # datatype of menu text 
    clicked = StringVar() 
    
    # initial menu text 
    clicked.set( "What would you like to do?" ) 
    
    # Create Dropdown menu 
    drop = OptionMenu( root , clicked , *options ) 
    drop.pack() 
    
    # Create button, it will change label text 
    button = Button( root , text = "click Me" , command = show ).pack() 

    
    # Execute tkinter 
    root.mainloop() 
    



    '''
    What we would like is to not only stop the spooler, and print a test page but also just change the tcp port address
    I believe it is possible through the following line of code(https://superuser.com/questions/61659/how-do-i-add-a-standard-tcp-ip-printer-port-from-a-command-line):

    rundll32 printui.dll,PrintUIEntry /if /b "PDFPrinter" /f %windir%\inf\ntprint.inf /r  "IP_157.57.50.98" /m "HP Laserjet 4000 Series PCL"

    Now the main challange is the following finding the correct printer. You see what I would like is that is for the PS systems to allow the user to select the correct 
    printer to do the tasks. This is something I would like to automate quickly, i wonder how many printers the PS systems display through CMD to see if we can just quickly query how many and then allow the user to select the correct one
    and then from there select the correct printerIP.

    Overall We would like the printername regardless so the rest of our scripts can work as expected


    To place it as a parameter all I need is:
    from subprocess import *
p = Popen(['run-client.bat', param1, param2], stdout=PIPE, stderr=PIPE)
output, errors = p.communicate()
p.wait() # wait for process to terminate

Where in the batch I just need to use %1 to reference ou string input

What We really want is to just effeciently grab the printer names
    '''

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main() 

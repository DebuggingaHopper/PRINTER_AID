# APOTECA Internal Tools

## Printer Queue Removal
This is a very simple tool tht could be place within various PS devices, where if the user is having a printer issue they can click this to clear the print queue and if it doesnt they can call the help desk line

ETA: I give it 2-3 days once I acquire the needed information

### Core Design:
1. it should allow the user to select the Printer type they are troubleshooting which would be a certain set of models that would have tjhe same name in various sites when installed

2. Once the user clicks then the printer queue is cleeared, print spooler is restarted, and a test page is printer

3. if nothing occurs what will occur is that the help desk line would appear so that they may contact us.

### Ideal features
    What we would like is to not only stop the spooler, and print a test page but also just change the tcp port address
    I believe it is possible through the following line of code(https://superuser.com/questions/61659/how-do-i-add-a-standard-tcp-ip-printer-port-from-a-command-line):

    '''
    rundll32 printui.dll,PrintUIEntry /if /b "PDFPrinter" /f %windir%\inf\ntprint.inf /r  "IP_157.57.50.98" /m "HP Laserjet 4000 Series PCL"
    '''

    Now the main challange is the following finding the correct printer. You see what I would like is that is for the PS systems to allow the user to select the correct 
    printer to do the tasks. This is something I would like to automate quickly, i wonder how many printers the PS systems display through CMD to see if we can just quickly query how many and then allow the user to select the correct one
    and then from there select the correct printerIP.

    Overall We would like the printername regardless so the rest of our scripts can work as expected


    To place it as a parameter all I need is:
    '''
    from subprocess import *
    p = Popen(['run-client.bat', param1, param2], stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    p.wait() # wait for process to terminate
    '''
    
Where in the batch I just need to use %1 to reference ou string input

What We really want is to just effeciently grab the printer names

    Of course what also helps is a logger so we can create one


## APOTECA resources

Soemthing that is extremely frustrating is that there isn't a centralized resource instead we have to navigate a complex network plath thats not user freindly

This way isnetad of everyone relying on the othwrs to provide where they are they can quickly get sent to the path through a simple program

Now what would be really helpful is to have an internal database that contains the DATS, a US version of SWGA with the only use to be to check if we have this drug and aquire the img and IDE from the farmaci folder.

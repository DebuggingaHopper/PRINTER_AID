

# Printer Queue Removal
This is a very simple tool that I wanted to create due to a certain issue we have within the compnay I am emploted at. Long story short, we want our users to quickly clear the queues with minimal possibility for the user to make a mistake. In this case just to clear the printer queue for the user.

### Core Design:
1. It should allow the user to select the printer type they are troubleshooting, which would be a certain set of models that would have the same name on various sites when installed.

2. Once the user clicks, the printer queue is cleared, the print spooler is restarted, and a test page is printed.

3. If nothing occurs, what will occur is that the help desk line will appear so that they may contact us.

### Ideal features
What we would like is to not only stop the spooler and print a test page, but also just change the TCP port address.

I believe it is possible through the following line of code (https://superuser.com/questions/61659/how-do-i-add-a-standard-tcp-ip-printer-port-from-a-command-line):

```
rundll32 printui.dll,PrintUIEntry /if /b "PDFPrinter" /f %windir%\inf\ntprint.inf /r "IP_157.57.50.98" /m "HP Laserjet 4000 Series PCL"
```

Now the main challenge is finding the correct printer. You see, what I would like is for the PS systems to allow the user to select the correct printer to do the tasks. This is something I would like to automate quickly. I wonder how many printers the PS systems display through CMD to see if we can just quickly query how many and then allow the user to select the correct one, and then from there select the correct printer IP.

Overall, we would like the printer name regardless so the rest of our scripts can work as expected.
To place it as a parameter, all I need is:

    ```
    from subprocess import *
    p = Popen(['run-client.bat', param1, param2], stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    p.wait() # wait for process to terminate
    ```
   
   
where in the batch I just need to use %1 to reference our input

What we really want is to just efficiently grab the printer names.

### 5/25/2024

In less than an hour, I was able to determine an efficient way to display all the printers the PC has at its disposal, and later on, we can filter said list to only show the Zebra printers. This was very easy to do, along with the extremely simple implementation of arguments in this program. Now what I will be researching for around 20 minutes is how to set the port to a different IP address.


From our little discovery we were able to find documentation of Windows prnport (yes very mature I am aware). So it seems what we can do to the printer is change it's settings which could be possible from this documentation:
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/prnport

However at the same time I am looking at alternatives at:
- https://superuser.com/questions/1403776/how-to-find-the-ip-of-a-network-printer-from-command-line 
- https://superuser.com/questions/61659/how-do-i-add-a-standard-tcp-ip-printer-port-from-a-command-line
- https://community.spiceworks.com/t/need-script-to-bulk-change-printer-port-ip-addresses-on-2012-r2-print-server/559431/13

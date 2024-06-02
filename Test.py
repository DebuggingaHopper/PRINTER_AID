import subprocess
import pyuac
# What this script proves is that yhe app crashes because it relies on the print spooler service running at all times
# When it's restarted then the app freezes because its trying to grab the necessray info to display 

# What was dteermined that we needed to run a seperate thread for this asyncrhonous call 
def main():
    subprocess.run(r"Status.bat"+" "+ "PDFPrinter",shell=True, check=True)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
       main()
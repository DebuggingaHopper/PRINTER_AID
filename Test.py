import subprocess
import pyuac
def main():
    subprocess.run(r"Status.bat"+" "+ "PDFPrinter",shell=True, check=True)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
       main()

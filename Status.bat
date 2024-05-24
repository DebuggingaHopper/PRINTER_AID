for /F "tokens=3 delims=: " %%H in ('sc query "Spooler" ^| findstr "STATE"') DO (
   if /I "%%H" NEQ "STOPPED" (
      net stop Spooler
      del %systemroot%\System32\spool\printers\* /Q
      net start Spooler
      pause
      )
  if /I "%%H" NEQ "RUNNING" (
      net start Spooler
      net stop Spooler
      del %systemroot%\System32\spool\printers\* /Q
      net start Spooler
      pause
      )
    )
echo %Status%
rundll32 printui.dll,PrintUIEntry /k /n"PDFPrinter"




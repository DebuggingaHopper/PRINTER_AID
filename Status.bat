del %systemroot%\System32\spool\printers\* /Q
timeout /t 30 /nobreak
rundll32 printui.dll,PrintUIEntry /k /n %1

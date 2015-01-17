del *.pyc
for %%f in (*.ui) do c:\python27\python.exe c:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py %%f -x -o %%~nf_ui.py
pause

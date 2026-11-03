from PyQt5 import uic

with open("SpeedTestWindow.py" , "w" , encoding="utf-8") as fout:
    uic.compileUi("SpeedTestWindow.ui", fout)
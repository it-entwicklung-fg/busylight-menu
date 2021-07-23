#!/usr/bin/env python3
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import os 
from ColorFunctions import *

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

scriptDir = os.path.dirname(os.path.realpath(__file__))

# Adding an icon
iconBlue = QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Blue.png')
iconGreen = QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Green.png')
iconRed = QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Red.png')
iconWhite = QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_White.png')
iconYellow = QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Yellow.png')

iconOff = QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Off.png')

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(iconOff)
tray.setVisible(True)
 
# Creating the options
menu = QMenu()
option1 = QAction(iconGreen, "Frei")
option2 = QAction(iconRed, "Am Telefon")
option3 = QAction(iconBlue, "In Fernwartung")
option4 = QAction(iconYellow, "Beschäftigt")
option1.triggered.connect(lambda: Green(tray, iconGreen))
option2.triggered.connect(lambda: Red(tray, iconRed))
option3.triggered.connect(lambda: Blue(tray, iconBlue))
option4.triggered.connect(lambda: Yellow(tray, iconYellow))
menu.addAction(option1)
menu.addAction(option2)
menu.addAction(option3)
menu.addAction(option4)

menu.addSeparator()

# Farben
submenu = QMenu("Farben")
suboption1 = QAction(iconGreen, "Grün")
suboption2 = QAction(iconRed, "Rot")
suboption3 = QAction(iconBlue, "Blau")
suboption4 = QAction(iconYellow, "Gelb")
suboption5 = QAction(iconWhite, "Weiß")
suboption1.triggered.connect(lambda: Green(tray, iconGreen))
suboption2.triggered.connect(lambda: Red(tray, iconRed))
suboption3.triggered.connect(lambda: Blue(tray, iconBlue))
suboption4.triggered.connect(lambda: Yellow(tray, iconYellow))
suboption5.triggered.connect(lambda: White(tray, iconWhite))
submenu.addAction(suboption1)
submenu.addAction(suboption2)
submenu.addAction(suboption3)
submenu.addAction(suboption4)
submenu.addAction(suboption5)
menu.addMenu(submenu)
  
menu.addSeparator()  

# Aus
optionOff = QAction(iconOff, "Aus")
menu.addAction(optionOff)
optionOff.triggered.connect(lambda: Off(tray, iconOff))

# To quit the app
#quit = QAction("Beenden")
#quit.triggered.connect(app.quit)
#menu.addAction(quit)
  
# Adding options to the System Tray
tray.setContextMenu(menu)
  
app.exec_()

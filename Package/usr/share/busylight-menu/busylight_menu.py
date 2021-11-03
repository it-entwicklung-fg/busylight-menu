#!/usr/bin/python3
import os
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

scriptDir = os.path.dirname(os.path.realpath(__file__))

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Icons
icons = {
    "off" : QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Off.png'),
    "red" : QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Red.png'),
    "green" : QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Green.png'),
    "blue" : QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Blue.png'),
    "yellow" : QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_Yellow.png'),
    "white" : QIcon(scriptDir + os.path.sep + 'icons' + os.path.sep + 'BL_White.png')
    }

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icons["off"])
tray.setVisible(True)
 
# Creating the options
menu = QMenu()
option1 = QAction(icons["green"], "Frei")
option2 = QAction(icons["red"], "Am Telefon")
option3 = QAction(icons["blue"], "In Fernwartung")
option4 = QAction(icons["yellow"], "Beschäftigt")
option1.triggered.connect(lambda: color(icons["green"], 0, 255, 0))
option2.triggered.connect(lambda: color(icons["red"], 255, 0, 0))
option3.triggered.connect(lambda: color(icons["blue"], 0, 0, 255))
option4.triggered.connect(lambda: color(icons["yellow"], 255, 255, 0))
menu.addAction(option1)
menu.addAction(option2)
menu.addAction(option3)
menu.addAction(option4)

menu.addSeparator()

# Farben
submenu = QMenu("Farben")
suboption1 = QAction(icons["green"], "Grün")
suboption2 = QAction(icons["red"], "Rot")
suboption3 = QAction(icons["blue"], "Blau")
suboption4 = QAction(icons["yellow"], "Gelb")
suboption5 = QAction(icons["white"], "Weiß")
suboption1.triggered.connect(lambda: color(icons["green"], 0, 255, 0))
suboption2.triggered.connect(lambda: color(icons["red"], 255, 0, 0))
suboption3.triggered.connect(lambda: color(icons["blue"], 0, 0, 255))
suboption4.triggered.connect(lambda: color(icons["yellow"], 255, 255, 0))
suboption5.triggered.connect(lambda: color(icons["white"], 255, 255, 255))
submenu.addAction(suboption1)
submenu.addAction(suboption2)
submenu.addAction(suboption3)
submenu.addAction(suboption4)
submenu.addAction(suboption5)
menu.addMenu(submenu)
  
menu.addSeparator()  

# Aus
optionOff = QAction(icons["off"], "Aus")
menu.addAction(optionOff)
optionOff.triggered.connect(lambda: color(optionOff.icon))

# To quit the app
optionquit = QAction("Beenden")
optionquit.triggered.connect(lambda: quit())
menu.addAction(optionquit)
  
# Adding options to the System Tray
tray.setContextMenu(menu)

# Function to exit app
def quit():
    rgbfile = open("/var/cache/busylight/rgb", "w")
    rgbfile.write("0\n")
    rgbfile.write("0\n")
    rgbfile.write("0\n")
    rgbfile.close()
    app.quit()

# Function to change color
def color(icon=icons["off"], red=0, green=0, blue=0):
    tray.setIcon(QIcon(icon))
    rgbfile = open("/var/cache/busylight/rgb", "w")
    rgbfile.write(str(red) + "\n")
    rgbfile.write(str(green) + "\n")
    rgbfile.write(str(blue) + "\n")
    rgbfile.close()

app.exec_()

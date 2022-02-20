#!/usr/bin/python3
import os.path
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from configparser import ConfigParser

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

config_file = "/var/local/busylight/config.conf"
config = ConfigParser()

# Get current Color
if os.path.isfile(config_file):
    config.read(config_file)
    rgb = config["RGB"]
    if len(rgb) >= 3:
        red = int(rgb["red"])
        green = int(rgb["green"])
        blue = int(rgb["blue"])
        print(green)
        boolR = red == 255
        boolG = green == 255
        boolB = blue == 255
        print(boolG)
        if (0 <= red <= 255) and (0 <= green <= 255) and (0 <= blue <= 255):
            color = "red" if boolR and not boolG  and not boolB  else "green" if not boolR and boolG and not boolB else "blue" if not boolR and not boolG and boolB else "yellow" if boolR and boolG and not boolB else "white" if boolR and boolG and boolB else "off"
    else:
        color = "off"

# Icons
icons = {
    "off": QIcon.fromTheme("busylight-off"),
    "red": QIcon.fromTheme("busylight-red"),
    "green": QIcon.fromTheme("busylight-green"),
    "blue": QIcon.fromTheme("busylight-blue"),
    "yellow": QIcon.fromTheme("busylight-yellow"),
    "white": QIcon.fromTheme("busylight-white")
}

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icons[color])
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
optionOff.triggered.connect(lambda: color(icons["off"]))

# To quit the app
option_exit = QAction("Beenden")
option_exit.triggered.connect(lambda: quit_app())
menu.addAction(option_exit)

# Adding options to the System Tray
tray.setContextMenu(menu)


# Function to exit app
def quit_app():
    if os.path.isfile(config_file):
        config.read(config_file)
        rgb = config["RGB"]
        rgb["red"] = "0"
        rgb["green"] = "0"
        rgb["blue"] = "0"
        with open(config_file, "w+") as conf:
            config.write(conf)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Service not running")
        msg.setInformativeText("The background servive that is needed is not running")
        msg.setWindowTitle("ERROR")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()
    app.quit()


# Function to change color
def color(icon=icons["off"], red=0, green=0, blue=0):
    if os.path.isfile(config_file):
        tray.setIcon(QIcon(icon))
        config.read(config_file)
        rgb = config["RGB"]
        rgb["red"] = str(red)
        rgb["green"] = str(green)
        rgb["blue"] = str(blue)
        with open(config_file, "w+") as conf:
            config.write(conf)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Service not running")
        msg.setInformativeText("The background servive that is needed is not running")
        msg.setWindowTitle("ERROR")
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


app.exec_()

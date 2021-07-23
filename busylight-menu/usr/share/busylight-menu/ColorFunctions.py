from BusyLight import *
import time, threading

repeat = True
r = 0
g = 0
b = 0
run = False

# Colors
def Green(tray, icon):
  global repeat, r, g, b, run
  repeat = True
  tray.setIcon(icon)
  r = 0
  g = 255
  b = 0
  if run == False:
    Color()

def Red(tray, icon):
  global repeat, r, g, b, run
  repeat = True
  tray.setIcon(icon)
  r = 255
  g = 0
  b = 0
  if run == False:
    Color()

def Blue(tray, icon):
  global repeat, r, g, b, run
  repeat = True
  tray.setIcon(icon)
  r = 0
  g = 0
  b = 255
  if run == False:
    Color()

def Yellow(tray, icon):
  global repeat, r, g, b, run
  repeat = True
  tray.setIcon(icon)
  r = 255
  g = 255
  b = 0
  if run == False:
    Color()
    
def White(tray, icon):
  global repeat, r, g, b, run
  repeat = True
  tray.setIcon(icon)
  r = 255
  g = 255
  b = 255
  if run == False:
    Color()

def Off(tray, icon):
  global repeat, r, g, b, run
  repeat = False
  tray.setIcon(icon)
  r = 0
  g = 0
  b = 0
  
def Color():
  global repeat, r, g, b, run
  if(repeat == True):
    run = True
    color_setter(r, g, b)
    threading.Timer(0.5, Color).start()
  else:
    clear_bl()
    run = False

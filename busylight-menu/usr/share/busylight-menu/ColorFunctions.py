from BusyLight import *
import threading

repeat = True
r = 0
g = 0
b = 0

# Colors
def Color(red, green, blue, tray, icon):
  global repeat, r, g, b
  tray.setIcon(icon)
  r = red
  g = green
  b = blue
  if repeat == False:
    repeat = True
    ColorAutomation()

def Off(tray, icon):
  global repeat, r, g, b
  repeat = "clear"
  tray.setIcon(icon)
  r = 0
  g = 0
  b = 0
  
def ColorAutomation():
  global repeat, r, g, b
  if(repeat == True):
    color_setter(r, g, b)
    threading.Timer(0.5, ColorAutomation).start()
  elif (repeat == "clear"):
    clear_bl()
    repeat = False

from tkinter import *
import tkinter.font
from gpiozero import LED, Buzzer
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time

## Hardware Declaration
buzzer = Buzzer(14)
ledRed = LED(15)
ledGreen = LED(18)
ledBlue = LED(23)


##GUI DEFINITIONS ##
win = Tk()
win.title("My Application")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event functions
def ledRedToggle():
    if ledRed.is_lit:
        ledRed.off()
        ledRedButton.deselect()
    else:
        ledRed.on()
        RPi.GPIO.output(14, RPi.GPIO.HIGH)
        time.sleep(0.5)
        RPi.GPIO.output(14, RPi.GPIO.LOW)
        ledRedButton.select()

def ledGreenToggle():
    if ledGreen.is_lit:
        ledGreen.off()
        ledGreenButton.deselect()
    else:
        ledGreen.on()
        RPi.GPIO.output(14, RPi.GPIO.HIGH)
        time.sleep(0.5)
        RPi.GPIO.output(14, RPi.GPIO.LOW)
        ledGreenButton.select()
    
def ledBlueToggle():
    if ledBlue.is_lit:
        ledBlue.off()
        ledBlueButton.deselect()
    else:
        ledBlue.on()
        RPi.GPIO.output(14, RPi.GPIO.HIGH)
        time.sleep(0.5)
        RPi.GPIO.output(14, RPi.GPIO.LOW)
        ledBlueButton.select()

def close():
    RPi.GPIO.cleanup()
    win.destroy()
   
## WIDGETS
color = IntVar()
ledRedButton = Radiobutton(win, text = "Red", variable = "color", value = 1, font = myFont, command = ledRedToggle, bg = 'bisque2',height = 1, width = 24)
ledGreenButton = Radiobutton(win, text = "Green", variable = "color", value = 2, font = myFont, command = ledGreenToggle, bg = 'bisque2',height = 1, width = 24)
ledBlueButton = Radiobutton(win, text = "Blue", variable = "color", value = 3, font = myFont, command = ledBlueToggle, bg = 'bisque2',height = 1, width = 24)


exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)

ledRedButton.grid(row = 0, column = 1)
ledGreenButton.grid(row = 1, column = 1)
ledBlueButton.grid(row = 2, column = 1)

win.protocol('WM_DELETE_WINDOW', close)
win.mainloop() # loop forever

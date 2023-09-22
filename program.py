from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

# Mode of Raspberry Pi
RPi.GPIO.setmode(RPi.GPIO.BCM)

# LED Pin Declaration
ledRed = LED(20)
ledGreen = LED(12)
ledBlue = LED(21)

# Padding Variables
px = 30
py = 30

# LED control
def led_control(led, state):
    if state:
        led.on()
        # Turn off other LEDs
        [other_led.off() for other_led in (ledRed, ledGreen, ledBlue) if other_led != led]
    else:
        led.off()

# Event functions
def ledRedToggle():
    led_control(ledRed, not ledRed.is_lit)

def ledGreenToggle():
    led_control(ledGreen, not ledGreen.is_lit)

def ledBlueToggle():
    led_control(ledBlue, not ledBlue.is_lit)

def close():
    RPi.GPIO.cleanup()
    win.destroy()

# GUI definitions
win = Tk()
win.title("My Application")

# Set Style
myFont = tkinter.font.Font(family = 'Arial', size = 12, weight = "bold")

# Create a label widget
label = Label(win, text="Three LEDs Task")

# Grid the label widget
label.grid(row=0, column=1, padx = px, pady = py)

# Widgets
color = IntVar()

# Create an array of arguments for the Radiobutton widget
radiobutton_args = [
    {
        "text": "Green",
        "variable": color,
        "value": 2,
        "font": myFont,
        "command": ledGreenToggle,
        "bg": "white",
        "height": 1,
        "width": 20
    },
    {
        "text": "Red",
        "variable": color,
        "value": 1,
        "font": myFont,
        "command": ledRedToggle,
        "bg": "white",
        "height": 1,
        "width": 20
    },
    {
        "text": "Blue",
        "variable": color,
        "value": 3,
        "font": myFont,
        "command": ledBlueToggle,
        "bg": "white",
        "height": 1,
        "width": 20
    }
]

# Create the Radiobutton widgets
row = 1
for args in radiobutton_args:
    Radiobutton(win, **args).grid(row=row, column=1)
    row+=1

# Create an array of arguments for the exit button
exit_button_args = [
    {
        "text": "Exit",
        "font": myFont,
        "command": close,
        "bg": "red",
        "height": 1,
        "width": 20,
    }
]

# Create the exit button
exitButton = Button(win, **exit_button_args[0])
exitButton.grid(row = 4, column = 1, padx=px, pady=py)

# Style the exit button
exitButton.config(foreground="white", borderwidth=2, relief="raised")

win.protocol('WM_DELETE_WINDOW', close)
win.mainloop() # loop forever



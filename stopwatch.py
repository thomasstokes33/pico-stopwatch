'''
Author1: Thomas


Date: May 2023

REQUIREMENTS: 
* Pimoroni-Pico Library:https://github.com/pimoroni/pimoroni-pico/releases/tag/v1.20.1
*

'''

from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
import time
import sys
import select
from machine import Pin

# Setting up the display
display = PicoGraphics(display = DISPLAY_PICO_DISPLAY, pen_type = PEN_RGB332, rotate = 270)
display.set_font("bitmap8")

# Setting up colours
WHITE  = display.create_pen(255, 255, 255)
BLACK  = display.create_pen(0, 0, 0)
RED    = display.create_pen(255, 0, 0)
YELLOW = display.create_pen(255, 255, 0)

def clear(colour = BLACK):
    '''
    This function clears the screen and sets the background colour to the specified colour
    @param: colour (default = BLACK) - The colour of the background
    '''
    display.set_pen(colour)
    display.clear()
    display.update()


def resetTime():
    '''
    This function resets the time to 0
    '''
    global startTime,pausedTime
    startTime = time.time()
  
    pausedTime= startTime
    


def getTime():
    '''
    This function returns the time since the stopwatch was started
    '''
    if run:
        
        return time.time() - startTime
    else:
        return pausedTime-startTime

def play():
    '''
    Handles the start button being pressed
    '''
    global run, startTime, pausedTime
    if not run: #catches button presses whilst already playing
        if (startTime!=pausedTime ):
            currentlyDisplayed = pausedTime-startTime
            startTime = time.time()-currentlyDisplayed
        else:
            startTime = time.time()  #this is the case for when it is first started or reset to zero.
        run=True    
    
    
    
        

def stop():
    '''
    Handles the stop button being pressed
    '''
    global run,pausedTime
    if run:
        run=False
        pausedTime = time.time()

startButton = Pin(12,Pin.IN,Pin.PULL_UP) #a starts
stopButton =   Pin(13,Pin.IN,Pin.PULL_UP) #b stops
resetPin = Pin(14,Pin.IN,Pin.PULL_UP) #x resets
run = False
startTime = time.time()
pausedTime = startTime
resetPin.irq(lambda pin: resetTime(),Pin.IRQ_FALLING) #Falling is used so that pressing the button only triggers the reset once
clear()
display.set_pen(WHITE) # Sets the colour of the text
display.text(str(getTime()), 10, 10, 240, 3) # Displays the text: text, x, y, wrap length, scale          text, x, y, wrap length, scale,angle,spacing
display.update() # Updates the display

startButton.irq(lambda p: play(),Pin.IRQ_FALLING)
stopButton.irq(lambda p: stop(),Pin.IRQ_FALLING)


while True:
    clear()
    display.set_pen(WHITE) 
    display.text(str(getTime()), 10, 10, 240, 3) #main loop which displays the stopwatch
    display.update()
    time.sleep(0.2)





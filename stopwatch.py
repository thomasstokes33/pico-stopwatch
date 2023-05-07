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
    ##todo: reset time
    


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
        pass
        ##todo: start button handler
    
    
        

def stop():
    '''
    Handles the stop button being pressed
    '''
    global run,pausedTime
    ##todo: stop button handler


##todo: pin setup


clear()
display.set_pen(WHITE) # Sets the colour of the text
display.text(str(getTime()), 10, 10, 240, 3) # Displays the text: text, x, y, wrap length, scale          text, x, y, wrap length, scale,angle,spacing
display.update() # Updates the display



while True:
    clear()
    display.set_pen(WHITE) 
    display.text(str(getTime()), 10, 10, 240, 3) #main loop which displays the stopwatch
    display.update()
    time.sleep(0.2)





# Used as a base to interpret LOGO commands and send them to the AXIDRAW
# [ OCR ] -> [ LOGO ] -> [* AXIDRAW ]

import os
from ocrmac import ocrmac
from pyaxidraw import axidraw
import math
import time

logo_folder = '/Users/tudvari/Documents'
pipe_name = 'axidraw'
pipe_path = logo_folder + os.sep + pipe_name

heading = 0
# axidraw keeps track of the turtle pos
ad = None
degToRad = math.pi / 180

def setup():
    global ad
    ad = axidraw.AxiDraw()
    ad.interactive()
    if not ad.connect():            # Open serial port to AxiDraw
        quit()
    ad.options.units = 2            # set working units to cm.
    ad.options.model = 1            # set axidraw model to AxiDraw V3/A1
    ad.update()       

def interpret_line(ln):
    global heading
    global degToRad
    print("interpreting " + ln)
    # ex fd 100, bk 100, rt 90, lt 90
    # ex pu, pd
    tokens = ln.split(" ")
    if len(tokens) == 1:
        if tokens[0] == "pu":
            ad.penup()
        elif tokens[0] == "pd":
            ad.pendown()
        elif tokens[0] == "cs":
            ad.goto(297 / 2, 210 / 2)
            #interpret_line("pd")
            heading = 0
        elif tokens[0] == "home":
            heading = 0
            ad.moveto(0, 0)

    if len(tokens) == 2:
        command = tokens[0]
        argument = float(tokens[1])
        if command == 'rt':
            heading += argument
        if command == 'lt':
            heading -= argument
        if command == 'fd':
            argument = argument * -1 # so it doesn't feel upside down on axidraw
            deltaX = math.cos(degToRad * heading) * argument
            deltaY = math.sin(degToRad * heading) * argument
            print("move: " + str(deltaX) + ", " + str(deltaY) + "\n")
            ad.go(deltaX, deltaY) 
        if command == 'bk':
            argument = argument * -1
            deltaX = math.cos(degToRad * heading) * -argument
            deltaY = math.sin(degToRad * heading) * -argument
            ad.go(deltaX, deltaY) 
            print("move: " + str(deltaX) + ", " + str(deltaY) + "\n")

    if len(tokens) == 3:
        command = tokens[0]
        if command == 'setpos':
            # set pos from the center
            print("x is " + tokens[1] + " y is " + tokens[2])
            x = -1 * float(tokens[2]) + (297 / 2)
            y = -1 * float(tokens[1]) + (210 / 2)
            ad.goto(x, y)
    
def main():
    try:
        setup()
        interpret_line("cs")
        pipe_fd = os.open(pipe_path, os.O_RDONLY)
        with os.fdopen(pipe_fd, 'r') as pipe:
            while True:
                instruction = pipe.readline().strip()
                if len(instruction) > 0:
                    interpret_line(instruction)
                time.sleep(0.01)
    finally:
        interpret_line("home")
        if ad is not None:
            ad.disconnect()

if __name__ == "__main__":
    main()
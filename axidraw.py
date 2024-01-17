# Documentation
# https://axidraw.com/doc/py_api/

# from pyaxidraw import axidraw

from pyaxidraw import axidraw   
ad = axidraw.AxiDraw()
ad.plot_setup("svgs/1-turtle.svg")
ad.plot_run()

# ad = axidraw.AxiDraw()
# ad.interactive()
# if not ad.connect():            # Open serial port to AxiDraw
#     quit()
# ad.options.units = 2            # set working units to cm.
# ad.options.model = 1            # set axidraw model to AxiDraw V3/A1
# ad.update()                     # Process changes to options 
# ad.move(1000, 100)
# ad.moveto(0,0)                  # Pen-up move, back to origin.

# ad.disconnect()                 # Close serial port to AxiDraw
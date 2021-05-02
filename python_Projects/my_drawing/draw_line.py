"""
File: draw line
Name:Ray Lee
-------------------------
TODO:This program will print a line with the following method:
     1st mouse clicked: create a circle at the point clicked
     2nd mouse clicked: connect the point from 2nd clicked and the 1st clicked circle, the circle will be erased
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# CONSTANT
SIZE = 10

# global variable
window = GWindow(1000, 1000)
times = 0  # record if it is the first or second click
circle = GOval(SIZE, SIZE)  # nature of the circle shown after the first click


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(link)


def link(m):
    global times, circle
    if times == 0:
        circle.x = m.x-SIZE/2
        circle.y = m.y-SIZE/2
        window.add(circle, m.x-SIZE/2, m.y-SIZE/2)
        times = 1
    else:
        line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, m.x, m.y)
        window.add(line)
        window.remove(circle)
        times = 0





if __name__ == "__main__":
    main()

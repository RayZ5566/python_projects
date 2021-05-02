"""
File: bouncing ball
Name:Ray Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
from campy.util.sound import Sound

VX = 3
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')


# global variables
times = 0  # record times outside the window
ball = GOval(SIZE, SIZE)  # create the ball
moving = 0  # check if the ball is moving, refusing mouse clicked interrupt
times_record = GLabel('times tried : '+str(times))


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)
    times_record.font = 'calibri-20-bold-italic'
    window.add(times_record, 0, times_record.height)
    onmouseclicked(start)


def start(m):
    global times,  moving
    if times < 3 and moving == 0:
        speed = 0  # record the current speed of the ball
        moving = 1
        while not ball.x+SIZE >= window.width:
            ball.move(VX, speed)  # ball falling down with speed plus Gravity and move horizontally with VX
            pause(DELAY)
            speed += GRAVITY
            if ball.y+SIZE >= window.height:  # check if touched the floor
                speed *= REDUCE  # the remaining vertical speed at this bounce
                speed = -speed
        if ball.x + SIZE >= window.width:  # check if outside the window
            times += 1  # record times of ball outside the window
            times_record.text = 'times tried: ' + str(times)
            moving = 0  # ready to restart
        window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()

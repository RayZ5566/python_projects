"""
File: pokeball
Name:Ray Lee
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GRoundRect
from campy.graphics.gcolor import GColor
from campy.graphics.gwindow import GWindow


def main():
    w = GWindow(600, 600, title='Pokéball')  # create a 600*600 window
    center = w.height/2

    # Upper ball red
    radius_u = 200
    upper = GOval(2*radius_u, 2*radius_u, x=center-radius_u, y=center-radius_u)
    red = GColor(255, 56, 56)
    upper.filled = True
    upper.fill_color = red
    upper.color = red

    # Boundary black
    radius_b = 210
    bound = GOval(2*radius_b, 2*radius_b, x=center-radius_b, y=center-radius_b)
    black = GColor(56, 56, 56)
    bound.filled = True
    bound.fill_color = black
    bound.color = black

    # Lower ball white
    radius_l = 400
    lower = GArc(radius_l, 2*radius_l, 180, 180, x=center-radius_u, y=center-radius_u)
    white = GColor(255, 255, 255)
    lower.filled = True
    lower.fill_color = white
    lower.color = white

    # Center belt
    width_b = radius_b-10
    height_b = 35
    belt = GRect(2*width_b, height_b, x=center-width_b, y=center-height_b/2)
    belt.filled = True
    belt.fill_color = black
    belt.color = black

    # Center button bound
    radius_b_b = 60
    button_b = GOval(2*radius_b_b,2*radius_b_b, x=center-radius_b_b, y=center-radius_b_b)
    button_b.filled = True
    button_b.fill_color = black
    button_b.color = black

    # Center button
    radius_bu = 50
    button = GOval(2*radius_bu, 2*radius_bu, x=center-radius_bu, y=center-radius_bu)
    button.filled = True
    button.fill_color = white
    button.color = white


    w.add(bound)
    w.add(upper)
    w.add(lower)
    w.add(belt)
    w.add(button_b)
    w.add(button)







if __name__ == '__main__':
    main()

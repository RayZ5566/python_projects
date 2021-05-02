"""
File: pokeball
Name:Ray Lee
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GRoundRect
from campy.graphics.gcolor import GColor
from campy.graphics.gwindow import GWindow

RADIUS = 200

class Pokeball:

    def __init__(self, radius=RADIUS):

        # w = GWindow(600, 600, title='Pokéball')  # create a 600*600 window
        # center = w.height/2

        # Upper ball red
        # radius_u = 200
        self.upper = GOval(2*radius, 2*radius)
        red = GColor(255, 56, 56)
        self.upper.filled = True
        self.upper.fill_color = red
        self.upper.color = red

        # Boundary black
        # radius_b = 210
        self.bound = GOval(2*(radius+10/radius), 2*(radius+10/radius))
        black = GColor(56, 56, 56)
        self.bound.filled = True
        self.bound.fill_color = black
        self.bound.color = black

        # Lower ball white
        radius_l = 400
        self.lower = GArc(2*radius, 4*radius, 180, 180)
        white = GColor(255, 255, 255)
        self.lower.filled = True
        self.lower.fill_color = white
        self.lower.color = white

        # Center belt
        width_b = radius
        height_b = 30/radius
        self.belt = GRect(2*width_b, height_b)
        self.belt.filled = True
        self.belt.fill_color = black
        self.belt.color = black

        # Center button bound
        radius_b_b = 50/radius
        self.button_b = GOval(2*radius_b_b,2*radius_b_b)
        self.button_b.filled = True
        self.button_b.fill_color = black
        self.button_b.color = black

        # Center button
        radius_bu = 40/radius
        self.button = GOval(2*radius_bu, 2*radius_bu)
        self.button.filled = True
        self.button.fill_color = white
        self.button.color = white


        # w.add(self.bound)
        # w.add(self.upper)
        # w.add(self.lower)
        # w.add(self.belt)
        # w.add(self.button_b)
        # w.add(self.button)







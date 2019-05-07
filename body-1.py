# Aditya Srivastava ; CS1 ; 10/19/16 ; body.py
# This class allows you to draw a body which can move and accelerate.

from cs1lib import *

class Body:

    # initializing values for the constructor
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):

        self.mass = mass
        self.x = x  # x position in meters
        self.y = y  # y position in meters
        self.vx = vx  # x velocity in meters
        self.vy = vy  # y velocity in meters
        self.pixel_radius = pixel_radius     # radius in pixels
        self.r = r    # color (r)
        self.g = g    # color (g)
        self.b = b    # color (b)

    # method updates the position
    def update_position(self, timestep):

        self.x = self.x + timestep * self.vx  # updating the x position with timestep and velocity
        self.y = self.y + timestep * self.vy  # updating the y position with timestep and velocity

    # method updates the velocity
    def update_velocity(self, ax, ay, timestep):

        self.vx = self.vx + timestep * ax  # updating the x velocity with timestep and acceleration
        self.vy = self.vy + timestep * ay  # updating the y velocity with timestep and acceleration

    # method draws from the parameters passed in cx, cy, and pixels_per_meter
    def draw(self, cx, cy, pixels_per_meter):

        set_fill_color(self.r, self.g, self.b)      # allows the color to be set when the class is called

        # draws the circle for body's and converts the inputs into pixels
        draw_circle((pixels_per_meter * self.x) + cx, (pixels_per_meter * self.y) + cy, self.pixel_radius)
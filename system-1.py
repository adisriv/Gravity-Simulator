# Aditya Srivastava, CS1, 10/19/16 ; system.py
# This class allows multiple bodies in a given list to be drawn and move by using the Body class and its methods

from cs1lib import *
from body import Body
from math import *

class System:

    def __init__(self, body_list):

        self.body_list = body_list    # body list is set to self.body_list to be used in this class

    # updates the position and velocity of each object in the list
    def update(self, timestep):

        # updates the position of each body in the list
        for each_body in range(len(self.body_list)):

            (ax, ay) = self.compute_acceleration(self.body_list[each_body])     # calling the values of ax and ay as tuples so they can be called at the same time
            self.body_list[each_body].update_velocity(ax, ay, timestep)  # acceleration is set to ax and ay and timestep is used
            self.body_list[each_body].update_position(timestep)        # calls the update position method from Body

    # computes the x and y components of the acceleration of the body at index n in the list
    def compute_acceleration(self, n):

        G = 6.67384e-11    # universal gravitation constant
        ax = 0             # acceleration in the x direction is set to 0 to begin
        ay = 0             # acceleration in the y direction is set to 0 to begin
        for each_body in range(len(self.body_list)):

            # if loop to make sure accleration isn't calculated for a body n on itself
            if self.body_list[each_body] != n:

                m = self.body_list[each_body].mass       # m is set to mass
                dx = self.body_list[each_body].x - n.x   # distance between the x coordinate of two bodies
                dy = self.body_list[each_body].y - n.y   # distance between the y coordinate of two bodies
                r = sqrt(dx * dx + dy * dy)              # radius given by the distance formula

                a = (G * m)/(r * r)                     # acceleration formula

                ax = ax + (a * dx) / r                   # adding up the values of the acceleration in the x direction
                ay = ay + (a * dy) / r                   # adding up the values of the acceleration in the x direction

        return (ax, ay)                                  # returns the values ax and ay as a tuple

    # draws the each body that is located in the list
    def draw(self, cx, cy, pixels_per_meter):

        # for loop for drawing each body in the list
        for body_one in self.body_list:

            # draws a body by calling the draw method in Body and passing on the values of the parameters
            body_one.draw(cx, cy, pixels_per_meter)



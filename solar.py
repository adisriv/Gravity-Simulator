# Aditya Srivastava ; CS1 ; 10/24/16 ; solar.py
# This file simulates the solar system and how the planets revolve around the sun
# Discussed solar.py with Section Leaders: Cara.E.Van.Uden and Devika.S.Dholakia on how to adjust timescale, timestep, and pixels_per_meter

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 10000000        # real seconds per simulation second


FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame
AU = 1.49598e11             # astronomical units
EM = 5.9736e24              # earth mass (1 EM per earth mass)
PIXELS_PER_METER = 120 / AU  # distance scale for the simulation


def main():

    set_clear_color(0, 0, 0)    # black background

    clear()
    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, 24, 1, 1, 0)    # yellow sun
mercury = Body(EM * 0.055, AU * 0.387, 0, 0, 47890, 3, 0.5, 0.5, 0.5)   # gray mercury
venus = Body(EM * 0.81, AU * 0.723, 0, 0, 35040, 4, 0, 1, 0)       # green venus
earth = Body(EM, AU, 0, 0, 29790, 9, 0, 0, 1)                # blue earth
mars = Body(EM * 0.108, AU * 1.52, 0, 0, 24140, 6, 1, 0, 0)    # red mars
solar_system = System([sun, mercury, venus, earth, mars])


start_graphics(main, 2400, framerate=FRAMERATE)
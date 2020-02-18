"""This file contains the Color class."""
import numpy as np


class Color:
    """Facilitate storage of color values."""

    name = ""
    MIN_VAL = 0
    MAX_VAL = 0

    def __init__(self, color_name):
        self.name, self.MIN_VAL, self.MAX_VAL = self.set_color(color_name)

    def set_color(self, color_name):
        """Return the color to search for."""
        global MIN_VAL, MAX_VAL
        color = color_name
        if color == "green":
            MIN_VAL = np.array([35, 60, 60])
            MAX_VAL = np.array([75, 255, 255])
        elif color == "blue":
            MIN_VAL = np.array([100, 60, 60])
            MAX_VAL = np.array([135, 255, 255])
        return color, MIN_VAL, MAX_VAL

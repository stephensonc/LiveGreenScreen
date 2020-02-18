import numpy as np


class Color:
    name = ""
    min_val = 0
    max_val = 0

    def __init__(self, color_name):
        self.name, self.min_val, self.max_val = self.set_color(color_name)

    def set_color(self, color_name):
        """Return the color to search for."""
        global min_val, max_val
        color = color_name
        if color == "green":
            min_val = np.array([35, 60, 60])
            max_val = np.array([75, 255, 255])
        elif color == "blue":
            min_val = np.array([100, 60, 60])
            max_val = np.array([135, 255, 255])
        return color, min_val, max_val

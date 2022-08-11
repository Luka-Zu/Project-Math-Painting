from PIL import Image
import numpy as np


class Canvas:
    """
    object representing image
    """

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data

    # Method for creating image representation of
    def make(self, location):
        img = Image.fromarray(self.data, 'RGB')
        img.save(location)

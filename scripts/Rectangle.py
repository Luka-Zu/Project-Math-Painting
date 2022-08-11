class Rectangle:
    """
    object representing rectangle
    """

    def __init__(self, x, y, rgb, width, height):
        self.height = height
        self.width = width
        self.rgb = rgb
        self.y = y
        self.__x = x

    def draw(self, canvas):
        # TODO
        pass

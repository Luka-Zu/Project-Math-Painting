class Square:
    """
    object representing square
    """

    def __init__(self, x, y, rgb, length):
        self.length = length
        self.rgb = rgb
        self.y = y
        self.x = x

    def draw(self, canvas):
        if self.x >= canvas.width or self.y >= canvas.height:
            return
        else:
            fill_x_till = min(self.x + self.length, canvas.width)
            fill_y_till = min(self.y + self.length, canvas.height)
            canvas.data[self.x: fill_x_till, self.y: fill_y_till] = self.rgb


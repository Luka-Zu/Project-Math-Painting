import numpy as np
from PIL import Image

from scripts.Canvas import Canvas
from scripts.Rectangle import Rectangle
from scripts.Square import Square

windowX = int(input("Enter picture Width: "))
windowY = int(input("Enter picture Height: "))

# representation off canvas  2D array (X,Y) of which
# elements are 3 element array representing (RGB) color
# of that Pixels (X,Y) color

data = np.zeros((windowX, windowY, 3), dtype=np.uint8)
canvas = Canvas(width=windowY, height=windowY, data=data)

# choosing color of Background
background_color = input("Enter background Color (Black or White): ")
if background_color == "Black":
    data[:] = [0, 0, 0]
else:
    data[:] = [255, 255, 255]

# While loop (Main logic of program)
shall_continue = True
while shall_continue:

    decision = input("Do you want to draw Rectangle or Square: ")

    if decision == "Rectangle":
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        red = int(input("Enter Red: "))
        green = int(input("Enter Green: "))
        blue = int(input("Enter Blue: "))
        rect = Rectangle(x=x, y=y, width=width, height=height, rgb=[red, green, blue])

        rect.draw(canvas=canvas)

    else:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        length = int(input("Enter length: "))
        red = int(input("Enter Red: "))
        green = int(input("Enter Green: "))
        blue = int(input("Enter Blue: "))
        square = Square(x=x, y=y, length=length, rgb=[red, green, blue])

        square.draw(canvas=canvas)

    # ------------------------------------------------------------------------
    check = input('Enter "Quit" if you want to Stop: ')
    if check == "Quit":
        shall_continue = False

# creating image using Pillow library
# creating image out of data array
canvas.make("canvas.png")

import numpy as np
from PIL import Image

windowX = int(input("Enter picture Width: "))
windowY = int(input("Enter picture Height: "))

# representation off canvas  2D array (X,Y) of which
# elements are 3 element array representing (RGB) color
# of that Pixels (X,Y) color

data = np.zeros((windowX, windowY, 3), dtype=np.uint8)

# choosing color of Background
background_color = input("Enter background Color (Black or White): ")
if background_color == "Black":
    data[:] = [0, 0, 0]
else:
    data[:] = [255, 255, 255]

# While loop (Main logic of program)
shall_continue = True
while shall_continue:
    # TODO
    check = input('Enter "Quit" if you want to Stop: ')
    if check == "Quit":
        shall_continue = False

# creating image using Pillow library
# creating image out of data array
img = Image.fromarray(data, 'RGB')

img.save("canvas.png")

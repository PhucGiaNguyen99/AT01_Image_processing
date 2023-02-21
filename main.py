# First step: Given x and y coordinates of a point, return the color of this pixel.
import numpy as np
from PIL import Image

# open the image and convert with mode RGB
pim = Image.open(r"C:\Users\saota\Downloads\sky_2.jpg").convert('RGB')
pixels = pim.load()


def find_pixel_with_color():
    im = np.array(pim)
    # Define the blue color we want to find - PIL uses RGB ordering
    blue = [0, 0, 225]
    # Get all X and Y coordinates of all blue pixels
    X, Y = np.where(np.all(im == blue, axis=2))
    print(X, Y)


def find_RGB_from_coordinates(X, Y):
    image_rgb = pim.getpixel((X, Y))
    return pixels[X, Y]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(find_RGB_from_coordinates(100, 100))

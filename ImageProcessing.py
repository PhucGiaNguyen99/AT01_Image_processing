# First step: Given x and y coordinates of a point, return the color of this pixel.
import argparse

import numpy as np
from PIL import Image

def find_RGB_from_coordinates(file_address, x_coordinate, y_coordinate):
    image = Image.open(file_address, mode='r', formats=None)
    image_rgb = image.convert('RGB')
    pixels_list = image_rgb.load()
    return pixels_list[x_coordinate, y_coordinate]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help="File address")
    parser.add_argument('x_coordinate', type=int, help="X-coordinate of the pixel")
    parser.add_argument('y_coordinate', type=int, help="Y-coordinate of the pixel")
    args = parser.parse_args()

    print(find_RGB_from_coordinates(args.file_name, args.x_coordinate, args.y_coordinate))

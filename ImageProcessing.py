# First step: Given x and y coordinates of a point, return the color of this pixel.
import argparse

import numpy as np
from PIL import Image


def find_RGB_from_coordinates(image_address, x_coordinate, y_coordinate):
    """
    Get RGB value from given x_coordinate and y_coordinate.
    :param image_address: image
    :param x_coordinate:  x_coordinate of the pixel
    :param y_coordinate: y_coordinate of the pixel
    :return: RGB value of the pixel
    """
    image = Image.open(image_address, mode='r', formats=None)
    image_rgb = image.convert('RGB')
    pixels_list = image_rgb.load()
    return pixels_list[x_coordinate, y_coordinate]


def list_of_pixels_from_image(image_address):
    """
    Get list of pixels from given image.
    :param image_address: given image
    :return: list of pixels
    """
    im = Image.open(image_address, mode='r', formats=None)
    im_rgb = im.convert("RGB")
    return list(im_rgb.getdata())


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('file_name', type=str, help="File address")
    # parser.add_argument('x_coordinate', type=int, help="X-coordinate of the pixel")
    # parser.add_argument('y_coordinate', type=int, help="Y-coordinate of the pixel")
    # args = parser.parse_args()

    # print(find_RGB_from_coordinates(args.file_name, args.x_coordinate, args.y_coordinate))

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help="File address")
    args = parser.parse_args()
    pixels_list = list_of_pixels_from_image()
    for p in pixels_list:
        print(p)

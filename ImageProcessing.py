# First step: Given x and y coordinates of a point, return the color of this pixel.
import argparse

import cv2
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


def search_pixel_in_image_using_for_loop(image_address):
    """
    Find coordinates of a pixel in the given image.
    :param image_address: given image to search at
    :return: x, y coordinates of the pixel in the image
    """
    img = cv2.imread(image_address)
    pixel = img[0, 10]  # row coordinate is 0, column coordinate is 10
    print("Pixel is ", pixel)

    for iidx, i in enumerate(img):
        for xidx, x in enumerate(i):
            if (x == pixel).all():
                print(f"SUCCESS - [{iidx} {xidx}")


#   NEED TO LOOK UP HOW TO CHECK A PIXEL
def search_pixel_in_image_using_np_array(image_address):
    img = cv2.imread(image_address)
    pixel = (115, 59, 0)  # row coordinate is 0, column coordinate is 10
    print("Pixel is ", pixel)

    # create an image of just the pixel, having the same size of the image
    # shape return the width and height of the image
    # numpy.tile (A, reps) -> construct an array by repeating A the number of times by reps.
    pixel_tile = np.tile(pixel, (*img.shape[:2], 1))

    # absolute difference of the two images
    diff = np.sum(np.abs(img - pixel_tile), axis=2)

    # print indices
    print("\n".join([f"SUCCESS - {idx}" for idx in np.argwhere(diff == 0)]))


def get_height_of_image(image_address):
    """
    Get width and height of an image.
    :param image_address: given image address
    """
    img = cv2.imread(image_address)
    height, width, _ = img.shape
    print("width: ", width)
    print("height: ", height)


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
    search_pixel_in_image_using_for_loop(args.file_name)
    # get_height_of_image(args.file_name)

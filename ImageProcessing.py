# First step: Given x and y coordinates of a point, return the color of this pixel.
import argparse
import cv2 as cv
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


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
    Get list of all pixels from given image.
    :param image_address: given image
    :return: list of pixels
    """
    im = Image.open(image_address, mode='r', formats=None)
    im_rgb = im.convert("RGB")
    return list(im_rgb.getdata())


def search_pixel_in_image_using_for_loop(image_address):
    """
    Using for loop, find matching points of a point in the image.
    :param image_address: given image to search at
    :return: x, y coordinates of the pixel in the image
    """
    img = cv.imread(image_address)
    pixel = img[0, 10]  # row coordinate is 0, column coordinate is 10
    print("Pixel is ", pixel)

    for iidx, i in enumerate(img):
        for xidx, x in enumerate(i):
            if (x == pixel).all():
                print(f"SUCCESS - [{iidx} {xidx}")


#   NEED TO LOOK UP HOW TO CHECK A PIXEL
def search_pixel_in_image_using_np_array(image_address):
    """
    Using Numpy array, find matching points of a point in the image.
    :param image_address:
    :return:
    """
    img = cv.imread(image_address)
    pixel = (0, 0, 0)  # row coordinate is 0, column coordinate is 0
    print("Pixel is ", pixel)

    # create an image of just the pixel, having the same size of the image
    # shape return the width and height of the image
    # numpy.tile (A, reps) -> construct an array by repeating A the number of times by reps.
    pixel_tile = np.tile(pixel, (*img.shape[:2], 1))

    # absolute difference of the two images
    diff = np.sum(np.abs(img - pixel_tile), axis=2)
    result_list = []
    for idx in np.argwhere(diff == 0):
        idx_tupe = (idx[0], idx[1])
        print("x: ", idx_tupe[0])
        print("y: ", idx_tupe[1])
        print()
    # print(result_list)
    # print indices
    # print("\n".join([f"SUCCESS - {idx}" for idx in np.argwhere(diff == 0)]))


def template_matching(pattern_image, input_image):
    # open two images paths
    matching_pattern_coords = []
    pattern_img = cv.imread(pattern_image)
    input_img = cv.imread(input_image)
    # get width and height of pattern image and input image
    pattern_img_width, pattern_img_height = pattern_img.shape[0], pattern_img.shape[1]

    input_img_width, input_img_height = input_img.shape[0], input_img.shape[1]

    # find the offset which is the size of the pattern image
    offset = pattern_img_height

    # find the top left point of the pattern image in the input image
    top_left_point_pattern = pattern_img[0, 0]

    # find the coords of the matching points of the top_left_pt_pattern
    # pixel_tile = (np.tile(top_left_point_pattern, (*input_img[:2], 1))).all()
    pixel_tile = np.tile(top_left_point_pattern, (*input_img.shape[:2], 1))

    diff = np.sum(np.abs(input_img - pixel_tile), axis=2)
    for matching_point_coords in np.argwhere(diff == 0):
        matching_point_coords_tuple = (matching_point_coords[0], matching_point_coords[1])
        x_matching_pt = matching_point_coords_tuple[0]
        y_matching_pt = matching_point_coords_tuple[1]

        # check if the matching points is within the range
        if (x_matching_pt + offset < input_img_height) and (y_matching_pt + offset < input_img_width):
            for x_extending in range(offset):
                for y_extending in range(offset):
                    # terminate the loop if there's any point unmatched
                    if not (equal_pixels(get_pixel_at_coords(pattern_img, x_extending, y_extending),
                                         get_pixel_at_coords(input_img, x_matching_pt + x_extending,
                                                             y_matching_pt + y_extending))):
                        break
            # Otherwise, add the top left point to matching_pattern_coords
            matching_pattern_coords.append((x_matching_pt, y_matching_pt))
    print(matching_pattern_coords)


def equal_pixels(pixel1, pixel2) -> bool:
    """
    Check if two pixels are equal.
    :param pixel1: RGB value of pixel 1
    :param pixel2: RGB value of pixel 2
    :return: True if two pixels are equal. Otherwise, return False
    """
    return np.all(pixel1 == pixel2)


def find_pixel_coordinates_in_image(image_path):
    """
    Find coords of all matching points of a point in the image.
    :param image_path: given image to find the matching points
    :return: coords of all matching points
    """
    # img = Image.open(image_path, mode='r', formats=None)
    img = cv.imread(image_path)
    pixel = (0, 0, 0)
    indices = np.where(np.all(img == pixel, axis=-1))

    matching_coordinates = list(zip(indices[0], indices[1]))

    print(matching_coordinates)
    # print("matching x-coord: ", matching_coordinates[0])
    # print("matching y-coord: ", matching_coordinates[1])


def get_pixel_of_top_left_point(image_path) -> tuple:
    """
    Find the pixel at the top left position of an image.
    :param image_path: image to find
    :return: the pixel at the top left position
    """
    img = Image.open(image_path, mode='r', formats=None)
    return img.getpixel((0, 0))


def get_pixel_at_coords(img, x_coord, y_coord) -> tuple:
    return img[x_coord, y_coord]


def get_height_of_image(img_path) -> int:
    img = Image.open(img_path, mode='r', formats=None)
    return img.height


def get_width_of_image(img_path) -> int:
    img = Image.open(img_path, mode='r', formats=None)
    return img.width


def template_matching_using_opencv(image, template):
    matching_list = []
    img = cv.imread(image, cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    img2 = img.copy()
    template = cv.imread(template, cv.IMREAD_GRAYSCALE)
    assert template is not None, "file could not be read, check with os.path.exists()"
    w, h = template.shape[::-1]


    method = eval('cv.TM_SQDIFF')

    # Apply template matching
    res = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    top_left = min_loc

    matching_list.append(top_left)
    return matching_list




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str, help="Image path")
    parser.add_argument('template', type=str, help="Template path")
    # parser.add_argument('pattern_image_path', type=str, help="Pattern image path")
    # parser.add_argument('input_image_path', type=str, help="Input image path")
    args = parser.parse_args()
    # template_matching_2(args.o,arg., args.input_image_path)
    print(template_matching_using_opencv(args.image, args.template))

# search_pixel_in_image_using_np_array(args.pattern_image_path, args.input_image_path)

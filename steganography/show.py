import cv2
import sys
import numpy

HEADER_SIZE = 8

def pixel_from_size(size, width):
    """
    """
    i = size // width
    j = size % width
    return i, j

def next_pixel(i, j, width):
    """
    """
    j = j + 1
    if j == width:
        i = i + 1
        j = 0
    return i, j

def merge_byte_from_pixel(pixel):
    """
    """
    r, g, b, a = pixel
    byte = ((r & 3) << 6) | ((g & 3) << 4) | ((b & 3) << 2) | (a & 3)
    return byte

if __name__ == "__main__":
    """
    """
    image = sys.argv[1]

    # open the image
    array = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    height, width, channels = array.shape

    # extract the amount of bytes from the first 8 pixels
    i, j = 0, 0
    index = 0
    slices = []
    while index < HEADER_SIZE:
        slices.append(merge_byte_from_pixel(array[i][j]))
        i, j = next_pixel(i, j, width)
        index = index + 1

    # compute the size from byte slices
    size = 0
    for byte in slices:
        size = (size << 8) | byte

    # output the hidden bytes
    i, j = pixel_from_size(HEADER_SIZE, width)
    index = 0
    while index < size:
        byte = numpy.int8(merge_byte_from_pixel(array[i][j]))
        sys.stdout.buffer.write(byte)
        i, j = next_pixel(i, j, width)
        index = index + 1

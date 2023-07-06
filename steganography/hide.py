import os
import cv2
import sys

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

def graft_byte_on_rgba(byte, pixel):
    """
    """
    shift = 6
    group = []
    for c in range(len(pixel)):
        group.append((byte >> shift) & 3)
        shift = shift - 2
    for c in range(len(pixel)):
        pixel[c] = pixel[c] & 252 | group[c]
    return pixel

if __name__ == "__main__":
    """
    """
    image = sys.argv[1]
    secret = sys.argv[2]

    # open image
    array = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    idata = open(secret, "rb")

    # hide file on image array (two bits per channel in RGBA)
    height, width, channels = array.shape
    i, j = 0, HEADER_SIZE
    byte = idata.read(1)
    while byte:
        byte = byte[0]
        array[i][j] = graft_byte_on_rgba(byte, array[i][j])
        i, j = next_pixel(i, j, width)
        byte = idata.read(1)

    # split the amount of written bytes in 8 bytes
    size = (i * width + j - HEADER_SIZE)
    slices = [0] * HEADER_SIZE
    index = HEADER_SIZE - 1
    while size:
        slices[index] = size & 3
        slices[index] = slices[index] | ((size >> 2) & 3) << 2
        slices[index] = slices[index] | ((size >> 4) & 3) << 4
        slices[index] = slices[index] | ((size >> 6) & 3) << 6

        index = index - 1
        size = size >> 8

    # update the first 8 pixels as the header
    i, j = 0, 0
    index = 0
    while index < HEADER_SIZE:
        array[i][j] = graft_byte_on_rgba(slices[index], array[i][j])
        i, j = next_pixel(i, j, width)
        index = index + 1

    # write the image
    cv2.imwrite(os.path.basename(secret) + '.png', array)

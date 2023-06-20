import cv2
import sys

def merge_byte(r, g, b, a):
    """
    """
    return ((r & 3) << 6) | ((g & 3) << 4) | ((b & 3) << 2) | (a & 3)

if __name__ == "__main__":
    """
    """
    image = sys.argv[1]

    array = cv2.imread(image, cv2.IMREAD_UNCHANGED)

    height, width, channels = array.shape
    i, j = 0, 0
    for i in range(height):
        for j in range(width):
            r, g, b, a = array[i][j]
            print(bin(merge_byte(r, g, b, a)), merge_byte(r, g, b, a))

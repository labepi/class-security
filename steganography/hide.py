import cv2
import sys

def split_byte(byte):
    """
    """
    return byte >> 6 & 3, byte >> 4 & 3, byte >> 2 & 3, byte & 3

if __name__ == "__main__":
    """
    """
    image = sys.argv[1]
    secret = sys.argv[2]

    array = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    idata = open(secret, "rb")

    height, width, channels = array.shape
    i, j = 0, 0
    byte = idata.read(1)
    while byte:
        byte = byte[0]
        r, g, b, a = array[i][j]
        slices = split_byte(byte)

        r = r & 252 | slices[0]
        g = g & 252 | slices[1]
        b = b & 252 | slices[2]
        a = a & 252 | slices[3]
        array[i][j] = [r, g, b, a]

        j = j + 1
        if j == width:
            i = i + 1
            j = 0

        byte = idata.read(1)

    cv2.imwrite('secret.png', array)

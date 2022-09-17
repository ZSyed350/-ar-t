import cv2
import numpy as np

SRC = "img_in/llama.jpg"
OUT = "img_out/llama.jpg"


def gen_canny(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # convert to gray
    img = cv2.GaussianBlur(img, (5, 5), 0)  # apply gaussian blur to soften edges
    canny = cv2.Canny(img, 50, 150)  # apply canny edge detection
    canny = cv2.bitwise_not(canny)  # flip white and black so lines are black
    return canny


def transparent_background(img):
    # FIXME: returned np.array is as expected, but the image background is not transparent.
    #  may be an issue with the saving method, maybe there is a way to specify color space?

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)  # convert to format that includes alpha (opacity) channel

    for row in img:
        for pixel in row:  # for each pixel, check if white (BGR = 255)
            if (pixel[0] == 255) and (pixel[1] == 255) and (pixel[2] == 255):
                pixel[3] = 0
    return img  # if pixel white, set alpha to 0


if __name__ == "__main__":
    img = cv2.imread(SRC)
    img_lines = gen_canny(img)
    cv2.imwrite(OUT, img_lines)
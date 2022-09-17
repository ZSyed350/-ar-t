import canny
import color_block
import os
import cv2


# GLOBAL VARIABLES
IMG_NAME = "kim_namjoon.jpg"  # include extension
IN = "img_in"
OUT = "img_out"
SRC_IMG = os.path.join(IN, IMG_NAME)
PATH_OG = os.path.join(OUT, IMG_NAME.split('.')[0] + '_original.jpg')
PATH_CANNY = os.path.join(OUT, IMG_NAME.split('.')[0] + '_canny.jpg')
PATH_COLOR = os.path.join(OUT, IMG_NAME.split('.')[0] + '_color.jpg')
NUM_COLORS = 7


if __name__ == "__main__":
    img = cv2.imread(SRC_IMG)
    canny = canny.gen_canny(img)
    colors = color_block.color_block(img, NUM_COLORS)

    # EXPORTS
    cv2.imwrite(PATH_OG, img)
    cv2.imwrite(PATH_CANNY, canny)
    cv2.imwrite(PATH_COLOR, colors)
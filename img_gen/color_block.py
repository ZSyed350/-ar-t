import numpy as np
import cv2

SRC = "img_in/pengu.jpg"
OUT = "img_out/pengu_color.jpg"
NUM_COLORS = 8

def color_block(img, num_colors):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    Z = img.reshape((-1, 3))
    Z = np.float32(Z)  # convert to np.float32
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)  # algo criteria
    ret, label, center = cv2.kmeans(Z, num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)  # apply kmeans

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    return res2


if __name__ == "__main__":
    img = cv2.imread(SRC)
    img_colors = color_block(img, NUM_COLORS)
    cv2.imwrite(OUT, img_colors)

    cv2.imshow('img color blocked', img_colors)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
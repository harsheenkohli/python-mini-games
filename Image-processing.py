# CCTV => Low quality => Image processed
# Images usually processed as matrices

from PIL import Image
import cv2  # for image enhancement

# flipping the image => transposing
img = Image.open('Newspaper.jpg')

# transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# save to a file in human understandable format
transposed_img.save('Corrected.png')  # write proper path

# read the image
img = cv2.imread('Corrected.png')

# CLAHE : Contrast Limited Adaptive Histogram Equalisation

# Preparation for CLAHE
clahe = cv2.createCLAHE()

# convert to grey-scale image
enh_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # in matrix form

# apply enhancement
enh_img = clahe.apply(enh_img)     # in matrix form

# save output
cv2.imwrite('enhanced.png', enh_img)

print("Done enhancing!")

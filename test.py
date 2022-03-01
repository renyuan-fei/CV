import numpy as np
from skimage import io

img_io = io.imread ('./assignment1/a1/images/cat.jpg')

np_img = np.array (img_io/255)

print (np_img)

print (np_img.shape)

# 裁剪

crop_img = np_img[100:200:1, 100:300:1]

print (crop_img.shape)

print (crop_img)

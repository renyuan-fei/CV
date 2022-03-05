import numpy as np
from skimage import io
from a1code import *
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10.0, 8.0)  # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


def display (img, caption=''):
    # Show image using pyplot
    plt.figure ()
    plt.imshow (img)
    plt.title (caption)
    plt.axis ('off')
    plt.show ()


# 1

image1 = load ('images/cat.jpg')

display (image1, 'cat')

print_stats (image1)

# 2

# crop_img = crop(image1, 205, 5, 502, 202)
# display(crop_img)
# print_stats(crop_img)
#
# resize_img = resize(crop_img, 4.5, 4.5 )
# display(resize_img)
# print_stats(resize_img)
#
# contrast_img = change_contrast(image1, 0.5)
# display(contrast_img)
# print_stats(contrast_img)
#
# grey_img = greyscale (image1)
# display(grey_img)
# print_stats(grey_img)
#
# binary_img = binary(grey_img, 0.3)
# display(binary_img)
# print_stats(binary_img)
#
# binary_img = binary(grey_img, 0.7)
# display(binary_img)
# print_stats(binary_img)

kernel_verticl = np.array (
        [
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]
            ]
        )

kernel = np.array (
        [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
            ]
        )

test_img = np.zeros ((9, 9))
test_img[3:6, 3:6] = 1
display (test_img)
print(test_img)
print ("\n")

test_output = conv2D (test_img, kernel)
display (test_output)
print ("我的结果：")
print (test_output)
print ("\n")
expected_output = np.zeros ((9, 9))
expected_output[2:7, 2:7] = 1
expected_output[5:, 5:] = 0
expected_output[4, 2:5] = 2
expected_output[2:5, 4] = 2
expected_output[4, 4] = 3
display (expected_output)
print ("期望结果：")
print (expected_output)
print ("\n")

# assert np.max (test_output - expected_output) < 1e-10

# 临时用测试
# test_output = conv2D (grey_img, kernel_verticl)
# display(test_output)
# print_stats(test_output)
#
# temp = test_output - grey_img
# display(temp)
# # coding: utf-8
import numpy as np
from a1code import *
import matplotlib.pyplot as plt

img = load ('images/cat.jpg')

def display(img, caption=''):
    # Show image using pyplot
    plt.figure()
    plt.imshow(img)
    plt.title(caption)
    plt.axis('off')
    plt.show()

#
# arr = np.arange(12).reshape((3, 4))
# print ('array is:')
# print (arr)
#
# # 取第一维的索引 1 到索引 2 之间的元素，也就是第二行
# # 取第二维的索引 1 到索引 3 之间的元素，也就是第二列和第三列
# slice_one = arr[1:2+1, 1:3+1]
# print ('first slice is:')
# print (slice_one, slice_one.shape)
#
# # 取第一维的全部
# # 按步长为 2 取第二维的索引 0 到末尾 之间的元素，也就是第一列和第三列
# slice_two = arr[:, ::2]
# print ('second slice is:')
# print (slice_two)
RGB_image = np.array (
        [
            [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
            [[4, 4, 4], [5, 5, 5], [6, 6, 6]],
            [[7, 7, 7], [8, 8, 8], [9, 9, 9]]
            ]
        )
# image = np.array (
#         [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]
#             ]
#         )
#
kernel = np.array (
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 0]
            ]
        )
#
kernel_vertical = np.array (
        [
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1]
            ]
        )

# # print (np.sum (np.multiply (kernel,array)))
# #
# # print (np.dot (kernel,array))
#
# height, width = array.shape
#
# zero_array = np.zeros ((1, width))
# print (zero_array)
#
# # 上下
# array = np.insert (array, 0, [0], axis=0)
# array = np.insert (array, width + 1, [0], axis=0)
#
# # 左右
# array = np.insert (array, 0, [0], axis=1)
# array = np.insert (array, height + 1, [0], axis=1)
#
# print (array)


# SHAPE = image.shape
#
# if (len(SHAPE) == 3):
#     print('3D')
# else:
#     print('3D')

# my_shape = img.shape
#
# new_height = int(my_shape[0] * 0.5)
# new_width = int(my_shape[1] * 0.5)
#
# new_img = np.resize (img, (new_height, new_width, 3))
# temp = np.array (new_img)
# display(new_img)

# ker_height, ker_width = kernel.shape
#
# temp = np.zeros ((ker_height, ker_width))
# x = ker_height - 1
# y = ker_width - 1
#
# for i in range (ker_height - 1):
#     x = x - 1
#     for j in range (ker_width - 1):
#         temp[i, j] = kernel[x, y]
#         y = y - 1
#
# y = ker_width
#
# print (temp)


# # rgb图像边缘填充
#
# height, width, channel = RGB_image.shape
#
# print(RGB_image.shape)
#
# # for i in range (0,channel - 1):
# #     # 上下
# #     RGB_image = np.insert (RGB_image[:, :, i], 0, [0], axis=0)
# #     RGB_image = np.insert (RGB_image[:, :, i], height + 1, [0], axis=0)
# #
# #     # 左右
# #     RGB_image = np.insert (RGB_image[:, :, i], 0, [0], axis=1)
# #     RGB_image = np.insert (RGB_image[:, :, i], width + 1, [0], axis=1)
#
# # 上下
# RGB_image = np.insert (RGB_image, 0, [0], axis=0)
# RGB_image = np.insert (RGB_image, height + 1, [0], axis=0)
#
# # 左右
# RGB_image = np.insert (RGB_image, 0, [0], axis=1)
# RGB_image = np.insert (RGB_image, width + 1, [0], axis=1)
#
# print(RGB_image.shape)
# print (RGB_image)


# rgb图像卷积
# out = RGB_conv(RGB_image, kernel)
# print(out)
# display(out)

# out1 = RGB_conv(img, kernel)
#
# display(out1)

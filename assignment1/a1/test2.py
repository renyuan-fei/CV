# # coding: utf-8
import numpy as np
from a1code import *
import matplotlib.pyplot as plt

image1 = load ('images/cat.jpg')


def display (img, caption=''):
    # Show image using pyplot
    plt.figure ()
    plt.imshow (img)
    plt.title (caption)
    plt.axis ('off')
    plt.show ()


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
# RGB_image = np.array (
#         [
#             [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
#             [[4, 4, 4], [5, 5, 5], [6, 6, 6]],
#             [[7, 7, 7], [8, 8, 8], [9, 9, 9]]
#             ]
#         )
image = np.array (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
        )

height, width = image.shape

# kernel = np.array (
#         [
#             [1, 0, 1],
#             [0, 0, 0],
#             [1, 0, 0]
#             ]
#         )
# #
# kernel_vertical = np.array (
#         [
#             [1, 1, 1],
#             [0, 0, 0],
#             [-1, -1, -1]
#             ]
#         )

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

# print_stats(img)
# i'
# temp = resize (img, 0.125, 0.125)
# print_stats(temp)

# new_img = resize (img, 8, 8)
# display(new_img)

# gauss_kernel = (16) * gauss2D (3, 4)
# print (gauss_kernel)

# # gradients
# # negative
# kernel_vertical1 = np.array (
#         [
#             [1, 1, 1],
#             [0, 0, 0],
#             [-1, -1, -1]
#             ]
#         )
#
# kernel_horizontal1 = np.array (
#         [
#             [1, 0, -1],
#             [1, 0, -1],
#             [1, 0, -1]
#             ]
#         )
#
# print("positive gradients")
# positive_gradient_img = conv (grey_img, kernel_vertical1) + conv (grey_img, kernel_horizontal1)
# display(positive_gradient_img)
# print_stats(positive_gradient_img)
#
# # positive
# kernel_vertical2 = np.array (
#         [
#             [-1, -1, -1],
#             [0, 0, 0],
#             [1, 1, 1]
#             ]
#         )
#
# kernel_horizontal2 = np.array (
#         [
#             [-1, 0, 1],
#             [-1, 0, 1],
#             [-1, 0, 1]
#             ]
#         )
#
# print("positive gradient")
# negative_gradient_img = conv (grey_img, kernel_vertical2) + conv (grey_img, kernel_horizontal2)
# display(negative_gradient_img)
# print_stats(negative_gradient_img)


# kernel = np.array (
#         [
#             [1, 2, 3, 4, 5, 6],
#             [4, 5, 6, 7, 8, 9],
#             [7, 8, 9, 10, 11, 12],
#             [7, 8, 9, 10, 11, 12],
#             [7, 8, 9, 10, 11, 12]
#             ]
#         )

# 获取kernel的 height 和 width
# ker_height, ker_width = kernel.shape

# 反转kernel
# for i in range (ker_height - 1):
#     for j in range (ker_width - i - 1):
#         temp = kernel[i, j]
#         kernel[i, j] = kernel[ker_height - j - 1, ker_width - i - 1]
#         kernel[ker_height - j - 1, ker_width - i - 1] = temp
#
# print(kernel)

# out = np.flip(kernel, axis=0)
# out1 = np.flip(out, axis=1)
# print(out1)

# print_stats (image)
#
# for i in range (int (ker_height / 2)):
#     image = np.insert (image, 0, [0], axis=0)
#     image = np.insert (image, height + i + 1, [0], axis=0)
#
# # 左右
# for i in range (int (ker_width / 2)):
#     image = np.insert (image, 0, [0], axis=1)
#     image = np.insert (image, width + i + 1, [0], axis=1)
#
# print_stats (image)
# print (image)

# temp1 = resize (img, 0.5, 0.5)
# display (temp1)
#
# temp2 = resize (temp1, 0.5, 0.5)
# display (temp2)
#
# temp3 = resize (temp2, 0.5, 0.5)
# display (temp3)

# print(np.flip(image))

# gauss_kernel1 = gauss2D (5, 10)
#
# gauss_img1 = conv (image1, gauss_kernel1)
# display(gauss_img1)
# display(image1)
# display ((image1 - gauss_img1))
# print_stats (image1 - gauss_img1)
# temp1 = image1 - gauss_img1
# print(temp1)
#
# resize_img = resize(image1,0.5,0.5)
# gauss_img2 = conv (resize_img, gauss_kernel1)
# display(gauss_img2)
# display(resize_img)
# display ((resize_img - gauss_img2))
# print_stats (resize_img - gauss_img2)
# temp2 = resize_img - gauss_img2
# print(temp2)
#
# temp3 = resize(temp1,0.5,0.5)
# display(temp3 - temp2)
# print(temp3 - temp2)



# # create a gauss kernel
# gauss_kernel = gauss2D (3, 200)
#
# # I1
# gauss_img1 = conv (image1, gauss_kernel)
# image_I1 = resize (gauss_img1, 0.5, 0.5)
# display (image_I1,"I1")
# print_stats (image_I1)
#
# # I2
# gauss_img2 = conv (image_I1, gauss_kernel)
# image_I2 = resize (gauss_img2, 0.5, 0.5)
# display (image_I2,"I2")
# print_stats (image_I2)
#
# # I3
# gauss_img3 = conv (image_I2, gauss_kernel)
# image_I3 = resize (gauss_img3, 0.5, 0.5)
# display (image_I3,"I3")
# print_stats (image_I3)
#
# # I4
# gauss_img4 = conv (image_I3, gauss_kernel)
# image_I4 = resize (gauss_img4, 0.5, 0.5)
# display (image_I4,"I4")
# print_stats (image_I4)
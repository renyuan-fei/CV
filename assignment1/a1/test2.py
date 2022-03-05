# # coding: utf-8
import numpy as np

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


# array = np.array (
#         [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]
#             ]
#         )
#
# kernel = np.array (
#         [
#             [0, 1, 2],
#             [2, 2, 0],
#             [0, 1, 2]
#             ]
#         )
#
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

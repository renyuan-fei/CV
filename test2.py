# coding: utf-8
import numpy as np

arr = np.arange(12).reshape((3, 4))
print ('array is:')
print (arr)

# 取第一维的索引 1 到索引 2 之间的元素，也就是第二行
# 取第二维的索引 1 到索引 3 之间的元素，也就是第二列和第三列
slice_one = arr[1:2+1, 1:3+1]
print ('first slice is:')
print (slice_one, slice_one.shape)

# 取第一维的全部
# 按步长为 2 取第二维的索引 0 到末尾 之间的元素，也就是第一列和第三列
slice_two = arr[:, ::2]
print ('second slice is:')
print (slice_two)

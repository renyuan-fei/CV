# string = './A2_smvs/book_covers/Query\001.jpg'
#
# print (string[-5:-4])
# print ('\001')
#
# if string[-5:-4] == '\001':
#     print('True')
#
# print ('\\' + '001')
#
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print (str.split( ))       # 以空格为分隔符，包含 \n
# print (str.split(' ', 1 )) # 以空格为分隔符，分隔成两个

# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
#
# print(d['a'][0])
# print(d['a'][1])

import re

my_re = r'./A2_smvs/.*/.*/[0-9]{3}.jpg'
my_re3 = r'[0-9]{3}'

my_test = './A2_smvs/book_covers/Query/001.jpg'
my_test2 = './A2_smvs/book_covers/Reference/001.jpg'
my_test3 = '123'

# print(re.search (my_re2, my_test2))
# print(re.search (r'[0-9]{3}', '123').span())
if re.match (my_re, my_test):
    print (True)

if re.match (my_re, my_test2):
    print (True)

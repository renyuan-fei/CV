import re
# 可映射多个值的字典
from collections import defaultdict

from my_function import *


# if __name__ == '__main__':
#     INPUT1 = [1000, 6000, 1000, 700, 862, 2, 'book_covers']
#     best_match_test (INPUT1)
#
#     print('---------------------------------------------------------------------------------------------------------\n')
#
#     INPUT2 = [1000, 6000, 1000, 700, 862, 2, 'landmarks']
#     best_match_test (INPUT2)
# museum[0.6153846153846154, 4000, 0.766]
# book TEST:194     Accuracy: 0.9702970297029703     feature:  3000     ratio:  0.762
# ----------------------------------------------------------------------------------------------------------------------


def match_score (path, image='', is_extra_picture=False, one_img=False, num_not_repeat=True, is_result_show=True,
                 feature=500,
                 ratio=0.8,
                 k=1):
    if image != '':
        one_img = True

    threshold = 30

    Reference_paths = []
    Query_paths = []

    Reference = []
    Query = []

    temp = []

    if is_extra_picture:
        # 匹配任何内容
        my_re = r'.*'
    else:
        # 正则表达式，仅匹配原有的数据集
        my_re = r'[0-9]{3}'

    # 读取一个Query，用所有Reference进行匹配
    if one_img:
        # 读取Query
        Query.append (cv2.imread (f'./A2_smvs/{path}/Query/{image}.jpg', cv2.IMREAD_GRAYSCALE))
    else:
        # 获取Query图片路径
        Query_paths = glob.glob (f'./A2_smvs/{path}/Query/*.jpg')
        Query_paths.sort ()
        # 读取图片
        for path1 in Query_paths:
            if re.match (my_re, path1[-7:-4]):
                Query.append (cv2.imread (path1, cv2.IMREAD_GRAYSCALE))

    # 获取Reference图片路径
    Reference_paths = glob.glob (f'./A2_smvs/{path}/Reference/*.jpg')
    Reference_paths.sort ()
    # 读取图片
    for path2 in Reference_paths:
        if re.match (my_re, path2[-7:-4]):
            Reference.append (cv2.imread (path2, cv2.IMREAD_GRAYSCALE))

    # print(len(Query))
    # print(len(Reference))
    #
    # print(Reference[0])

    # 创建ORB特征提取器
    orb = cv2.ORB_create (nfeatures=feature)

    # 判断是否是第一次循环
    key = True
    count1 = 0

    success_count = 0

    temp_count = 0

    for i in Query:
        # 是否找到结果
        is_success = False

        # 创建dict,储存（匹配个数，图片名称）
        my_dict = defaultdict (list)
        # 创建list，储存匹配个数(之后需要要排序)
        my_match = []

        max_score = 0
        count2 = 0

        kp1, des1 = orb.detectAndCompute (i, None)

        # 获取Query图片的名称
        if one_img:
            p1 = image
            count1 = 1
        else:
            p1 = Query_paths[count1][-7:-4]
            count1 += 1

        if key:
            for j in Reference:
                is_not_in_dataset = True

                # 检测关键点
                # 计算描述符
                kp2, des2 = orb.detectAndCompute (j, None)

                # create BFMatcher object
                bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)

                matches = bf.knnMatch (des2, des1, 2)

                # 将des2存储,后面节约计算时间
                temp.append ([des2, kp2])

                # 筛选匹配项(ratio_test,ratio=0.8)
                # 创建子集，并以list的形式存入(一个只包含一个值的list)
                good_match = []
                good_without_list = []

                for (x, y) in matches:
                    if x.distance < ratio * y.distance:
                        good_match.append ([x])
                        good_without_list.append (x)

                if len (good_match) > 4:
                    M, Mask = findHomography (kp2, kp1, good_without_list, True)

                    if len (Mask) > max_score:
                        max_score = len (Mask)
                        p2 = Reference_paths[count2][-7:-4]

                    # 储存 {match:p2}
                    my_dict[len (Mask)].append (Reference_paths[count2][-7:-4])

                    # 储存 [match]
                    my_match.append (len (Mask))

                    if p1 == Reference_paths[count2][-7:-4]:
                        is_not_in_dataset = False

                count2 += 1

            key = False

        else:
            is_not_in_dataset = True

            for ref in temp:
                bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)

                # 用储存的 des2 进行匹配，节约计算时间
                matches = bf.knnMatch (ref[0], des1, 2)

                # 筛选匹配项(ratio_test,ratio=0.8)
                # 创建子集，并以list的形式存入(一个只包含一个值的list)
                good_match = []
                good_without_list = []

                for (x, y) in matches:
                    if x.distance < ratio * y.distance:
                        good_match.append ([x])
                        good_without_list.append (x)

                M, Mask = findHomography (ref[1], kp1, good_without_list, True)

                if len (Mask) > max_score:
                    max_score = len (Mask)
                    p2 = Reference_paths[count2][-7:-4]

                # 储存 {match:[p2]}
                my_dict[len (Mask)].append (Reference_paths[count2][-7:-4])

                # 储存 [match]
                my_match.append (len (Mask))

                if p1 == Reference_paths[count2][-7:-4]:
                    is_not_in_dataset = False

                count2 += 1

        # 对my_match进行降序排序
        my_match.sort (reverse=True)

        loop = k

        # 确定循环的次数(相同数字的不算)
        if num_not_repeat:
            new_key = 0
            temp_key = k

            for n in range (1, len (my_match)):
                if temp_key == 0:
                    break
                elif my_match[n] != my_match[n - 1]:
                    temp_key -= 1
                    new_key += 1
                else:
                    new_key += 1
            loop = new_key
            # print ('new_key', new_key)
        #
        # print(my_match)
        # print(my_dict)
        # print('\n')

        # 遍历前k个元素
        for val in range (0, loop):
            # print(my_match[val])
            # print(my_dict[my_match[val]])

            # 调用my_dict,查看其中是否有名字相同的结果
            for x in my_dict[my_match[val]]:
                # print(x)
                if p1 == x:
                    is_success = True
                    max_score = my_match[val]
                    p2 = x

        # print(len(my_match))
        # print('\n')

        if max_score > threshold and is_success:
            success_count += 1
        elif is_success == False and is_not_in_dataset == True:
            success_count += 1

        if is_result_show:
            temp_count += 1
            if max_score > threshold and is_success:
                print ('match successfully:', '<', p1, ' ', p2, '> ', max_score, '\n')
            elif is_success == False and is_not_in_dataset == True:
                print ('not in dataset:    ', '<', p1, ' ', p2, '> ', max_score, '\n')
            elif max_score > threshold and is_success == False:
                print ('match failed:      ', '<', p1, ' ', p2, '> ', max_score, '\n')

    print ('Accuracy: ', float (success_count / count1) * 100, '%')


if __name__ == '__main__':
    match_score ('book_covers', '001')

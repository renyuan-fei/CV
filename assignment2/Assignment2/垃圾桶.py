# def match_score_temp (path, image='', one_by_more=False, threshold=100):
#     if image != '':
#         one_by_more = True
#
#     Reference_paths = []
#     Query_paths = []
#
#     Reference = []
#     Query = []
#
#     temp = []
#
#     # 读取一个reference，用所有query进行匹配
#     if one_by_more:
#         # 读取Reference
#         Reference.append (cv2.imread ('./A2_smvs/' + path + '/Reference/' + image + '.jpg', cv2.IMREAD_GRAYSCALE))
#     else:
#         # 获取Reference图片路径
#         Reference_paths = glob.glob ('./A2_smvs/' + path + '/Reference/*.jpg')
#         Reference_paths.sort ()
#         # 读取图片
#         for path1 in Reference_paths:
#             Reference.append (cv2.imread (path1, cv2.IMREAD_GRAYSCALE))
#
#     # 获取Query图片路径
#     Query_paths = glob.glob ('./A2_smvs/' + path + '/Query/*.jpg')
#     Query_paths.sort ()
#     # 读取图片
#     for path2 in Query_paths:
#         Query.append (cv2.imread (path2, cv2.IMREAD_GRAYSCALE))
#
#     # print(len(Reference))
#     # print(len(Query))
#
#     # print (len (Reference_paths))
#     # print (len (Query_paths))
#
#     # print(Query_paths[0])
#
#     # 创建ORB特征提取器
#     orb = cv2.ORB_create ()
#
#     # 判断是否是第一次循环
#     key = True
#     count1 = 0
#
#     success_count = 0
#
#     for i in Reference:
#         max_score = 0
#         count2 = 0
#
#         kp1 = orb.detect (i, None)
#         kp1, des1 = orb.compute (i, kp1)
#
#         # 获取Reference图片的名称
#         if one_by_more:
#             p1 = image
#             count1 = 1
#         else:
#             p1 = Reference_paths[count1][-7:-4]
#             count1 += 1
#
#         if key:
#             for j in Query:
#                 # 检测关键点
#                 kp2 = orb.detect (j, None)
#                 # 计算描述符
#                 kp2, des2 = orb.compute (j, kp2)
#
#                 # create BFMatcher object
#                 bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)
#
#                 matches = bf.knnMatch (des1, des2, k=2)
#
#                 # 将des2存储,后面节约计算时间
#                 temp.append (des2)
#
#                 # 筛选匹配项(ratio_test,ratio=0.8)
#                 # 创建子集，并以list的形式存入(一个只包含一个值的list)
#                 good_match = []
#
#                 for (x, y) in matches:
#                     if x.distance < 0.8 * y.distance:
#                         good_match.append ([x])
#
#                 if len (good_match) > max_score:
#                     max_score = len (good_match)
#                     p2 = Query_paths[count2][-7:-4]
#
#                 count2 += 1
#
#             key = False
#
#         else:
#             for des2 in temp:
#                 bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)
#
#                 # 用储存的 des2 进行匹配，节约计算时间
#                 matches = bf.knnMatch (des1, des2, k=2)
#
#                 # 筛选匹配项(ratio_test,ratio=0.8)
#                 # 创建子集，并以list的形式存入(一个只包含一个值的list)
#                 good_match = []
#
#                 for (x, y) in matches:
#                     if x.distance < 0.8 * y.distance:
#                         good_match.append ([x])
#
#                 if len (good_match) > max_score:
#                     max_score = len (good_match)
#                     p2 = Query_paths[count2][-7:-4]
#
#                 count2 += 1
#         # print(max_score, '\n')
#
#         if max_score > threshold and p1 == p2:
#             print ('match successfully:', '<', p1, ' ', p2, '> ', max_score, '\n')
#             success_count += 1
#         else:
#             print ('match failed:', '<', p1, ' ', p2, '> ', max_score, '\n')
#
#     print ('Accuracy: ', float (success_count / count1) * 100, '%')














# ----------------------------------------------------------------------------------------------------------------------

# def match_score (path, image='', one_by_more=False, threshold=60, min_threshod=10):
#     if image != '':
#         one_by_more = True
#
#     Reference_paths = []
#     Query_paths = []
#
#     Reference = []
#     Query = []
#
#     temp = []
#
#     # 读取一个reference，用所有query进行匹配
#     if one_by_more:
#         # 读取Reference
#         Query.append (cv2.imread ('./A2_smvs/' + path + '/Query/' + image + '.jpg', cv2.IMREAD_GRAYSCALE))
#     else:
#         # 获取Reference图片路径
#         Query_paths = glob.glob ('./A2_smvs/' + path + '/Query/*.jpg')
#         Query_paths.sort ()
#         # 读取图片
#         for path1 in Query_paths:
#             Query.append (cv2.imread (path1, cv2.IMREAD_GRAYSCALE))
#
#     # 获取Query图片路径
#     Reference_paths = glob.glob ('./A2_smvs/' + path + '/Reference/*.jpg')
#     Reference_paths.sort ()
#     # 读取图片
#     for path2 in Reference_paths:
#         Reference.append (cv2.imread (path2, cv2.IMREAD_GRAYSCALE))
#
#     # print(len(Query))
#     # print(len(Reference))
#     #
#     # print (len (Query_paths))
#     # print (len (Reference_paths))
#
#     # print(Query_paths[0])
#
#     # 创建ORB特征提取器
#     orb = cv2.ORB_create ()
#
#     # 判断是否是第一次循环
#     key = True
#     count1 = 0
#
#     success_count = 0
#
#     for i in Query:
#         max_score = 0
#         count2 = 0
#
#         kp1 = orb.detect (i, None)
#         kp1, des1 = orb.compute (i, kp1)
#
#         # 获取Query图片的名称
#         if one_by_more:
#             p1 = image
#             count1 = 1
#         else:
#             p1 = Query_paths[count1][-7:-4]
#             count1 += 1
#
#         if key:
#             for j in Reference:
#                 # 检测关键点
#                 kp2 = orb.detect (j, None)
#                 # 计算描述符
#                 kp2, des2 = orb.compute (j, kp2)
#
#                 # create BFMatcher object
#                 bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)
#
#                 matches = bf.knnMatch (des2, des1, k=2)
#
#                 # 将des2存储,后面节约计算时间
#                 temp.append (des2)
#
#                 # 筛选匹配项(ratio_test,ratio=0.8)
#                 # 创建子集，并以list的形式存入(一个只包含一个值的list)
#                 good_match = []
#
#                 for (x, y) in matches:
#                     if x.distance < 0.8 * y.distance:
#                         good_match.append ([x])
#
#                 if len (good_match) > max_score:
#                     max_score = len (good_match)
#                     p2 = Reference_paths[count2][-7:-4]
#
#                 count2 += 1
#
#             key = False
#
#         else:
#             for des2 in temp:
#                 bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)
#
#                 # 用储存的 des2 进行匹配，节约计算时间
#                 matches = bf.knnMatch (des1, des2, k=2)
#
#                 # 筛选匹配项(ratio_test,ratio=0.8)
#                 # 创建子集，并以list的形式存入(一个只包含一个值的list)
#                 good_match = []
#
#                 for (x, y) in matches:
#                     if x.distance < 0.8 * y.distance:
#                         good_match.append ([x])
#
#                 if len (good_match) > max_score:
#                     max_score = len (good_match)
#                     p2 = Reference_paths[count2][-7:-4]
#
#                 count2 += 1
#         # print(max_score, '\n')
#
#         if max_score > threshold and p1 == p2:
#             print ('match successfully:', '<', p1, ' ', p2, '> ', max_score, '\n')
#             success_count += 1
#         elif threshold > max_score > min_threshod or p1 != p2:
#             print ('match failed:', '<', p1, ' ', p2, '> ', max_score, '\n')
#         elif max_score < min_threshod and p1 != p2:
#             print ('not in dataset:', '<', p1, ' ', p2, '> ', max_score, '\n')
#
#     print ('Accuracy: ', float (success_count / count1) * 100, '%')
#
#
# ----------------------------------------------------------------------------------------------------------------------
#
# from collections import defaultdict
# import re
#
#
# def match_score_GMSmatch (path, image='', one_img=False, num_not_repeat=True, is_result_show=True, ratio=0.8,
#                           threshold=0,
#                           k=1):
#     if image != '':
#         one_img = True
#
#     Reference_paths = []
#     Query_paths = []
#
#     Reference = []
#     Query = []
#
#     temp = []
#
#     # 正则表达式，仅匹配原有的数据集
#     my_re = r'[0-9]{3}'
#
#     # 读取一个Query，用所有Reference进行匹配
#     if one_img:
#         # 读取Query
#         Query.append (cv2.imread ('./A2_smvs/' + path + '/Query/' + image + '.jpg', cv2.IMREAD_GRAYSCALE))
#     else:
#         # 获取Query图片路径
#         Query_paths = glob.glob ('./A2_smvs/' + path + '/Query/*.jpg')
#         Query_paths.sort ()
#         # 读取图片
#         for path1 in Query_paths:
#             if re.match (my_re, path1[-7:-4]):
#                 Query.append (cv2.imread (path1, cv2.IMREAD_GRAYSCALE))
#
#     # 获取Reference图片路径
#     Reference_paths = glob.glob ('./A2_smvs/' + path + '/Reference/*.jpg')
#     Reference_paths.sort ()
#     # 读取图片
#     for path2 in Reference_paths:
#         if re.match (my_re, path2[-7:-4]):
#             Reference.append (cv2.imread (path2, cv2.IMREAD_GRAYSCALE))
#
#     # 创建ORB特征提取器
#     orb = cv2.ORB_create (10000)
#
#     # 判断是否是第一次循环
#     key = True
#     count1 = 0
#
#     success_count = 0
#
#     # temp_count = 0
#
#     for i in Query:
#         # 是否找到结果
#         is_success = False
#
#         # 创建dict,储存（匹配个数，图片名称）
#         my_dict = defaultdict (list)
#         # 创建list，储存匹配个数(之后需要要排序)
#         my_match = []
#
#         max_score = 0
#         count2 = 0
#
#         kp1, des1 = orb.detectAndCompute (i, None)
#
#         # 获取Query图片的名称
#         if one_img:
#             p1 = image
#             count1 = 1
#         else:
#             p1 = Query_paths[count1][-7:-4]
#             count1 += 1
#
#         if key:
#             for j in Reference:
#                 # 检测关键点
#                 # 计算描述符
#                 kp2, des2 = orb.detectAndCompute (j, None)
#
#                 # create BFMatcher object
#                 bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)
#
#                 matches = bf.match (des2, des1)
#
#                 matches_GMS = matchGMS (
#                         j.shape[:2], i.shape[:2], kp2, kp1, matches, withScale=False, withRotation=False,
#                         thresholdFactor=6
#                         )
#
#                 # 将des2存储,后面节约计算时间
#                 temp.append ([j, des2, kp2])
#
#                 if len (matches_GMS) > max_score:
#                     max_score = len (matches_GMS)
#                     p2 = Reference_paths[count2][-7:-4]
#
#                 # 储存 {match:p2}
#                 my_dict[len (matches_GMS)].append (Reference_paths[count2][-7:-4])
#
#                 # 储存 [match]
#                 my_match.append (len (matches_GMS))
#
#                 count2 += 1
#
#             key = False
#
#         else:
#             for memory in temp:
#                 bf = cv2.BFMatcher (cv2.NORM_HAMMING, crossCheck=False)
#
#                 # 用储存的 des2 进行匹配，节约计算时间
#                 matches = bf.match (memory[1], des1)
#                 matches_GMS = matchGMS (
#                         memory[0].shape[:2], i.shape[:2], memory[2], kp1, matches, withScale=False, withRotation=False,
#                         thresholdFactor=6
#                         )
#
#                 if len (matches_GMS) > max_score:
#                     max_score = len (matches_GMS)
#                     p2 = Reference_paths[count2][-7:-4]
#
#                 # 储存 {match:[p2]}
#                 my_dict[len (matches_GMS)].append (Reference_paths[count2][-7:-4])
#
#                 # 储存 [match]
#                 my_match.append (len (matches_GMS))
#
#                 count2 += 1
#
#         # 对my_match进行降序排序
#         my_match.sort (reverse=True)
#
#         loop = k
#
#         # 确定循环的次数(相同数字的不算)
#         if num_not_repeat:
#             new_key = 0
#             temp_key = k
#
#             for n in range (1, len (my_match)):
#                 if temp_key == 0:
#                     break
#                 elif my_match[n] != my_match[n - 1]:
#                     temp_key -= 1
#                     new_key += 1
#                 else:
#                     new_key += 1
#             loop = new_key
#             # print ('new_key', new_key)
#         #
#         # print(my_match)
#         # print(my_dict)
#         # print('\n')
#
#         # 遍历前k个元素
#         for val in range (0, loop):
#             # print(my_match[val])
#             # print(my_dict[my_match[val]])
#
#             # 调用my_dict,查看其中是否有名字相同的结果
#             for x in my_dict[my_match[val]]:
#                 # print(x)
#                 if p1 == x:
#                     is_success = True
#                     max_score = my_match[val]
#                     p2 = x
#
#         # print(len(my_match))
#         # print('\n')
#
#         if max_score > threshold and is_success:
#             success_count += 1
#
#         if is_result_show:
#             if max_score > threshold and is_success:
#                 print ('match successfully:', '<', p1, ' ', p2, '> ', max_score, '\n')
#             elif max_score > threshold and is_success == False:
#                 print ('match failed:      ', '<', p1, ' ', p2, '> ', max_score, '\n')
#             elif max_score < threshold and is_success == False:
#                 print ('not in dataset:    ', '<', p1, ' ', p2, '> ', max_score, '\n')
#
#     print ('Accuracy: ', float (success_count / count1) * 100, '%')
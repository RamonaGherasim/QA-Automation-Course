# # from collections import *
# # def uniqueOccurrences(arr):
# #     return len(set(Counter(arr).values())) == len(set(arr))
# #
# #     # All the below code can be done in the line above!!
# #
# #     # elem_list = []
# #     # occurence_list = []
# #     # for i in arr:
# #     #     occurence = arr.count(i)
# #     #     if i not in elem_list:
# #     #         elem_list.append(i)
# #     #         occurence_list.append(occurence)
# #     #
# #     # print(elem_list)
# #     # print(occurence_list)
# #     #
# #     # for j in occurence_list:
# #     #     occurence = occurence_list.count(j)
# #     #     if occurence > 1:
# #     #         return False
# #     # return True
# #
# #
# # arr = [1, 2, 2, 3, 1]
# # print(uniqueOccurrences(arr))
# #
# # od = OrderedDict()
# # od["a"] = 1
# # od["b"] = 2
# # od["c"] = 3
# # del od["b"]
# # od["b"] = 4
# # for key, value in od.items():
# #     print(key, ":", value)
# #
# # dd = defaultdict(list)
# #
# # task = [["admin", "title", "detail", "due", "date", "No"],
# #         ["admin", "title", "detail", "due", "date", "Yes"]]
# # for row in task:
# #     for elem in row:
# #         dd[row[0]] = row[1:len(row)]
# #
# # print(dd)
# import random
#
# num_list = random.sample(range(-100, 100), 10)
# print(num_list)
#
# max_num = num_list[0]
# i = 0
# while len(num_list) > 0:
#     num = num_list[i]
#     if num > max_num:
#         max_num = num
#     i += 1
#     # if i == len(num_list)-1:
#     #     break
# # for i in num_list:
# #     if i > max_num:
# #         max_num = i
# print(max_num)

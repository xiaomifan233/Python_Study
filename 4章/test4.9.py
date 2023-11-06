list = (0,2,4,3)
# flag = True
# for i in range(0,len(list)-1):
#     a = list[i]
#     for j in range(i+1,len(list)):
#         b = list[j]
#         if (a == b):
#             print("有重复")
#             flag = False
# if flag:
#     print("无重复")
print('list是否有重复元素',len(list) != len(set(list)))
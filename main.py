list1 = [1, 2, 3, 4, 6]
print(list1)
list1.insert(4, 5)  # 在指定索引添加元素
print(list1)
list2 = list(range(0, 100))
print(list2)
list3 = list((1, 'AB', 'C'))
print(list3)
list4 = list1 + list3
print(list4)
print(list3 * 3)
print(list3[1:3])
print(list1.index(2))  # 检索元素出现的位置
print(list3.index(2,1,5))  # 检索0到5内元素出现的位置
print(list3.count(1))  # 统计出现次数
list1.append(7)  # 在末尾添加元素

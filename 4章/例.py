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
print(list1.index(2, 0, 5))  # 检索0到5内2元素出现的位置
print(list3.count(1))  # 统计出现次数
list1.append(7)  # 在末尾添加元素
list2.extend(list3)
print(list2)
list1.remove(1)
print(list1)
list1.pop()  # 抛出一个指定的元素，默认最后一位
list1.reverse()  # 列表倒序
list1.sort()  # 对列表排序
list1.sort(reverse=True)  # 逆序排列
list5 = sorted(list1)  # 排序但不改变原列表，返回排序后的列表

# 字典
import copy
dict1 = {'name': 'joke', 'age': 10, 'sex': ['男','女']}
dict2 = dict1
dict2['name'] = 'tom'
print(dict1,dict2)
dict3 = dict1.copy()
dict3['name'] = 'john'
dict3['sex'].append('?')
print(dict1,dict2,dict3)
dict4 = copy.deepcopy(dict1)

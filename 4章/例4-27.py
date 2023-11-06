list = [10, 23, 5, 76, 21, 44, 92, 8, 19, 33]
for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)
list1 = [10, 23, 5, 76, 21, 44, 92, 8, 19, 33]
for i in range(len(list1) - 1):
    Min = list1[i]
    p = i
    for j in range(i + 1, len(list1)):
        if list1[j] < Min:
            Min = list1[j]
            p = j
    if p != i:
        list1[i], list1[p] = list1[p], list1[i]
print(list1)

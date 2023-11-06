list = [1, 3, 4, 2, 6, 5]


def sorted(list):
    list1 = list[::]
    list2 = []
    for i in range(0, len(list1)):
        a = min(list1)
        list2.append(a)
        list1.remove(a)
    return list2


print(sorted(list))

import random

List = [random.randint(1, 100) for i in range(0, 20)]
print(List)
list1 = List[::2]
print(list1)
list1.sort(reverse=True)
List[::2] = list1
print(List)

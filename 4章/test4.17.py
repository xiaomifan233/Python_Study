import random
list  = [random.randint(1,100) for i in range(0,20)]
# list = []
# for i in range(0,20):
#     list.append(random.randint(0,100))
list1 = list[0:10]
list2 = list[10:20]
list1.sort()
list2.sort(reverse=True)
print(list1)
print(list2)
list = list1 + list2
print(list)



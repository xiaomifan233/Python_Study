'''第一题
the_key = input("请输入一个键")
dict = {'name': 'joke', 'age': 10, 'sex': ['男','女']}
if the_key in dict:
    print(dict[the_key])
else:
    print("毛线")
'''
'''
# 第二题
list = []
for i in range(10):
    list.append(random.randint(0,100))
list.sort()
print(list[0])
print(list[9])
'''
'''
# 第三题
a=[1,2,3,4,5,6,7,8,9,0]
a.insert(0,a.pop())
print(a)
'''
'''
# 第四题
list = []
for a in range(1, 1000):
    if a % 7 == 0 and a % 3 == 2:
        list.append(a);
print(list)
for i in range(len(list)):
    print(list[i],end = "")
    if(i+1)%10 == 0 and i != 0:
    print("\n")
'''
'''
#第五题
list = [2, 2, 2, 2, 2, 4]
flag = 0
for i in range(1,len(list)):
    a,b,c = 0,0,0
    for j in range(0, i):
        a = a + list[j]
    for k in range(1,len(list) - i):
        b = b + list[e = i + k]
    if (a == b):
        c = i
        flag = 1
        break
if (flag == 1):
    print("在%d" %c)
if (flag == 0):
    print("none")
'''

'''
# 第六题
dict = {}
for i in range(1,11):
    dict["class"+str(i)] = i*i
print(dict)
'''
'''
# 第八题
list = []
for i in range(1,100):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        list.append(i)
print(list)
'''
'''
# 第七题
dict = {'及格':[],'不及格':[]}
list = [56, 75, 43, 82, 74, 63, 90, 88]
for i in range(len(list)):
    if list[i] > 60:
        dict['及格'].append(list[i])
    else:
        dict['不及格'].append(list[i])
print(dict)
'''

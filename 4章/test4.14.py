# month = int(input("请输入第几个月"))
a = 1
b = 1
for i in range(1, 3):
    print("第%d个月1对兔子" % i)
for i in range(2, 12):
    c = b
    b = a + b
    a = c
    print("第%d个月%d对兔子" % (i + 1, b))

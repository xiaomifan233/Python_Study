n = int(input("请输入n"))
for i in range(0,n):
    if i % 7 != 0 and i %3 == 0:
        print(i, end=' ')

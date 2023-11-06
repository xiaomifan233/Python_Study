n = int(input('请输入方阵阶数'))
a = []
count = 0
b = []
c = []
for i in range(n):
    s = input()
    a.append([int(n) for n in s.split()])
for i in range(n):
    Max = a[i][0]
    for j in range(1, n):
        if a[i][j] > Max:
            Max = a[i][j]
    c.append(Max)
for j in range(n):
    Min = a[0][j]
    for i in range(1, n):
        if a[i][j] < Min:
            Min = a[i][j]
        b.append(Min)
for i in range(n):
    for j in range(n):
        if c[i] == b[j]:
            print(i+1,'行', j+1,'列', '值：', a[i][j])
            count += 1
if count != 0:
    print(count,"个")
else:
    print("none")
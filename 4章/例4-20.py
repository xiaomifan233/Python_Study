n = 0
Str = ""
print("100内的素数为：")
for i in range(2, 101):
    flag = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        n += 1
        Str = Str + "%-2d " % i
        if n % 10 == 0:
            print(Str)
            Str = ""
print(Str)

list = []
for i in range(1, 101):
    for j in range(2, i//2+1):
        if (i % j == 0):
            break
    else:
        list.append(i)
print(list)

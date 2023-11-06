lis = [1, 2]
i = 1
a = 0
while True:
    if lis[i] < 100000:
        i += 1
        a = pow(lis[i - 1], 2) + pow(lis[i - 2], 2)
        lis.append(a)
    else:
        break
print(lis)

a =0
for i in range(1,1000):
    a = 0
    for j in range(1,i-1):
        if i%j == 0:
            a = a + j
    if i == a:
        print(i)

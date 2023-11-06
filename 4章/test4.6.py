n = int(input('请输入n'))
if n < 3 and n > 0:
    print("可以买%d瓶水"%n)
elif n >= 3:
    a = n
    sum = n
    while (a >= 3) :
        a = a// 3;
        sum = sum + a;
        b = a % 3;
        a = a + b;
    print("可以喝%d瓶水"%sum)
else:print("输入有误")
x = int(input("输入x"))
if x < -1:
    x = x ** 3 + 1
elif -1 <= x <= 1:
    x = x ** 2 - 5
elif x > 1:
    x = x ** 3 - 1
print(x)

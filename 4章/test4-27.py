a = int(input('请输入任意位的数字'))
b = 0
while a > 0:
    b = b * 10 + a % 10
    a = a // 10
print(b)

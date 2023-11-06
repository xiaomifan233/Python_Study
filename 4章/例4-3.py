import math

while 1:
    a, b, c = eval(input('请输入三角形的三边长，用逗号隔开'))
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c) / 2.0
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("area=%6.2f" % area)
        break
    else:
        print("输入的三个数不构成三角形")
        continue

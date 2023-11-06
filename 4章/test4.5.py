def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print('Fermat is wrong')
    else:
        print("Fermat is right")


a = int(input('请输入a的值：'))
b = int(input('请输入b的值：'))
c = int(input('请输入c的值：'))
n = int(input('请输入n的值：'))
check_fermat(a, b, c, n)
# a = 2,b = 3,c = 4 ,n = 5  --->Fermat is right

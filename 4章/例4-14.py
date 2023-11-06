n = int(input("请输入正整数"))
i = 0
print("概数从低到高依次为")
while n > 0:
    print(n % 10)
    i = i + 1
    n = n // 10
print("概数是%d位数" % i)

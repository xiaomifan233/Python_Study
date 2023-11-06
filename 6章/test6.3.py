def pandigital(num):
    for i in range(1, len(num)):
        if str(i) not in num:
            return False
        else:
            continue
    print(num)
    return True


numb = input('请输入')
numbe = numb.split(',')
for i in numbe:
    pandigital(i)
# 1234,234,3332,12345
 
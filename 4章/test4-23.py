sen = input("请输入") #sentence
alp = 0              #alpha
num = 0              #number
for i in sen:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        alp += 1
print('字母 %d' % alp)
print('数字 %d' % num)

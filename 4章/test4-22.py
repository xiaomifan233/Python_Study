print('请输入逗号分隔的4位二进制数')
num = input()
result = []
for a in num.split(","):
    if int(a,2) % 5 == 0:result.append(a)
print(','.join(result))

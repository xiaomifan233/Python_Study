s = input("请输入：")
result = []
s1 = s.split()
for i in range(len(s1)):
    if len(s1[i]) != 1:
        result.append(s1[i])
    else:
        result.append(s1[i].replace('i', 'I'))
print(' '.join(result))

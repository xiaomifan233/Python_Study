s = input('请输入')
count = 0
for i in range(len(s)):
    if 0x4E00 <= ord(s[i]) <= 0x9EA5:
        count += 1
print(count)
str1 = input('请输入')
count = 0
for c in str1:
    if 0x4E00<= ord(str1)<=0x9FA5:
        count += 1
print(count)
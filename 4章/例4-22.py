import random
a = int(input('请输入最小值'))
b = int(input('请输入最大值'))
flag = 1
Num = random.randint(a,b+1)
print('你可以猜8次')
for times in range(1,9):
    gessNum = int(input())
    if gessNum < Num:
        print('小了')
    elif gessNum > Num:
        print('大了')
    else:
        print('猜中了')
        print('你在%d次猜中了'%times)
        flag = 0
        break
if flag == 1:
    print('次数用完了，你没有猜中')


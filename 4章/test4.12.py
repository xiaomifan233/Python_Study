h = int(input('请输入初始高度h：'))
t = int(input('请输入弹的次数t'))
sum = h
for i in range(t):
    h = 0.6*h
    sum +=  h*2
sum -= h
print('总距离：',sum)
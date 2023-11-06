lis = sorted(list(input().split()))
dic = {}
for i in lis:
    dic[i] = lis.count(i)
for a in dic:
    print('%s:%d' % (a, dic[a]))

list1 = ['赵','钱','孙','李']
list2 = [1,2]
list3 = []
for i in list1:
    for j in list2:
        list3.append([i,j])
print('重组后的列表')
print(list3 )
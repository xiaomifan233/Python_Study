while 1:
    x = int(input("输入一个三位整数"))
    if x >= 100 and x<= 999:
        a = x //100
        b = x // 10 %10
        c = x % 10
        print("个位：%d 十位：%d 百位"%(c,b,a))
        break
    else:
        print("你输入的数不是三位数，请重新输入")
        continue
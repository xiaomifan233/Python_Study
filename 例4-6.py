year = eval(input("请输入年份:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d年份是闰年" % year)
else:
    print("%d年不是闰年" % year)

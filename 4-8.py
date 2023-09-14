import math
score = int(input())
if score > 100 or score <0:
    print("你输入的成绩不合法")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

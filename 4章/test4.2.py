time = int(input("输入工作时长"))
basic_wages = 3000

wages = 0
if time < 88:
    wages = 88 * 20
elif 88 <= time <= 176:
    wages = basic_wages + time * 20
else:
    wages = basic_wages + 176 * 20 + (time - 176) * 20 * 0.3

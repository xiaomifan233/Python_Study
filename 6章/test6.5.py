def avr(list):
    sum = 0
    for num in list:
        sum += num
    return sum / len(list)


list = eval(input('请输入'))
print(avr(list))

def count_char(str):
    count = [0] * 26
    for alp in str:
        if alp.isalpha():
            index = ord(alp.lower()) - ord('a')
            count[index] += 1
    return count


str1 = input()
print(count_char(str1))
# hello,world!

word_input = input('请输入')
words = []
word_split = word_input.split()
for i in word_split:
    if len(i) == 3:
        words.append(i)
if len(words) == 0:
    print('none')
else:
    print(words)
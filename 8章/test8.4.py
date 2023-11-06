import jieba.posseg

str1 = 'Python语言是当前流行的计算程序设计语言'
words  = jieba.posseg.cut(str1)
for item in words:
    print(item.word+'--'+item.flag)
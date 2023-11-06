s = "学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？"
count = s.count('，') + s.count('？')
print(count,len(s)-count)
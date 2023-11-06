for i in range(1, 10):
    Str = ""
    for j in range(1, i + 1):
        Str = Str + "%d*%d=%-2d " % (j, i, i * j)
    print(Str)

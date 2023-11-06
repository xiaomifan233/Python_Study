Str = "abcdef"


def nixu(s):
    if s == "":
        return s
    else:
        return nixu(s[1:]) + s[0]


print(nixu(Str))

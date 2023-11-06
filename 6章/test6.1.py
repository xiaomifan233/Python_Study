c = input()


def count(str, c):
    count = 0
    for a in str:
        if a == c:
            count += 1
    return count


print(count(str, c))

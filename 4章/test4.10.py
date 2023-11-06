for i in range(1, 8):
    for j in range(1, 8 - i):
        print(' ', end='')
    for k in range(1, i + 1):
        print('#', end='')
    print()
for i in range(1, 7):
    for j in range(1, i + 1):
        print(' ', end='')
    for k in range(1, 8 - i):
        print('#', end='')
    print()
print()
for i in range(1, 15):
    if i < 8:
        for j in range(1, 8 - i):
            print(' ', end='')
        for k in range(1, i + 1):
            print('#', end='')
        print()
    else:
        for j in range(1, i - 6):
            print(' ', end='')
        for k in range(1, 15 - i):
            print('#', end='')
        print()

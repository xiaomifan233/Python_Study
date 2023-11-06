import math


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
            return True


n = int(input('请输入'))
if isPrime(n):
    print(n, '是')
else:
    print(n, '不是')

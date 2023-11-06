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
def isMonicen(n):
    if isPrime(n):
        m = 2**n -1
        if isPrime(m):
            return m
        else:
            return 0
    else:return 0
count = 0
n = 2
while count<5:
    if isMonicen(n) != 0:
        print(isMonicen(n))
        count += 1
    n += 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial((n - 1))


def compute_e(precision):
    e = 1.0
    term = 1.0
    n = 1
    while abs(term) > precision:
        term = 1.0 / factorial(n)
        e += term
        n += 1
    return e


precision = 1e-7
e_value = compute_e(precision)
print(f'e≈{e_value:.7f}')

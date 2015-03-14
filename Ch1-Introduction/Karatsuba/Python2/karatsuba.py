import itertools

def karatsuba(x, y):
    # Python doesn't implement TCO, so use a loop instead
    return

def num_digits(n):
    return itertools.dropwhile(lambda exp: n / 10**exp > 0, itertools.count()).next()

def split(n, m):
    pow_ten = 10**m
    high_digits = n / pow_ten
    low_digits = n - high_digits*pow_ten
    return high_digits, low_digits



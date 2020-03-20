from math import sqrt


def is_prime(x):
    """Returns true or false if n is prime"""
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        n = 2
    while n < x:
        if x % n == 0 and x != n or x % sqrt(x) == 0 and x != n:
            return False
        else:
            n += 1
    else:
        return True


def primes(n):
    """List of prime numbers less than n"""
    is_not_prime = tuple([p for i in range(2, n) for p in range(i * 2, n, i)])
    __primes = [is_prime for is_prime in range(2, n)
                if is_prime not in is_not_prime]
    return __primes

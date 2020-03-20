
def fib(n):
    """Returns the nth number in Fibonacci sequence"""

    a = 0
    b = 1
    c = a + b
    fib_list = [a, b]
    for i in range(n+1):
        fib_list.append(c)
        a = b
        b = c
        c = a + b
    return fib_list[n]


print(fib(30))

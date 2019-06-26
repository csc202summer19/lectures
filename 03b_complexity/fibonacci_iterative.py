import sys


def fibonacci(n):
    """ Compute the nth Fibonacci number *iteratively*. """
    if n <= 1:
        return n

    # Keep track of the previous two numbers:
    a = 0
    b = 1

    f_n = 1

    for i in range(2, n):
        # Update the two previous numbers:
        a = b
        b = f_n
        # Compute the next number:
        f_n = a + b

    return f_n


print(fibonacci(int(sys.argv[1])))

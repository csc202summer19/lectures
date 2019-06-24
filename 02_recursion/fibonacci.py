# def fibonacci(n):
#     """ Compute the nth Fibonacci number. """
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# def fibonacci(n):
#     """ Compute the nth Fibonacci number *iteratively*. """
#     if n <= 1:
#         return n
#
#     # Keep track of the previous two numbers:
#     a = 0
#     b = 1
#
#     f_n = 1
#
#     for i in range(2, n):
#         # Update the two previous numbers:
#         a = b
#         b = f_n
#         # Compute the next number:
#         f_n = a + b
#
#     return f_n


# NOTE: This is not really "compute the nth Fibonacci number."
#       It's more along the lines of "compute the nth Fibonacci number if
#        you already know the mth and (m - 1)st numbers.
def fibonacci(n, a = 0, b = 1):
    """ Compute the nth Fibonacci number recursively and more efficiently. """
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci(n - 1, b, a + b)

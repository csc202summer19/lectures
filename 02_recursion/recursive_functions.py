def power(a, n):
    """ Compute a^n. """
    # NOTE: a^n = a * a * a * ... * a
    #       a^n = a * a^(n - 1)
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


def factorial(n):
    """ Compute n!. """
    # NOTE: n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
    #       n! = n * (n - 1)!
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

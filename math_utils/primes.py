import math

def isprime(n):
    """Returns True if n is prime, False if not."""

    # work with the absolute value of n
    n = abs(n)

    if n in {0, 1}:
        return False

    if n in {2, 3}:
        return True

    # if (nontrivially) n = n1 * n2 then at least one factors must be <= sqrt(n).
    # thus, if no divisor of n is smaller than int(math.sqrt(n)), n must be prime.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

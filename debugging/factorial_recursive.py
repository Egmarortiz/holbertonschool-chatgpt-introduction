#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Compute the factorial of a non-negative integer n using recursion.

    Parameters:
        n (int): Non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n (n!), with 0! defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)


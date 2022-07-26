"""
Given an integer n, return the number of prime numbers that are strictly less
than n.

Constraints:
0 <= n <= 5 * 10^6

Attempt 1: I knew this was solved with the Sieve of Eratosthenes,
but I don't know it off the top of my head.
"""
from math import sqrt, floor, ceil


class Solution:
    def countPrimes(self, n: int) -> int:
        primeValues = [True] * n

        for x in range(2, ceil(sqrt(n))):
            if primeValues[x] is True:
                for j in range(x*x, n, x):
                    primeValues[j] = False

        # Note that we subtract two because we aren't counting 0 and 1 as
        # prime.
        return max(0, len([idx for idx, val in enumerate(primeValues) if val is
                    True]) - 2)

test = Solution()
print(test.countPrimes(1))
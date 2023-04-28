import sys
import math

def egcd(a, b):
    """
    Extended GCD Algorithm
    Returns 0: Greatest Common Divisor
            1: Quotients by the GCD
            2: Bézout Coefficients
    See: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    Time Complexity: O(h), where h is the number of digits in the smaller
        number b. 
    """
    (r_o, r) = (a, b)
    (s_o, s) = (1, 0)
    (t_o, t) = (0, 1)

    while r != 0:
        q = r_o // r
        (r_o, r) = (r, r_o - q * r)
        (s_o, s) = (s, s_o - q * s)
        (t_o, t) = (t, t_o - q * t)

    return [r_o, (s, t), (s_o, t_o)]

def gcd(a, b):
    """
    Greatest Common Divisor Algorithm
    Time Complexity: O(h), where h is the number of digits in the smaller
        number b. 
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    """
    Least Common Multiple
    Time Complexity: O(h), where h is the number of digits in the smaller
        number b. 
    """
    return int((a * b) / gcd(a, b))

def prime(n):
    """
    Primality Test.
    Time Complexity: O(sqrt(n)).
    """
    root = 2

    while (root * root) <= n:
        if n % root == 0:
            return False
        root = root + 1

    return True

def primes(n):
    """
    Returns a list of prime in the interval [2, n].
    Time Complexity: O(n * sqrt(n)).
    """
    ans = []

    while n > 1:
        if prime(n):
            ans.append(n)
        n = n - 1

    return ans

def products(n):
    """
    Generates all unordered pairs (p, q) of prime numbers p and q such that
        p * q is less or equal to n.
    Time Complexity: O(pi(n)^2), where pi(n) represents the number of prime
        numbers less than or equal to n.
    """
    values = primes(n)
    ans = []

    for i in range(len(values)):
        p = values[i]
        for j in range(i, len(values)):
            q = values[j]
            if p * q <= n:
                ans.append((p, q))

    return ans

def public(pair):
    """
    """
    (p, q) = pair
    totient = lcm(p - 1, q - 1)
    ans = []

    for e in range(3, totient):
        if gcd(e, totient) == 1:
            ans.append(e)

    return (p, q, totient, ans)

def private(info):
    """
    """
    (p, q, totient, keys) = info
    ans = []

    for e in keys:
        _, _, (d, y) = egcd(e, totient)
        if d < 0:
            d = totient + d
        ans.append((e, d))

    return (p, q, totient, len(ans), ans)

if __name__ == "__main__":
    """
    """
    ans = []
    for pair in products(int(sys.argv[1])):
        eset = public(pair)
        if len(eset[3]):
            ans.append(eset)

    book = []
    for entry in ans:
        book.append(private(entry))
        print(book[-1])

#!/usr/bin/python

import sys
import math

USAGE = """\
Returns all possible RSA systems with the given parameter.

{} <max>
  <max> - maximum value for the modulo right operand.\
"""

def egcd(a, b):
    """
    Extended GCD Algorithm.
    Returns (r, (s, t), (x, y)), where
            r is the Greatest Common Divisor;
            (s, t) are the Quotients by the GCD; and
            (x, y) are the Bézout Coefficients.
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
    Greatest Common Divisor Algorithm.
    Time Complexity: O(h), where h is the number of digits in the smaller
        number b. 
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    """
    Least Common Multiple.
    Time Complexity: O(h), where h is the number of digits in the smaller
        number b. 
    """
    return int((a * b) / gcd(a, b))

def factor(n):
    """
    Primality Test.
    Returns the least prime factor of n or None if n is prime.
    Time Complexity: O(sqrt(n)).
    """
    root = 2

    while (root * root) <= n:
        if n % root == 0:
            return root
        root = root + 1

    return None

def primes(n):
    """
    Returns a list of primes in the interval [2, n].
    Time Complexity: O(n * sqrt(n)).
    """
    ans = []

    while n > 1:
        if factor(n) == None:
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
    Given a pair (p, q) returns all possible RSA public keys using Carmichael's
    totient function lambda(n), where n = p * q.
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
    Given partial RSA system (p, q, totient, keys), where keys is a set of
    possible public keys, complement it with all associated RSA private keys.
    """
    (p, q, totient, keys) = info
    ans = []

    for e in keys:
        _, _, (d, y) = egcd(e, totient)
        if d < 0:
            d = totient + d
        ans.append((e, d))

    return (p, q, totient, ans)

def book(limit):
    """
    Returns all possible RSA systems where n (module right operand) is less or
    equal to the given limit.
    """
    ans = []
    pairs = products(limit)
    for pair in pairs:
        (p, q, totient, keys) = public(pair)
        if len(keys):
            ans.append((p, q, totient, keys))
 
    book = []
    for entry in ans:
        (p, q, totient, pairs) = private(entry)
        book.append((p * q, p, q, totient, pairs))

    return book

def crack(n):
    """
    Given a modulo value n, compute all possible RSA systems if n is a product
    of two prime numbers.
    """
    q = factor(n)

    ans = ()
    if q != None:
        p = n // q
        if factor(p) == None:
            ans = private(public((p, q)))

    return ans

if __name__ == "__main__":
    """
    """
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        b = book(n)
        for i in b:
            print(i)
    else:
        print(USAGE.format(sys.argv[0]))

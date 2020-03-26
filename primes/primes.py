#!/usr/bin/env python


def is_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def primes_in_interval(first, second):
    primes = []
    for i in range(first, second):
        if is_prime(i):
            primes.append(i)
    return str(primes)

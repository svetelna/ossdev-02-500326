#!/usr/bin/env python

import sys
import unittest
sys.path.insert(0, '../')
from primes import is_prime, primes_in_interval


class Test_Primes(unittest.TestCase):
    """
    Class for tesing prime calculation functions
    """
    def test_is_prime(self):
        res = is_prime(5)
        self.assertTrue(res)
        res = is_prime(9)
        self.assertFalse(res)

    def test_primes_in_interval(self):
        res = primes_in_interval(5, 9)
        self.assertEqual(res, str([5, 7]))


if __name__ == '__main__':
    unittest.main()

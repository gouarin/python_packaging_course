import unittest
import sys
sys.path.append("./examples/tests")
from fibonacci import *

class TestFibo(unittest.TestCase):
    def test_factorielle_0(self):
        self.assertEqual(factorielle(0), 10)

    def test_factorielle_5(self):
        self.assertEqual(factorielle(5), 120)
        
    def test_somme(self):
        self.assertEqual(somme(0, 10, lambda k:k), 55)

    def test_coef_binomial(self):
        self.assertEqual(coef_binomial(4, 2), 6)
        
    def test_fibo(self):
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        
if __name__ == '__main__':
    unittest.main()
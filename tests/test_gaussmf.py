import unittest
from pyfuzzy.mf import gaussmf


class GaussMFTestCase(unittest.TestCase):
    def test_gaussian_membership_function(self):
        self.assertEqual(gaussmf.gaussmf(1, [1.0, 0.1]), 1.0)

if __name__ == '__main__':
    unittest.main()


import unittest

from pyfuzzy.mf import zmf

class ZMFTestCase(unittest.TestCase):

    def test_ZMF1_membership_function(self):
        self.assertEqual(zmf.zmf(-1, [3.0, 7.0]), 1.0)

    def test_ZMF2_membership_function(self):
        self.assertEqual(zmf.zmf(5, [0.0, 10.0]), 0.5)

    def test_ZMF3_membership_function(self):
        self.assertEqual(zmf.zmf(6, [2.0, 8.0]), 0.22)

    def test_ZMF4_membership_function(self):
        self.assertEqual(zmf.zmf(10, [-2.0, 8.0]), 0.0)

    def test_ZMF5_membership_function(self):
        self.assertEqual(zmf.zmf(0, [9.0, 15.0]), 1.0)

    def test_ZMF6_membership_function(self):
        self.assertEqual(zmf.zmf(101, [5.0, 100.0]), 0.0)

    def test_ZMF7_membership_function(self):
        self.assertEqual(zmf.zmf(-2, [-5.0, 5.0]), 0.82)

    def test_ZMF8_membership_function(self):
        self.assertRaises(TypeError, lambda: zmf.zmf(0, [2]))

    def test_ZMF9_membership_function(self):
        self.assertRaises(TypeError, lambda: zmf.zmf(0, [3, 10.0]))

    def test_ZMF10_membership_function(self):
        self.assertRaises(TypeError, lambda: zmf.zmf(6, [10.0, 4.0]))
        
    def test_ZMF11_membership_function(self):
        self.assertRaises(TypeError, lambda: zmf.zmf(0, [1, 30.0, 100.0]))

    def test_ZMF12_membership_function(self):
        self.assertRaises(TypeError, lambda: zmf.zmf(0, [1, 2.5, 300, 800]))

    def test_ZMF13_membership_function(self):
        self.assertRaises(TypeError, lambda: zmf.zmf(10.0, []))


if __name__ == '__main__':
    unittest.main()

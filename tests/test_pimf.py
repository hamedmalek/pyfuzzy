import unittest
from pyfuzzy.mf import pimf

class PiMFTestCase(unittest.TestCase):
    def test_pimf_membership_function(self):
        self.assertEqual(pimf.pimf(0.0, [1.0, 4.0, 5.0, 10.0]), 0.0)

    def test_pimf2_membership_function(self):
        self.assertEqual(pimf.pimf(1.0, [1.0, 4.0, 5.0, 10.0]), 0.0)

    def test_pimf3_membership_function(self):
        self.assertEqual(pimf.pimf(4.0, [1.0, 4.0, 5.0, 10.0]), 1.0)

    def test_pimf4_membership_function(self):
        self.assertEqual(pimf.pimf(5.0, [1.0, 4.0, 5.0, 10.0]), 1.0)

    def test_pimf5_membership_function(self):
        self.assertEqual(pimf.pimf(10.0, [1.0, 4.0, 5.0, 10.0]), 0.0)

    def test_pimf6_membership_function(self):
        self.assertEqual(pimf.pimf(10.5, [1.0, 4.0, 5.0, 10.0]), 0.0)

    def test_pimf7_membership_function(self):
        self.assertRaises(TypeError, lambda: pimf.pimf(1.0, [1.0, 4.0, 5.0]))

    def test_pimf8_membership_function(self):
        self.assertRaises(TypeError, lambda: pimf.pimf(1.0, [1.0]))

    def test_pimf9_membership_function(self):
        self.assertRaises(TypeError, lambda: pimf.pimf(1.0, [1.0,]))

    def test_pimf10_membership_function(self):
        self.assertRaises(TypeError, lambda: pimf.pimf(1.0, []))

    def test_pimf11_membership_function(self):
        self.assertRaises(TypeError, lambda: pimf.pimf(1, [1, 4.0, 5.0, 10.0]))

    def test_pimf12_membership_function(self):
        self.assertAlmostEqual(pimf.pimf(2.5, [1.0, 4.0, 8.0, 13.0]), 0.5, places=2)

    def test_pimf13_membership_function(self):
        self.assertAlmostEqual(pimf.pimf(3.5, [1.0, 4.0, 8.0, 13.0]), 0.94, places=2)

    def test_pimf14_membership_function(self):
        self.assertAlmostEqual(pimf.pimf(5, [6.0, 4.0, 10.0, 5.0]), 1, places=2)

    def test_pimf15_membership_function(self):
        self.assertAlmostEqual(pimf.pimf(0.5, [0.0, 1.0, 1.0, 0.0]), 0.5, places=2)

    def test_pimf16_membership_function(self):
        self.assertAlmostEqual(pimf.pimf(0.4, [0.0, 1.0, 1.0, 0.0]), 0.320, places=3)


if __name__ == '__main__':
    unittest.main()
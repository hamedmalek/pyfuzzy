import unittest
from unittest import TestCase

from pyfuzzy.mf import trapmf


class TrapMFTestCase(unittest.TestCase):

    def test_trapezoidal_membership_function(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [-2.0, -0.5, 0.5, 2.5,3.3]))

    def test_trapezoidal_membership_function1(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [-2.0, -0.5, 0.5]))

    def test_trapezoidal_membership_function2(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [-2.0, -0.5]))

    def test_trapezoidal_membership_function3(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [-2.0]))

    def test_trapezoidal_membership_function4(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, []))

    def test_trapezoidal_membership_function5(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [2.5, 0.5, -0.5, -2.5]))

    def test_trapezoidal_membership_function6(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [2.0, 0.5, -0.5, -2.5]))

    def test_trapezoidal_membership_function7(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [-2.0, -2.0, 0.5, 2.5]))

    def test_trapezoidal_membership_function8(self):
        self.assertRaises(TypeError, lambda: trapmf.trapmf(2.0, [-2.0, -0.5, 0.5, 0.5]))

    def test_trapezoidal_membership_function9(self):
        self.assertAlmostEqual(trapmf.trapmf(-5.0, [-4.0, -2.5, -1.5, -0.5]), 0, places=4)

    def test_trapezoidal_membership_function10(self):
        self.assertAlmostEqual(trapmf.trapmf(-3.9, [-4.0, -2.5, -1.5, -0.5]), 0.0667, places=4)

    def test_trapezoidal_membership_function11(self):
        self.assertAlmostEqual(trapmf.trapmf(-3.5, [-4.0, -2.5, -1.5, -0.5]), 0.3333, places=4)

    def test_trapezoidal_membership_function12(self):
        self.assertAlmostEqual(trapmf.trapmf(-3.0, [-4.0, -2.5, -1.5, -0.5]), 0.6667, places=4)

    def test_trapezoidal_membership_function13(self):
        self.assertAlmostEqual(trapmf.trapmf(-2.3, [-4.0, -2.5, -1.5, -0.5]), 1, places=4)

    def test_trapezoidal_membership_function14(self):
        self.assertAlmostEqual(trapmf.trapmf(-2.0, [-4.0, -2.5, -1.5, -0.5]), 1, places=4)

    def test_trapezoidal_membership_function15(self):
        self.assertAlmostEqual(trapmf.trapmf(-1.7, [-4.0, -2.5, -1.5, -0.5]), 1, places=4)

    def test_trapezoidal_membership_function16(self):
        self.assertAlmostEqual(trapmf.trapmf(-1.3, [-4.0, -2.5, -1.5, -0.5]), 0.8000, places=4)

    def test_trapezoidal_membership_function17(self):
        self.assertAlmostEqual(trapmf.trapmf(-1.0, [-4.0, -2.5, -1.5, -0.5]), 0.5000, places=4)

    def test_trapezoidal_membership_function18(self):
        self.assertAlmostEqual(trapmf.trapmf(-0.6, [-4.0, -2.5, -1.5, -0.5]), 0.1000, places=4)

    def test_trapezoidal_membership_function19(self):
        self.assertAlmostEqual(trapmf.trapmf(-0.3, [-4.0, -2.5, -1.5, -0.5]), 0.0, places=4)

    def test_trapezoidal_membership_function20(self):
        self.assertAlmostEqual(trapmf.trapmf(-0.1, [-4.0, -2.5, -1.5, -0.5]), 0.0, places=4)

    def test_trapezoidal_membership_function21(self):
        self.assertAlmostEqual(trapmf.trapmf(-3.0, [-2.0, -0.5, 0.5, 2.5]), 0.0, places=4)

    def test_trapezoidal_membership_function22(self):
        self.assertAlmostEqual(trapmf.trapmf(-2.4, [-2.0, -0.5, 0.5, 2.5]), 0.0, places=4)

    def test_trapezoidal_membership_function23(self):
        self.assertAlmostEqual(trapmf.trapmf(-2.1, [-2.0, -0.5, 0.5, 2.5]), 0.0, places=4)

    def test_trapezoidal_membership_function24(self):
        self.assertAlmostEqual(trapmf.trapmf(-1.8, [-2.0, -0.5, 0.5, 2.5]), 0.1333, places=4)

    def test_trapezoidal_membership_function25(self):
        self.assertAlmostEqual(trapmf.trapmf(-1.4, [-2.0, -0.5, 0.5, 2.5]), 0.4000, places=4)

    def test_trapezoidal_membership_function26(self):
        self.assertAlmostEqual(trapmf.trapmf(-0.7, [-2.0, -0.5, 0.5, 2.5]), 0.8667, places=4)

    def test_trapezoidal_membership_function27(self):
        self.assertAlmostEqual(trapmf.trapmf(-0.6, [-2.0, -0.5, 0.5, 2.5]), 0.9333, places=4)

    def test_trapezoidal_membership_function28(self):
        self.assertAlmostEqual(trapmf.trapmf(-0.3, [-2.0, -0.5, 0.5, 2.5]), 1.0, places=4)

    def test_trapezoidal_membership_function29(self):
        self.assertAlmostEqual(trapmf.trapmf(0.0, [-2.0, -0.5, 0.5, 2.5]), 1.0, places=4)

    def test_trapezoidal_membership_function30(self):
        self.assertAlmostEqual(trapmf.trapmf(0.2, [-2.0, -0.5, 0.5, 2.5]), 1.0, places=4)

    def test_trapezoidal_membership_function31(self):
        self.assertAlmostEqual(trapmf.trapmf(0.8, [-2.0, -0.5, 0.5, 2.5]), 0.8500, places=4)

    def test_trapezoidal_membership_function32(self):
        self.assertAlmostEqual(trapmf.trapmf(1.0, [-2.0, -0.5, 0.5, 2.5]), 0.7500, places=4)

    def test_trapezoidal_membership_function33(self):
        self.assertAlmostEqual(trapmf.trapmf(1.6, [-2.0, -0.5, 0.5, 2.5]), 0.4500, places=4)

    def test_trapezoidal_membership_function34(self):
        self.assertAlmostEqual(trapmf.trapmf(2.0, [-2.0, -0.5, 0.5, 2.5]), 0.2500, places=4)

    def test_trapezoidal_membership_function35(self):
        self.assertAlmostEqual(trapmf.trapmf(2.4, [-2.0, -0.5, 0.5, 2.5]), 0.0500, places=4)

    def test_trapezoidal_membership_function36(self):
        self.assertAlmostEqual(trapmf.trapmf(2.8, [-2.0, -0.5, 0.5, 2.5]), 0.0, places=4)

    def test_trapezoidal_membership_function37(self):
        self.assertAlmostEqual(trapmf.trapmf(3.0, [-2.0, -0.5, 0.5, 2.5]), 0.0, places=4)

    def test_trapezoidal_membership_function38(self):
        self.assertAlmostEqual(trapmf.trapmf(0.3, [1.0, 3.0, 4.0, 5.5]), 0.0, places=4)

    def test_trapezoidal_membership_function39(self):
        self.assertAlmostEqual(trapmf.trapmf(1.3, [1.0, 3.0, 4.0, 5.5]), 0.1500, places=4)

    def test_trapezoidal_membership_function40(self):
        self.assertAlmostEqual(trapmf.trapmf(1.9, [1.0, 3.0, 4.0, 5.5]), 0.4500, places=4)

    def test_trapezoidal_membership_function41(self):
        self.assertAlmostEqual(trapmf.trapmf(2.4, [1.0, 3.0, 4.0, 5.5]), 0.7000, places=4)

    def test_trapezoidal_membership_function42(self):
        self.assertAlmostEqual(trapmf.trapmf(2.9, [1.0, 3.0, 4.0, 5.5]), 0.9500, places=4)

    def test_trapezoidal_membership_function43(self):
        self.assertAlmostEqual(trapmf.trapmf(3.3, [1.0, 3.0, 4.0, 5.5]), 1.0, places=4)

    def test_trapezoidal_membership_function44(self):
        self.assertAlmostEqual(trapmf.trapmf(4.3, [1.0, 3.0, 4.0, 5.5]), 0.8000, places=4)

    def test_trapezoidal_membership_function45(self):
        self.assertAlmostEqual(trapmf.trapmf(4.5, [1.0, 3.0, 4.0, 5.5]), 0.6667, places=4)

    def test_trapezoidal_membership_function46(self):
        self.assertAlmostEqual(trapmf.trapmf(5.0, [1.0, 3.0, 4.0, 5.5]), 0.3333, places=4)

    def test_trapezoidal_membership_function47(self):
        self.assertAlmostEqual(trapmf.trapmf(5.2, [1.0, 3.0, 4.0, 5.5]), 0.2000, places=4)

    def test_trapezoidal_membership_function48(self):
        self.assertAlmostEqual(trapmf.trapmf(6.0, [1.0, 3.0, 4.0, 5.5]), 0.0, places=4)

if __name__ == '__main__':
    unittest.main()

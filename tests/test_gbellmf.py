import unittest
from pyfuzzy.mf import gbellmf


class GbellMFTestCase(unittest.TestCase):
    # test for wrong input
    def test_generalizedBell1_membership_function(self):
        with self.assertRaises(TypeError):
            # test for zero A input
            gbellmf.gbellmf(0, [0.0, 4.0, 6.0])

    def test_generalizedBell2_membership_function(self):
        with self.assertRaises(TypeError):
            # test for list with wrong length
            gbellmf.gbellmf(6, [2.0, 6.0])

    def test_generalizedBell3_membership_function(self):
        with self.assertRaises(TypeError):
            # test for non list input
            gbellmf.gbellmf(6, 6.0)

    def test_generalizedBell4_membership_function(self):
        with self.assertRaises(TypeError):
            # test for non float list input
            gbellmf.gbellmf(6, [2, 4.0, 6.0])

    def test_generalizedBell5_membership_function(self):
        with self.assertRaises(TypeError):
            # test for wrong type input tuple instead of list
            gbellmf.gbellmf(6, (2.0, 4.0, 6.0))
    
    # test for wrong result
    def test_generalizedBell6_membership_function(self):
        self.assertEqual(gbellmf.gbellmf(4.0, [2.0, 4.0, 6.0]), 0.5)
    
    def test_generalizedBell7_membership_function(self):
        self.assertEqual(gbellmf.gbellmf(6.0, [2.0, 4.0, 6.0]), 1.0)

    def test_generalizedBell8_membership_function(self):
        self.assertEqual(gbellmf.gbellmf(8.0, [2.0, 4.0, 6.0]), 0.5)

    #################################
    def test_generalizedBell9_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(0, [2.0, 4.0, 6.0]), 0, places=3)

    def test_generalizedBell10_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(1.0, [2.0, 4.0, 6.0]), 0.001, places=3)
    
    def test_generalizedBell11_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(2.0, [2.0, 4.0, 6.0]), 0.0039, places=3)

    def test_generalizedBell12_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(3.0, [2.0, 4.0, 6.0]), 0.0376, places=3)

    def test_generalizedBell13_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(5.0, [2.0, 4.0, 6.0]), 1, places=2)
        # within 2 places 0.99

    def test_generalizedBell14_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(7.0, [2.0, 4.0, 6.0]), 1, places=2)
        # within 2 places 0.99

    def test_generalizedBell15_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(9.0, [2.0, 4.0, 6.0]), 0.0376, places=3)

    def test_generalizedBell16_membership_function(self):
        self.assertAlmostEqual(gbellmf.gbellmf(10.0, [2.0, 4.0, 6.0]), 0.0039, places=3)


# all test ran successfully
if __name__ == '__main__':
    unittest.main()


import unittest
from pyfuzzy.mf import trimf


class TriMFTestCase(unittest.TestCase):
    def test_Trimf1_membership_function(self):
        self.assertEqual(trimf.trimf(-1, [3.0, 6.0, 8.0]), 0.0)

    def test_Trimf2_membership_function(self):
        self.assertEqual(trimf.trimf(0, [3.0, 6.0, 8.0]), 0.0)

    def test_Trimf3_membership_function(self):
        self.assertEqual(trimf.trimf(2, [3.0, 6.0, 8.0]), 0.0)

    def test_Trimf4_membership_function(self):
        self.assertEqual(trimf.trimf(2, [3.0, 6.0, 10.0]), 0.0)

    def test_Trimf5_membership_function(self):
        self.assertEqual(trimf.trimf(2, [3.0, 6.0, 100.0]), 0.0)

    def test_Trimf6_membership_function(self):
        self.assertEqual(trimf.trimf(6, [3.0, 6.0, 8.0]), 1)

    def test_Trimf7_membership_function(self):
        self.assertEqual(trimf.trimf(1001, [3.0, 5.0, 1000.0]), 0)

    def test_Trimf8_membership_function(self):
        self.assertRaises(TypeError, lambda: trimf.trimf(0, [1, 0.0, 6.1]))

    def test_Trimf9_membership_function(self):
        self.assertRaises(TypeError, lambda: trimf.trimf(0, [1]))

    def test_Trimf10_membership_function(self):
        self.assertRaises(TypeError, lambda: trimf.trimf(0, [1, 2.5]))

    def test_Trimf11_membership_function(self):
        self.assertRaises(TypeError, lambda: trimf.trimf(0, [1, 30.5, 500]))

    def test_Trimf12_membership_function(self):
        self.assertRaises(TypeError, lambda: trimf.trimf(0, [1, 2.5, 300, 900]))


if __name__ == '__main__':
    unittest.main()

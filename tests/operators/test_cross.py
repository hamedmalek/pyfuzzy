import unittest

from pyfuzzy.operators.cross import cross


class CrossTestCase(unittest.TestCase):

    # Test input type - First input argument should be a dictionary.
    def test_cross_1(self):
        test_mf1 = [0.3, 0.4, 0.9, 0.2]
        test_mf2 = {1: 0.2, 2: 0.5}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test input type - Second input argument should be a dictionary.
    def test_cross_2(self):
        test_mf1 = {1: 0.2, 2: 0.5}
        test_mf2 = [0.3, 0.4, 0.9, 0.2]
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test input size - Dictionary should have at least one set.
    def test_cross_3(self):
        test_mf1 = {}
        test_mf2 = {1: 0.2, 2: 0.5}
        self.assertRaises(ValueError, lambda: cross(test_mf1, test_mf2))

    # Test input size - Dictionary should have at least one set.
    def test_cross_4(self):
        test_mf1 = {1: 0.2, 2: 0.5}
        test_mf2 = {}
        self.assertRaises(ValueError, lambda: cross(test_mf1, test_mf2))

    # Test key type - Key of dictionary should be a int.
    def test_cross_5(self):
        test_mf1 = {1.0: 0.2, 2.0: 0.5}
        test_mf2 = {1: 0.2, 2: 0.34, 3: 0.65}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test key type - Key of dictionary should be a int.
    def test_cross_6(self):
        test_mf1 = {'1': 0.2, '2': 0.5}
        test_mf2 = {1: 0.2, 2: 0.34, 3: 0.65}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test value type - Value of dictionary should be a float or int.
    def test_cross_7(self):
        test_mf1 = {1: [0.2], 2: [0.5]}
        test_mf2 = {1: 0.2, 2: 0.34, 3: 0.65}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test value type - Value of dictionary should be a float or int.
    def test_cross_8(self):
        test_mf1 = {1: '0.2', 2: '0.5'}
        test_mf2 = {1: 0.2, 2: 0.34, 3: 0.65}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test value type - Value of dictionary should be a float or int.
    def test_cross_9(self):
        test_mf1 = {1: 2, 2: 5}
        test_mf2 = {1: 0.2, 2: 0.34, 3: 0.65}
        self.assertRaises(ValueError, lambda: cross(test_mf1, test_mf2))

    # Test key type - Key of dictionary should be a int.
    def test_cross_10(self):
        test_mf1 = {1: 0.2, 2: 0.34, 3: 0.65}
        test_mf2 = {1.0: 0.2, 2.0: 0.5, 3.0: 0.76}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test key type - Key of dictionary should be a int.
    def test_cross_11(self):
        test_mf1 = {1: 0.2, 2: 0.34, 3: 0.65}
        test_mf2 = {'1': 0.2, '2': 0.5, '3': 0.76}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test value type - Value of dictionary should be a float or int.
    def test_cross_12(self):
        test_mf1 = {1: 0.2, 2: 0.34, 3: 0.65}
        test_mf2 = {1: [0.2], 2: [0.5], 3: [0.76]}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test value type - Value of dictionary should be a float or int.
    def test_cross_13(self):
        test_mf1 = {1: 0.2, 2: 0.34, 3: 0.65}
        test_mf2 = {1: '0.2', 2: '0.5', 3: '0.76'}
        self.assertRaises(TypeError, lambda: cross(test_mf1, test_mf2))

    # Test value range - Value should be between 0 or 1.
    def test_cross_14(self):
        test_mf1 = {1: 0.2, 2: 0.34, 3: 0.65}
        test_mf2 = {1: 2, 2: 5, 3: 7}
        self.assertRaises(ValueError, lambda: cross(test_mf1, test_mf2))

    # Test a random fuzzy set 1
    def test_cross_15(self):
        test_mf1 = {1: 0.2, 2: 0.3, 3: 0.8, 4: 0.7}
        test_mf2 = {1: 0.5, 2: 0.1, 3: 0.5, 4: 0.9}
        self.assertEqual(0.3, cross(test_mf1, test_mf2))

    # Test a random fuzzy set 2
    def test_cross_16(self):
        test_mf1 = {1: 0.5, 2: 0.1, 3: 0.5, 4: 0.9}
        test_mf2 = {1: 0.2, 2: 0.3, 3: 0.8, 4: 0.7}
        self.assertEqual(0.3, cross(test_mf1, test_mf2))

    # Test a random fuzzy set 3
    def test_cross_17(self):
        test_mf1 = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}
        test_mf2 = {1: 0.5, 2: 0.1, 3: 0.5, 4: 0.9, 5: 0.2}
        self.assertEqual(0.1, cross(test_mf1, test_mf2))

    # Test a random fuzzy set 4
    def test_cross_18(self):
        test_mf1 = {1: 0.1, 2: 0.7, 3: 0.4}
        test_mf2 = {1: 0.9, 2: 0.2, 3: 0.5}
        self.assertEqual(0.5, cross(test_mf1, test_mf2))

    # Test a random fuzzy set 5
    def test_cross_19(self):
        test_mf1 = {1: 0.0005, 2: 0.34, 3: 0.9999}
        test_mf2 = {1: 0.9995, 2: 0.66, 3: 0.0001}
        self.assertEqual(0.66, cross(test_mf1, test_mf2))


if __name__ == '__main__':
    unittest.main()

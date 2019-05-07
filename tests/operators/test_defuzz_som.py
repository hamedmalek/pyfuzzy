import unittest

from pyfuzzy.operators import defuzz_som


class DefuzzLomTestCase(unittest.TestCase):

    # Test input type - Input argument should be a dictionary.
    def test_Defuzz_som_1(self):
        test = [1, 2, 3]
        self.assertRaises(TypeError, lambda: Defuzz_som.Defuzz_som(test))

    # Test input type - Input argument should be a dictionary.
    def test_Defuzz_som_2(self):
        test = [[1], [2], [3]]
        self.assertRaises(TypeError, lambda: Defuzz_som.Defuzz_som(test))

    # Test input type - Input argument should be a dictionary.
    def test_Defuzz_som_3(self):
        test = 0.1
        self.assertRaises(TypeError, lambda: Defuzz_som.Defuzz_som(test))

    # Test input size - Dictionary should have at least one set.
    def test_Defuzz_som_4(self):
        test = {}
        self.assertRaises(ValueError, lambda: Defuzz_som.Defuzz_som(test))

    # Test key type - Key of dictionary should be a int.
    def test_Defuzz_som_5(self):
        test = {1.0: 0.1, 2.0: 0.2, 3.0: 0.3}
        self.assertRaises(TypeError, lambda: Defuzz_som.Defuzz_som(test))

    # Test value type - Value of dictionary should be a float or int.
    def test_Defuzz_som_6(self):
        test = {1: '0.1', 2: '0.2', 3: '0.3'}
        self.assertRaises(TypeError, lambda: Defuzz_som.Defuzz_som(test))

    # Test value type - Value of dictionary should be a float or int.
    def test_Defuzz_som_7(self):
        test = {1: [0.2], 2: [0.2], 3: [0.1]}
        self.assertRaises(TypeError, lambda: Defuzz_som.Defuzz_som(test))

    # Test value range - Value should be between 0 or 1.
    def test_Defuzz_som_8(self):
        test = {1: 2, 2: 3.5, 3: -1}
        self.assertRaises(ValueError, lambda: Defuzz_som.Defuzz_som(test))

    # Test 1 - return smallest item with largest value
    def test_Defuzz_som_9(self):
        test = {1: 0.5, 2: 0.3, 3: 0.85, 4: 0.35}
        self.assertEqual(Defuzz_som.Defuzz_som(test), 3)

    # Test 2 - return smallest item with largest value
    def test_Defuzz_som_10(self):
        test = {0: 0, 1: 0.3, 2: 0.3, 3: 0.3, 4: 0.5, 5: 0.5, 6: 1, 7: 1, 8: 0}
        self.assertEqual(Defuzz_som.Defuzz_som(test), 6)

    # Test 3 - return smallest item with largest value
    def test_Defuzz_som_11(self):
        test = {0: 0, 1: 0.8, 2: 0.2, 3: 0.8, 4: 0.8, 5: 0.5, 6: 0.5, 7: 0.2, 8: 0.2, 9: 0.2, 10: 0, 11: 0.8}
        self.assertEqual(Defuzz_som.Defuzz_som(test), 1)


# Run all unittests
if __name__ == '__main__':
    unittest.main()

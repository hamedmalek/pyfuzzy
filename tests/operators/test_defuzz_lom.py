import unittest

from pyfuzzy.operators import Defuzz_lom


class DefuzzLomTestCase(unittest.TestCase):

    # Test input type - Input argument should be a dictionary.
    def test_defuzz_lom_1(self):
        test = [0.1, 0.2, 0.3]
        self.assertRaises(TypeError, lambda: Defuzz_lom.defuzz_lom(test))

    # Test input size - Dictionary should have at least one set.
    def test_defuzz_lom_2(self):
        test = {}
        self.assertRaises(ValueError, lambda: Defuzz_lom.defuzz_lom(test))

    # Test key type - Key of dictionary should be a int.
    def test_defuzz_lom_3(self):
        test = {1.0: 0.5, 2.0: 0.76}
        self.assertRaises(TypeError, lambda: Defuzz_lom.defuzz_lom(test))

    # Test value type - Value of dictionary should be a float or int.
    def test_defuzz_lom_4(self):
        test = {1: '0.1', 2: '0.5', 3: '0.75'}
        self.assertRaises(TypeError, lambda: Defuzz_lom.defuzz_lom(test))

    # Test value type - Value of dictionary should be a float or int.
    def test_defuzz_lom_5(self):
        test = {1: [0.2], 2: [0.5], 3: [0.1]}
        self.assertRaises(TypeError, lambda: Defuzz_lom.defuzz_lom(test))

    # Test value range - Value should be between 0 or 1.
    def test_defuzz_lom_6(self):
        test = {1: 2, 2: 3.5, 3: -1}
        self.assertRaises(ValueError, lambda: Defuzz_lom.defuzz_lom(test))

    # Test a random fuzzy set 1
    def test_defuzz_lom_7(self):
        test = {1: 0.5, 2: 0.3, 3: 0.85, 4: 0.35}
        self.assertEqual(Defuzz_lom.defuzz_lom(test), 3)

    # Test a random fuzzy set 2
    def test_defuzz_lom_8(self):
        test = {0: 0, 1: 0.3, 2: 0.3, 3: 0.3, 4: 0.5, 5: 0.5, 6: 1, 7: 1, 8: 0}
        self.assertEqual(Defuzz_lom.defuzz_lom(test), 7)

    # Test a random fuzzy set 3
    def test_defuzz_lom_9(self):
        test = {0: 0, 1: 0.8, 2: 0.8, 3: 0.8, 4: 0.8, 5: 0.5, 6: 0.5, 7: 0.2, 8: 0.2, 9: 0.2, 10: 0, 11: 0}
        self.assertEqual(Defuzz_lom.defuzz_lom(test), 4)


# Run all unittests
if __name__ == '__main__':
    unittest.main()

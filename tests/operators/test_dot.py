import unittest

from pyfuzzy.operators import dot


class dotTestCase(unittest.TestCase):

    # Test input type - Input argument should be a dictionary.
    def test_dot_1(self):
        A = [(1,0.1), (2,0.8), (3,0.5)]
        B = [(1, 0.2), (2, 0.7), (3, 0.4)]
        self.assertRaises(TypeError, lambda: dot.dot(A, B))

    # Test input type - Input argument should be a dictionary.
    def test_dot_2(self):
        A = [[1, 0.1], (2, 0.8), [3, 0.5]]
        B = [[1, 0.2], [2, 0.7], [3, 0.4]]
        self.assertRaises(TypeError, lambda: dot.dot(A, B))

    # Test input type - Input argument should be a dictionary.
    def test_dot_3(self):
        A = 0.1
        B = 0.4
        self.assertRaises(TypeError, lambda: dot.dot(A, B))

    # Test input size - Dictionary should have at least one set.
    def test_dot_4(self):
        A = {}
        B = {1:0.2, 2:0.5}
        self.assertRaises(ValueError, lambda: dot.dot(A, B))

    # Test key type - Key of dictionary should be a int.
    def test_defuzz_som_5(self):
        A = {1.0: 0.1, 2.5: 0.8, 3.4: 0.3}
        B = {1.0: 0.3, 2.5: 0.2, 3.4: 0.3}
        self.assertRaises(TypeError, lambda: dot.dot(A, B))

    # Test value type - Value of dictionary should be a float or int.
    def test_dot_6(self):
        A = {1: '0.1', 2: '0.2', 3: '0.3'}
        B = {1: 0.8, 2: '0.4', 3: '1'}
        self.assertRaises(TypeError, lambda: dot.dot(A, B))

    # Test value type - Value of dictionary should be a float or int.
    def test_dot_7(self):
        A = {1: [0.2], 2: [0.2], 3: [0.1]}
        B = {1: [0.3], 2: [0.4], 3: [0.9]}
        self.assertRaises(TypeError, lambda: dot.dot(A, B))

    # Test value range - Value should be between 0 or 1.
    def test_dot_8(self):
        A = {1: 2, 2: 4.5, 3: -2}
        B = {1: 5, 2: 3.1, 3: -1}
        self.assertRaises(ValueError, lambda: dot.dot(A, B))

    def test_dot_9(self):
        A = {1: 0.1, 2: 0.7, 3: 0.4}
        B = {1: 0.9, 2: 0.2, 3: 0.5}
        self.assertEqual(dot.dot(A,B), 0.4)

    def test_dot_10(self):
        A = {0: 0, 1: 0.8, 2: 0.3, 3: 0.14, 4: 0.74, 5: 0.28, 6: 1, 7: 0.2, 8: 0.8}
        B = {0: 1, 1: 0.3, 2: 0.33, 3: 0.96, 4: 0.35, 5: 0.66, 6: 0.2, 7: 0.7, 8: 0.62}
        self.assertEqual(dot.dot(A, B), 0.62)


# Run all unittests
if __name__ == '__main__':
    unittest.main()

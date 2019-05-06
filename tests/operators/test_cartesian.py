import unittest
import string
from pyfuzzy.operators import cartesian


class UnionMaxTestCase(unittest.TestCase):

    def test_cartesian_1(self):
        u, v = [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]
        a = {1: 0, 2: 0.2, 3: 0.4, 4: 0.6, 5: 0.8, 6: 1}
        b = {1: 0, 2: 0.2, 3: 0.4, 4: 0.6, 5: 0.8, 6: 1}
        out = {(1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0, (2, 1): 0, (2, 2): 0.2, (2, 3): 0.2,
               (2, 4): 0.2, (2, 5): 0.2, (2, 6): 0.2, (3, 1): 0, (3, 2): 0.2, (3, 3): 0.4, (3, 4): 0.4, (3, 5): 0.4,
               (3, 6): 0.4, (4, 1): 0, (4, 2): 0.2, (4, 3): 0.4, (4, 4): 0.6, (4, 5): 0.6, (4, 6): 0.6, (5, 1): 0,
               (5, 2): 0.2, (5, 3): 0.4, (5, 4): 0.6, (5, 5): 0.8, (5, 6): 0.8, (6, 1): 0, (6, 2): 0.2, (6, 3): 0.4,
               (6, 4): 0.6, (6, 5): 0.8, (6, 6): 1}

        self.assertEqual(cartesian.cartesian(u, v, a, b, "min"), out)

    def test_cartesian_2(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        v = {}
        a = {"a": 0.2, "b": 0.7}
        b = 2
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_3(self):
        u = []
        v = []
        a = {"a": 1.0, "b": 0.4, "c": 0.9}
        b = {"a": 0.6, "b": 0.5, "c": 1.0}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_4(self):
        u = ["a", "b", "c"]
        v = ["a"]
        a = {"b"}
        b = {"a": 1.0, "c": 0.8}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_5(self):
        u = ["a", "b", "c"]
        v = ["a", "b", "c", "d"]
        a = {"a": 1.0, "b": 0.3, "c": 0.7}
        b = {"a": 0.6, "b": 0.5, "c": 0.8, "d": 0.7}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_6(self):
        u = ["a", "b"]
        v = []
        a = {"a": 1.0, "b": 3.0, "c": 1.0}
        b = {"a": 0.6, "b": 0.5}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_7(self):
        u = ["a", "b", "c"]
        v = ["a", "b", "c"]
        a = {"a": 0.8, "b": 0.8, "c": 0.7}
        b = {"a": 0.6, "b": 0.5, "c": 'aaaa'}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_8(self):
        u = {"b", "z"}
        v = u
        a = {"a": 1.0, "b": 0.6, "c": 0.7}
        b = {"a": 0.6, "b": 0.5, "c": 0.8}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_9(self):
        u = list(string.ascii_lowercase)
        v = list(string.ascii_lowercase)
        a = {"a": 0.2, "b": 0.1, "c": 0.7}
        b = {"a": 0.6, "b": 0.5, "c": 0.8}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_10(self):
        u = list(string.ascii_lowercase)
        v = list(string.ascii_lowercase)
        a = {"a": 1.0, "b": 0.2, "c": 0.7}
        b = {"ggh": 0.6, "c": 0.8}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))
    #
    def test_cartesian_11b(self):
        u = list(string.ascii_lowercase)
        v = list(string.ascii_lowercase)
        a = {"a": 1.0, "b": 0.6, "c": 0.7}
        b = {"a": 0.6, "b": 0.5, "c": 0.8}
        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "min"))

    def test_cartesian_12(self):
        u = list(range(10))
        v = list(range(10))
        a = {1: 0, 2: 0.2, 3: 0.4, 4: 0.6, 5: 0.8, 6: 1}
        b = {1: 1, 2: 0, 3: 0.4, 9: 0.6}
        out = {(0, 0): 0.0, (0, 1): 0.0, (0, 2): 0.0, (0, 3): 0.0, (0, 4): 0.0, (0, 5): 0.0, (0, 6): 0.0, (0, 7): 0.0,
               (0, 8): 0.0, (0, 9): 0.0, (1, 0): 0.0, (1, 1): 0, (1, 2): 0, (1, 3): 0.0, (1, 4): 0.0, (1, 5): 0.0,
               (1, 6): 0.0, (1, 7): 0.0, (1, 8): 0.0, (1, 9): 0.0, (2, 0): 0.0, (2, 1): 0.2, (2, 2): 0.0,
               (2, 3): 0.08000000000000002, (2, 4): 0.0, (2, 5): 0.0, (2, 6): 0.0, (2, 7): 0.0, (2, 8): 0.0,
               (2, 9): 0.12, (3, 0): 0.0, (3, 1): 0.4, (3, 2): 0.0, (3, 3): 0.16000000000000003, (3, 4): 0.0,
               (3, 5): 0.0, (3, 6): 0.0, (3, 7): 0.0, (3, 8): 0.0, (3, 9): 0.24, (4, 0): 0.0, (4, 1): 0.6,
               (4, 2): 0.0, (4, 3): 0.24, (4, 4): 0.0, (4, 5): 0.0, (4, 6): 0.0, (4, 7): 0.0, (4, 8): 0.0,
               (4, 9): 0.36, (5, 0): 0.0, (5, 1): 0.8, (5, 2): 0.0, (5, 3): 0.32000000000000006, (5, 4): 0.0,
               (5, 5): 0.0, (5, 6): 0.0, (5, 7): 0.0, (5, 8): 0.0, (5, 9): 0.48, (6, 0): 0.0, (6, 1): 1, (6, 2): 0,
               (6, 3): 0.4, (6, 4): 0.0, (6, 5): 0.0, (6, 6): 0.0, (6, 7): 0.0, (6, 8): 0.0, (6, 9): 0.6, (7, 0): 0.0,
               (7, 1): 0.0, (7, 2): 0.0, (7, 3): 0.0, (7, 4): 0.0, (7, 5): 0.0, (7, 6): 0.0, (7, 7): 0.0, (7, 8): 0.0,
               (7, 9): 0.0, (8, 0): 0.0, (8, 1): 0.0, (8, 2): 0.0, (8, 3): 0.0, (8, 4): 0.0, (8, 5): 0.0, (8, 6): 0.0,
               (8, 7): 0.0, (8, 8): 0.0, (8, 9): 0.0, (9, 0): 0.0, (9, 1): 0.0, (9, 2): 0.0, (9, 3): 0.0, (9, 4): 0.0,
               (9, 5): 0.0, (9, 6): 0.0, (9, 7): 0.0, (9, 8): 0.0, (9, 9): 0.0}

        self.assertEqual(cartesian.cartesian(u, v, a, b, "product"), out)

    def test_cartesian_13(self):
        u = {1, 2, 3, 4, 5, 67}
        v = {2, 3, 5, 6, 7, 8}
        a = {5: 0.8, 67: 1.0}
        b = {1: 0.8, 8: 1.0}

        self.assertRaises(TypeError, lambda: cartesian.cartesian(u, v, a, b, "product"))

    def test_cartesian_14(self):
        u, v = [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]
        a = {1: 0, 2: 0.2, 3: 0.4, 4: 0.6, 5: 0.8, 6: 1}
        b = {1: 0, 2: 0.2, 3: 0.4, 4: 0.6, 5: 0.8, 6: 1}
        out = {(1, 1): 0, (1, 2): 0.0, (1, 3): 0.0, (1, 4): 0.0, (1, 5): 0.0, (1, 6): 0, (2, 1): 0.0,
               (2, 2): 0.04000000000000001, (2, 3): 0.08000000000000002, (2, 4): 0.12, (2, 5): 0.16000000000000003,
               (2, 6): 0.2, (3, 1): 0.0, (3, 2): 0.08000000000000002, (3, 3): 0.16000000000000003, (3, 4): 0.24,
               (3, 5): 0.32000000000000006, (3, 6): 0.4, (4, 1): 0.0, (4, 2): 0.12, (4, 3): 0.24, (4, 4): 0.36,
               (4, 5): 0.48, (4, 6): 0.6, (5, 1): 0.0, (5, 2): 0.16000000000000003, (5, 3): 0.32000000000000006,
               (5, 4): 0.48, (5, 5): 0.6400000000000001, (5, 6): 0.8, (6, 1): 0, (6, 2): 0.2, (6, 3): 0.4,
               (6, 4): 0.6, (6, 5): 0.8, (6, 6): 1}

        self.assertEqual(cartesian.cartesian(u, v, a, b, "product"), out)


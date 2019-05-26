import unittest
from pyfuzzy.operators import compose_maxproduct

class Compose_MaxproductTestCase(unittest.TestCase):

    def test_compose_max_product_1(self):  # validation of a type being dictionary
        a = 2.4
        b = {"a": 1.0, "b": 1.0}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_2(self):  # validation of b type being dictionary
        a = {"a": 1.0}
        b = bool(0)
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_3(self):  # validation of a & b be the subset of u
        u = {1: 1.0, 2: 1.0, 3: 1.0}
        a = {(1, 1): 1.0}
        b = {(1, 1): 1.0, (1, 2): 1.0}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(u, a, b))

    def test_compose_max_product_4(self):  # validation of each dictionary item type being float
        a = {"a": 1.0, "b": "1.0e", "c": 1.0}
        b = {"b": 1.0}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_5(self):  # validation of each a's items being in the range of [0,1]
        a = {"a": 5.1, "b": 0.2}
        b = {"a": 0.2, "b": 0.3}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_6(self):  # validation of each b's items being in the range of [0,1]
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 2.0}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_7(self):  # validation of each a's items being float
        a = {"a": 0.2, "b": 'nan'}
        b = {"a": 1.0, "b": 1.0}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_8(self):  # validation of each b's items being float
        a = {"a": 0.2, "b": 0.4}
        b = {"a": 1.0, "b": 'nan'}
        self.assertRaises(TypeError, lambda: compose_maxproduct.compose_maxproduct(a, b))

    def test_compose_max_product_9(self):  # validation output of function for fuzzy relations
        a = {(1, 1): 0.2, (1, 2): 0.1, (2, 1): 0.6, (2, 2): 0.8}
        b = {(1, 1): 0.5, (1, 2): 0.7, (1, 3): 0.6, (2, 1): 0.4, (2, 2): 0.8, (2, 3): 0.3}
        self.assertEqual(compose_maxproduct.compose_maxproduct(a, b),
                         {(1, 1): 0.1, (1, 2): 0.14, (1, 3): 0.12, (2, 1): 0.32, (2, 2): 0.64, (2, 3): 0.36})

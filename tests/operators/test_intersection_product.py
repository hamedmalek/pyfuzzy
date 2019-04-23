import unittest
from pyfuzzy.operators import intersection_product

class IntersectionMinTestCase(unittest.TestCase):

    def test_intersection_product_1(self): #validation of u type being dictionary
        u = "input"
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_2(self): #validation of a type being dictionary 
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = 2.4
        b = {"a": 1.0, "b": 1.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_3(self): #validation of b type being dictionary 
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = bool(0)
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_4(self): #validation of a & b be the subset of u
        u = {1: 1.0, 2: 1.0, 3: 1.0}
        a = {(1,1): 1.0}
        b = {(1,1): 1.0, (1,2): 1.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))
		
    def test_intersection_product_5(self): #validation of each dictionary item type being float
        u = {"a": 1.0, "b": "1.0e", "c": 1.0}
        a = {"a": 1.0, "b":0.3}
        b = {"b": 1.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_6(self): #validation of b being a subset of u
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"b": 0.2, "c": 0.3}
        b = {"d": 1.0, "e": 0.9}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_7(self): #validation of each a's items being in the range of [0,1]
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 5.1, "b": 0.2}
        b = {"a": 0.2, "b": 0.3}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_8(self): #validation of each b's items being in the range of [0,1]
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 2.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_9(self): #validation of each a's items being float
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a":0.2,"b": 'nan'}
        b = {"a": 1.0, "b": 1.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_10(self): #validation of each b's items being float
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a":0.2,"b": 0.4}
        b = {"a": 1.0, "b": 'nan'}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))
		
    def test_intersection_product_11(self): #validation of each u's items being 1.0
        u = {"a": 0.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"b": 1.0}
        self.assertRaises(TypeError, lambda: intersection_product.intersection_product(u, a, b))

    def test_intersection_product_12(self): #validation output of function for fuzzy sets
        u = {1: 1.0, 2: 1.0, 3: 1.0}
        a = {1: 1.0}
        b = {1: 1.0}
        self.assertEqual(intersection_product.intersection_product(u, a, b), {1: 1.0, 2: 0, 3: 0})

    def test_intersection_product_13(self): #validation output of function for fuzzy relations
        u = {(1,1): 1, (1,2): 1, (1,3): 1,(2,1):1, (2,2):1,(2,3):1,(3,1):1, (3,2):1,(3,3):1}
        a = {(1,1): 1,(3,1):0.3}
        b = {(1,1):0.5,(1,2): 1,(3,1):0.2}
        self.assertEqual(intersection_product.intersection_product(u, a, b), {(1, 1): 0.5, (1, 2): 0, (1, 3): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0, (3, 1): 0.06, (3, 2): 0, (3, 3): 0})

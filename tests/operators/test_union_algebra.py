import unittest
from mf import union_algebra

class UnionAlgebraTestCase(unittest.TestCase):

    def test_union_algebra_1(self):
        u = 2
        a = {"a": 1.0,"b":1.0,"c":1.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_2(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = 1
        b = {"a": 1.0, "b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_3(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0, "c":1.0}
        b = 1
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_4(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"d": 1.0, "c": 0.2}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_5(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0, "b": 1.0, "c": 0.2}
        b = {"d": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_6(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 2.0, "b": 0.5,"c": 0.4}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_7(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0, "b": 0.2, "c": 0.3}
        b = {"b": 1.0, "c": 2.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_8(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 'c'}
        b = {"a": 0.5, "b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_9(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0, "b": 0.5,"c": 0.1}
        b = {"b": 1.0, "c": 'b'}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_10(self):
        u = {"a": 0.5, "b": 1.0, "c": 1.0}
        a = {"a": 1.0,"b": 0.5}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_11(self):
        u = {"a": 'cd', "b": 1.0, "c": 1.0}
        a = {"a": 0.5,"b":0.5,"c":0.6}
        b = {"a": 0.4 ,"b": 0.3, "c": 1.0}
        self.assertRaises(TypeError, lambda: union_algebra.union_algebra(u, a, b))

    def test_union_algebra_12(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = { "b": 0.7, "c": 0.8}
        b = {"a": 0.3, "b": 0.2, "c": 0.7}
        self.assertEqual(union_algebra.union_algebra(u, a, b), {'a': 0.3, 'b': 0.7599999999999999, 'c': 0.9400000000000001} )

    def test_union_algebra_13(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 0.4, "b": 0.3, "c": 0.5}
        b = {"a": 0.2, "b": 0.65, "c": 0.1}
        self.assertEqual(union_algebra.union_algebra(u, a, b), {'a': 0.52, 'b': 0.7549999999999999, 'c': 0.5499999999999999})
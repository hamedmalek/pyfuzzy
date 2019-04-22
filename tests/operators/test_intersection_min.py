import unittest
from pyfuzzy.operators import intersection_min

class IntersectionMinTestCase(unittest.TestCase):

    def test_intersection_min_1(self):
        u = 1
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_2(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = 1
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_3(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = 1
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_4(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"d": 1.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_5(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"d": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_6(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 3.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_7(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 2.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_8(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 'baghali'}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_9(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 'baghali'}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_10(self):
        u = {"a": 0.5, "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_10(self):
        u = {"a": 'asghar', "b": 1.0, "c": 1.0}
        a = {"a": 1.0}
        b = {"b": 1.0, "c": 1.0}
        self.assertRaises(TypeError, lambda: intersection_min.intersection_min(u, a, b))

    def test_intersection_min_11(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 0.5, "b": 0.1, "c": 0.8}
        b = {"a": 0.3, "b": 0.2, "c": 0.7}
        self.assertEqual(intersection_min.intersection_min(u, a, b), {"a": 0.3, "b": 0.1, "c": 0.7})

    def test_intersection_min_12(self):
        u = {"a": 1.0, "b": 1.0, "c": 1.0}
        a = {"a": 0.5, "b": 0.2}
        b = {"b": 0.1, "c": 0.7}
        self.assertEqual(intersection_min.intersection_min(u, a, b), {"a": 0.0, "b": 0.1, "c": 0.0})
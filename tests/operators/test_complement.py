import unittest
from pyfuzzy.operators import complement

class ComplementTestCase(unittest.TestCase):

    def test_Complement_1(self):
        A = [0.2,0.3,0.7]
        U = {1: 1.0, 2: 1.0}
        self.assertRaises(TypeError, lambda: complement.complement(U,A))

    def test_Complement_2(self):
        A = {1:0.2,2:0.5,3:0.4}
        U = [1,1,1]
        self.assertRaises(TypeError, lambda: complement.complement(U,A))

    def test_Complement_3(self):
        A = {1:0.2,2:0.5,3:0.4,4:0.5}
        U = {1: 1.0, 2: 1.0,3:1.0}
        self.assertRaises(TypeError, lambda: complement.complement(U,A))

    def test_Complement_4(self):
        A = {1:1.2,2:1.5,3:1.4}
        U = {1: 1.0, 2: 1.0,3:1.0}
        self.assertRaises(TypeError, lambda: complement.complement(U,A))

    def test_Complement_5(self):
        A = {1:0.2,2:0.5,3:"0.4"}
        U = {1: 1.0, 2: 1.0,3:1.0}
        self.assertRaises(TypeError, lambda: complement.complement(U,A))

    def test_Complement_6(self):
        A = {1:0.2,2:0.5,3:0.4}
        U = {1: 1.0, 2: 0.5,3:1.0}
        self.assertRaises(TypeError, lambda: complement.complement(U,A))

    def test_Complement_7(self):
        A = {1:0.2,2:0.5,3:0.4}
        U = {1: 1.0, 2: 1.0,3:1.0}
        self.assertEqual(complement.complement(U,A), {1:0.8,2:0.5,3:0.6})

    def test_Complement_8(self):
        A = {1:0.6, 2:0.5, 3:0.5, 4:0.1, 5:0.25}
        U = {1:1.0, 2:1.0, 3:1.0, 4:1.0, 5:1.0}
        self.assertEqual(complement.complement(U,A), {1:0.4, 2:0.5, 3:0.5, 4:0.9, 5:0.75})

    def test_Complement_9(self):
        A = {1:0.6, 2:0.5, 3:0.5, 4:0.1, 5:0.25, 6:0.75, 7:0.64, 8:0.2}
        U = {1:1.0, 2:1.0, 3:1.0, 4:1.0, 5:1.0, 6:1.0, 7:1.0, 8:1.0}
        self.assertEqual(complement.complement(U,A), {1:0.4, 2:0.5, 3:0.5, 4:0.9, 5:0.75, 6:0.25, 7:0.36, 8:0.8})

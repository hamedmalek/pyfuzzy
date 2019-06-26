import unittest
from pyfuzzy.operators import image_maxmin

class image_maxminTestCase(unittest.TestCase):

    def test_image_maxmin_1(self):  # validation of the type of A as a dictionary
        A = bool('true')
        R = {(1,1): 0.6, (1,2): 0.2,(2,1):0.7,(2,2):0.8}
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_2(self):  # validation of the type of R as a dictionary
        A = {"x1": 0.3,"x2":0.6}
        R = {1,3,5,2}
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_3(self):  # validation of A and R's first dimension both being the subset of X
        A = {"y1": 1.0, "y2":0.7, "y3":0.4} #A is subset of Y
        R = {"u1,x1": 0.2, "u1,x2": 1.0,"u2,x1":0.8,"u2,x2":0.4,"u3,x1":0.6,"u3,x2":0.3} #R is from the space of U*X
        #but R should be from the space of Y*X or A should be subset of U
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_4(self):  # validation of each A's items being in the range of [0,1]
        A = {"u1": 0.7, "u2": 0.5,"u3":6.0}
        R = {"u1,y1": 1.0, "u2,y1": 0.2, "u3,y1":0.9}
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_5(self):  # validation of each R's item being in the range of [0,1]
        A = {"a": 1.0,"b":0.4}
        R = {"a,y1": 1.0,"a,y2":0.4,"b,y1":0.6 ,"b,y2": 4.0}
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_6(self):  # validation of each A's item being float
        A = {"x1": 0.4, "x2": "u2"}
        R = {"x1,y1": 0.3, "x2,y1": 0.5}
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_7(self):  # validation of each R's item being float
        A = {"x1": 0.2, "x2": 0.4,"x3":0.9}
        R = {"x1,y1": 1.0, "x2,y1": "unknownVal", "x3,y1":0.2}
        self.assertRaises(TypeError, lambda: image_maxmin.image_maxmin(R, A))

    def test_image_maxmin_8(self):  # first output validation of function 
        A = {1: 0.1, 2: 0.2, 3: 1.0}
        R = {(1, 1): 0.3, (1, 2): 0.7, (2, 1): 0, (2, 2): 0.8, (3, 1): 1.0, (3, 2): 0.4}
        self.assertEqual(image_maxmin.image_maxmin(R, A),{1: 1.0, 2: 0.4})
    def test_image_maxmin_9(self):  # second output validation of function 
        A = {"x1": 0.4, "x2": 0.6}
        R = {"x1,y1": 0.1, "x1,y2": 0.7, "x1,y3": 0.8, "x2,y1": 0.1, "x2,y2": 1.0, "x2,y3": 0.2}
        self.assertEqual(image_maxmin.image_maxmin(R, A),{"y1": 0.1, "y2": 0.6,"y3":0.4})
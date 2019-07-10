import unittest
from pyfuzzy.operators import image_maxproduct

    class image_maxproductTestCase(unittest.TestCase):

        # Test input type - Input argument should be a dictionary.
        def test_image_maxproduct_1(self):
            A = [1, 2, 3] # list is not a dictionary
            self.assertRaises(TypeError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test input type - Input argument should be a dictionary.
        def test_image_maxproduct_2(self):
            A = [[1], [2], [3]]
            B = [1:2,12:13,15:16]
            self.assertRaises(TypeError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test input type - Input argument should be a dictionary.
        def test_image_maxproduct_3(self):
            R , A = 0.1
            self.assertRaises(TypeError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test input size - Dictionary should have at least one set.
        def test_image_maxproduct_4(self):
            A , R = {}
            self.assertRaises(ValueError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test key type - Key of dictionary should be a int.
        def test_image_maxproduct_5(self):
            A , R = {1.0: 0.1, 2.0: 0.2, 3.0: 0.3}
            self.assertRaises(TypeError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test value type - Value of dictionary should be a float or int.
        def test_image_maxproduct_6(self):
            A , R = {1: '0.1', 2: '0.2', 3: '0.3'}
            self.assertRaises(TypeError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test value type - Value of dictionary should be a float or int.
        def test_image_maxproduct_7(self):
            R , A = {1: [0.2], 2: [0.2], 3: [0.1]}
            self.assertRaises(TypeError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test value range - Value should be between 0 or 1.
        def test_image_maxproduct_8(self):
            R , A = {1: 2, 2: 3.5, 3: -1}
            self.assertRaises(ValueError, lambda: image_maxproduct.image_maxproduct(R, A))

        # Test  - return image_max_product value
        def test_image_maxproduct_9(self):
            R = {1:1}
            A = {1:0}
            result = {1:0}
            self.assertEqual(image_maxproduct.image_maxproduct(R, A), result)

        # Test  - return image_max_product value
        def test_image_maxproduct_10(self):
            R = {1:[0.2,0.4,0.5],2:[0.4,0.8,0.1],3:[0.5,0.1,1]}
            A = {1:0.3}
            result = {1:0.15}
            self.assertEqual(image_maxproduct.image_maxproduct(R, A), result)

        # Test  - return image_max_product value
        def test_image_maxproduct_11(self):
            R = {1:[0.2,0.4,0.5],2:[0.4,0.8,0.1],3:[0.5,0.1,1]}
            A = {1:1,2:1,3:1}
            result = {1:1 ,2:1 ,3:1}
            self.assertEqual(image_maxproduct.image_maxproduct(R, A), result)

        # Test  - return image_max_product value
        def test_image_maxproduct_12(self):
            R = {1: [0.2, 0.4, 0.5], 2: [0.4, 0.8, 0.1], 3: [0.5, 0.1, 1]}
            A = {1: 0, 2: 0, 3: 0}
            result = {1: 0, 2: 0, 3: 0}
            self.assertEqual(image_maxproduct.image_maxproduct(R, A), result)


        # Test  - return image_max_product value
        def test_image_maxproduct_13(self):
            R = {1: [0.2, 0.4, 0.5], 2: [0.4, 0.8, 0.1], 3: [0.5, 0.1, 1]}
            A = {1: 1, 2: 0.5, 3: 0}
            result = {1: 0.2, 2: 0.4, 3: 0.5}
            self.assertEqual(image_maxproduct.image_maxproduct(R, A), result)


    # Run all unittests
    if __name__ == '__main__':
        unittest.main()
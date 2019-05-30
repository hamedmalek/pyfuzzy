import unittest
from pyfuzzy.operators import slightly

class SlightlyTestCase(unittest.TestCase):

    def test_slightly(self):  # error about wrong type of input
        with self.assertRaises(TypeError):
            a = [1,2,3,4,5]
            slightly.slightly(a)

    def test_slightly1(self):  # error about great values in dic
        with self.assertRaises(TypeError):
            a = {0: 0.2, 1: 0.5, 2: 1.3}
            slightly.slightly(a)


    def test_slightly2(self):  # error about int values in dic
        with self.assertRaises(TypeError):
            a = {0: 1, 1: 0.5, 2: 0.9}
            slightly.slightly(a)


    def test_slightly3(self):  # error about right values
        a = {1: 0.8, 2: 0.5, 3: 1.0, 4: 0.3}
        self.assertEqual(slightly.slightly(a), {1: 0.8944271909999159, 2: 0.7071067811865475, 3: 1.0, 4: 0.5477225575051661})


if __name__ == '__main__':
    unittest.main()


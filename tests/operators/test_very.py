
import unittest
import very

class veryTestCase(unittest.TestCase):
   # Test input type - Input argument should be a dictionary
   def test_very_1(self):
      A = [(1,0.1), (2,0.8), (3,0.5)]
      self.assertRaises(TypeError, lambda: very(A))
   
   # Test input type - Input argument should be a dictionary
   def test_very_2(self):
      A = [[1,0.1], [2,0.8], [3,0.5]]
      self.assertRaises(TypeError, lambda: very(A))
   
   # Test input type - Input argument should be a dictionary
   def test_very_3(self):
      A = 2.1
      self.assertRaises(TypeError, lambda: very(A))
   
   # Test input size - Input dictionary should have at least one set
   def test_very_4(self):
      A = {}
      self.assertRaises(ValueError, lambda: very(A))
   
   # Test value type - Input dictionary values should be int or float type
   def test_very_5(self):
      A = {1:'0.1', 2:'0.2', 3:'0.3'}
      self.assertRaises(TypeError, lambda: very(A))

   # Test value type - Input dictionary values should be int or float type
   def test_very_6(self):
      A = {1:[0.1], 2:[0.2], 3:[0.3]}
      self.assertRaises(TypeError, lambda: very(A))

   # Test value range - Input values should be between 0 and 1
   def test_very_7(self):
      A = {1:0.5, 2:3, 3:0.3}
      self.assertRaises(ValueError, lambda: very(A))

   # Test output
   def test_very_8(self):
      A = {1:0.9, 2:0.2, 3:0.5}
      B = {1:0.81, 2:0.04, 3:0.25}
      self.assertDictEqual(very(A), B)
      
if __name__ == '__main__':
    unittest.main()

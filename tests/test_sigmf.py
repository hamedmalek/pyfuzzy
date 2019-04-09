import unittest
from pyfuzzy.mf import sigmf


class sigmfTestCase(unittest.TestCase):
    def test_gaussian_membership_function(self):
        self.assertEqual(sigmf.sigmf(0, [1.0, 0.0]), 0.5)
        
    def test_gaussian2_membership_function(self):   
        self.assertRaises( TypeError, lambda:sigmf.sigmf(0, [1.0, 0.0, 2.0]))
        
    def test_gaussian3_membership_function(self):  
        self.assertRaises( TypeError, lambda:sigmf.sigmf(0, 1.0 ))
      
    def test_gaussian4_membership_function(self): 
        self.assertRaises( TypeError, lambda:sigmf.sigmf(0, [ ] ))
         
    def test_gaussian5_membership_function(self):    
        self.assertRaises( TypeError, lambda:sigmf.sigmf(0, [1.0, ] )) 
     
    def test_gaussian6_membership_function(self):
        self.assertRaises( TypeError, lambda:sigmf.sigmf(0, [1, 0.0]))
        
    def test_gaussian7_membership_function(self):  
        self.assertRaises( TypeError, lambda:sigmf.sigmf(0, [1.0, 0]))
        
         ####
    def test_gaussian8_membership_function(self):
        self.assertEqual(sigmf.sigmf(0, [0.0, 1.0]), 0.5) 
        
    def test_gaussian9_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(0, [1.0, 0.5]), 0.3775, places=4)
        
        
    def test_gaussian10_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(1, [1.0, 1.0]), 0.5, places=4)
        
    def test_gaussian11_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(1, [1.0, 0.0]), 0.731, places=3)
        
    def test_gaussian12_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(1, [0.0, 0.0]), 0.5, places=3)
        
    def test_gaussian13_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(-1, [1.0, 0.5]), 0.1824, places=4)
        
    def test_gaussian14_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(-2, [0.5, 0.2]), 0.2497, places=4)
    
    def test_gaussian15_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(1, [-0.5, -0.2]), 0.3543, places=4)
        
        
    def test_gaussian16_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(1, [-0.5, 0.2]), 0.4013, places=4)
        
    def test_gaussian17_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(1, [0.5, -0.2]), 0.645, places=2)
        
              
    def test_gaussian18_membership_function(self):
        self.assertAlmostEqual(sigmf.sigmf(-1, [-0.5, -0.2]), 0.5986, places=2)
        
   

if __name__ == '__main__':
    unittest.main()
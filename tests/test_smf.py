import unittest
from pyfuzzy.mf import smf


class smfTestCase(unittest.TestCase):
    def test_solinebasedcurve1_membership_function(self):
        self.assertEqual(smf.smf(0, [1.0, 0.0]), 0)
        
    def test_solinebasedcurve2_membership_function(self):   
        self.assertRaises( TypeError, lambda:smf.smf(1, [1.0, 0.0, 2.0]))
        
    def test_solinebasedcurve3_membership_function(self):  
        self.assertRaises( TypeError, lambda:smf.smf(0, 1.0 ))
      
    def test_solinebasedcurve4_membership_function(self): 
        self.assertRaises( TypeError, lambda:smf.smf(0, [ ] ))
         
    def test_solinebasedcurve5_membership_function(self):    
        self.assertRaises( TypeError, lambda:smf.smf(0, [1.0, ] )) 
     
    def test_solinebasedcurve6_membership_function(self):
        self.assertRaises( TypeError, lambda:smf.smf(0, [  0.0]))
        
    def test_solinebasedcurve7_membership_function(self):  
        self.assertRaises( TypeError, lambda:smf.smf( 1, -1.1))
        
         ####
    def test_solinebasedcurve8_membership_function(self):
        self.assertEqual(smf.smf(0, [1.0, -1.0]), 0.0) 
        
    def test_solinebasedcurve9_membership_function(self):
        self.assertAlmostEqual(smf.smf(1, [-1.0, -0.5]), 1.0)        
        
    def test_solinebasedcurve10_membership_function(self):
        self.assertAlmostEqual(smf.smf(1, [1.0, 1.0]), 0.0)
        
    def test_solinebasedcurve11_membership_function(self):
        self.assertAlmostEqual(smf.smf(1, [1.0, 0.0]), 0.0)
        
    def test_solinebasedcurve12_membership_function(self):
        self.assertAlmostEqual(smf.smf(0, [0.0, 0.0]), 0.0)
        
    def test_solinebasedcurve13_membership_function(self):
        self.assertAlmostEqual(smf.smf(-1, [1.0, 0.5]), 0.0)
        
    def test_solinebasedcurve14_membership_function(self):
        self.assertAlmostEqual(smf.smf(-2, [0.5, 0.2]), 0.0)
    
    def test_solinebasedcurve15_membership_function(self):
        self.assertAlmostEqual(smf.smf(1, [-0.5, -0.2]), 1.0)
             
    def test_solinebasedcurve16_membership_function(self):
        self.assertAlmostEqual(smf.smf(1, [-0.5, 0.2]), 1.0)
        
    def test_solinebasedcurve17_membership_function(self):
        self.assertAlmostEqual(smf.smf(1, [0.5, -0.2]), 1.0)
                   
    def test_solinebasedcurve18_membership_function(self):
        self.assertAlmostEqual(smf.smf(-1, [-0.5, -0.2]), 0.0)
        
   

if __name__ == '__main__':
    unittest.main()

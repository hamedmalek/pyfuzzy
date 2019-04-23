import unittest
from pyfuzzy.operators import mf2dict
from pyfuzzy.mf import gaussmf
from pyfuzzy.mf import gbellmf
from pyfuzzy.mf import pimf
from pyfuzzy.mf import sigmf
from pyfuzzy.mf import smf
from pyfuzzy.mf import trapmf
from pyfuzzy.mf import trimf
from pyfuzzy.mf import zmf

class mf2dictTestCase(unittest.TestCase):

    def test_mf2dict_1(self):
        u = [1, 2, 3, 4, 5]
        a = 'gaussmf'
        b =  [4.0, 5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.835270211411272, 2: 0.9231163463866358, 3: 0.9801986733067553, 4: 1.0, 5: 0.9801986733067553})
     
    def test_mf2dict_2(self):
        u = [4, 5]
        a = 'gaussmf'
        b =  [-1.2, 3.6]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {4: 0.35232195499549696, 5: 0.22695019488695936})
        
    def test_mf2dict_3(self):
        u = [1, 2, 3, 4, 5]
        a = 'gbellmf'
        b =  [1.0, 3.0, 5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.000244081034903588, 2: 0.0013698630136986301, 3: 0.015384615384615385, 4: 0.5, 5: 1.0})

    def test_mf2dict_4(self):
        u = [1, 2, 3, 4]
        a = 'gbellmf'
        b =  [-0.51, -1.5, 5.3]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.9983343598529832, 2: 0.9963223653037285, 3: 0.9892150598419418, 4: 0.9430597115190215})
   
    def test_mf2dict_5(self):
        u = [1, 2, 3, 4, 5]
        a = 'pimf'
        b =  [2.0, 3.0, 4.0, 5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 0.0})
        
    def test_mf2dict_6(self):
        u = [1, 2, 3, 4]
        a = 'pimf'
        b =  [-2.8, 1.3, 4.5, 0.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.9892920880428316, 2: 1.0, 3: 1.0, 4: 1.0})
        
    def test_mf2dict_7(self):
        u = [1, 2, 3, 4, 5]
        a = 'sigmf'
        b =  [0.0, 1.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5, 5: 0.5})

    def test_mf2dict_8(self):
        u = [1, 2, 3]
        a = 'sigmf'
        b =  [-1.0, 1.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.5, 2: 0.2689414213699951, 3: 0.11920292202211755})

    def test_mf2dict_9(self):
        u = [1, 2, 3, 4, 5]
        a = 'smf'
        b =  [4.0, 5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 1.0})
   
    def test_mf2dict_10(self):
        u = [1, 2, 3, 4]
        a = 'smf'
        b =  [-3.2,  -1.2]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0})
      
    def test_mf2dict_11(self):
        u = [1, 2, 3, 4, 5]
        a = 'trapmf'
        b =  [2.0, 3.0, 4.0, 5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 0.0})
      
    def test_mf2dict_12(self):
        u = [1, 2, 3]
        a = 'trapmf'
        b =  [-1.3, 0.0, 4.7, 5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 1.0, 2: 1.0, 3: 1.0})
   
    def test_mf2dict_13(self):
        u = [1, 2, 3, 4, 5]
        a = 'trimf'
        b =  [1.0, 3.0, 4.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.0, 2: 0.5, 3: 1.0, 4: 0.0, 5: 0.0})
   
    def test_mf2dict_14(self):
        u = [1, 2, 3, 4]
        a = 'trimf'  
        b =  [-1.2,  -0.5 , -0.1]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0})
   
    def test_mf2dict_15(self):
        u = [1, 2, 3, 4, 5]
        a = 'zmf'
        b =  [4.1,  5.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0.0})

    def test_mf2dict_16(self):
        u = [1, 2, 3]
        a = 'zmf'
        b =  [-2.7, 4.0]
        self.assertEqual(mf2dict.mf2dict(u, a, b), {1: 0.4009801737580753, 2: 0.17821341055914455, 3: 0.04455335263978614})
    ###################
    def test_mf2dict_17(self):
        u = [1, 2, 3, 4, 5]
        a = 'gaussmf'
        b =  [4.0, -5.0, 0.9]
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))
        
    def test_mf2dict_18(self):
        u = [1, 2, 3, 4, 5]
        a = 'gaussmf'
        b =  []
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))
      
    def test_mf2dict_19(self):
        u = [1, 2, 3, 4, 5]
        a = 'trapmf'
        b =  [-2.0, -3.0, -4.0, -5.0]
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))
      
    def test_mf2dict_20(self):
        u = [1, 2, 3]
        a = 'trapmf'
        b =  [-1.3, 0.0, 4.7, 5.0, 0.0]
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))
   
    def test_mf2dict_21(self):
        u = [1, 2, 3, 4, 5]
        a = 'trimf'
        b =  [1.0, 4.0]
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))
   
    def test_mf2dict_22(self):
        u = [1, 2, 3, 4]
        a = 'trimf'  
        b =  []
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))
   
    def test_mf2dict_23(self):
        u = [1, 2, 3, 4, 5]
        a = 'zmf'
        b =  [4.1, 5.0, -1.0]
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))

    def test_mf2dict_24(self):
        u = [1, 2, 3]
        a = 'zmf'
        b =  [-2.7, 4.0, 0]
        self.assertRaises( TypeError, lambda:mf2dict.mf2dict(u, a, b))

    
if __name__ == '__main__':
    unittest.main()

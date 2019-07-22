import unittest
from pyfuzzy.mf import gaussmf
from pyfuzzy.anfis.anfis import ANFIS


class ANFISTestCase(unittest.TestCase):
    def test_ANFIS_constractor_learning_rate(self):
        with self.assertRaises(TypeError):
            ANFIS(10,3,False)

    def test_ANFIS_constractor_epochs(self):
        with self.assertRaises(TypeError):
            ANFIS(10.1,2.5,False)

    def test_ANFIS_constractor_epochs_value(self):
        with self.assertRaises(TypeError):
            ANFIS(10.1,1,False)

    def test_ANFIS_constractor_plot(self):
        with self.assertRaises(TypeError):
            ANFIS(10.1,3,"True")

    def test_ANFIS_dataset_prepare_path(self):
        anfis = ANFIS(10.1,3,True)
        with self.assertRaises(TypeError):
            anfis.dataset_prepare(5,2)

    def test_ANFIS_dataset_prepare_input_dim(self):
        anfis = ANFIS(10.1,3,True)
        with self.assertRaises(TypeError):
            anfis.dataset_prepare("trainingSet.txt",2.5)

    def test_ANFIS_membership_pattern_membership_type(self):
        anfis = ANFIS(10.1,3,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        with self.assertRaises(TypeError):
            anfis.membership_pattern(1,[0. , 1.])
            
    def test_ANFIS_membership_pattern_membership_value(self):
        anfis = ANFIS(10.1,3,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        with self.assertRaises(TypeError):
            anfis.membership_pattern("sample",[0. , 1.])

    def test_ANFIS_membership_pattern_param_type(self):
        anfis = ANFIS(10.1,3,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        with self.assertRaises(TypeError):
            anfis.membership_pattern("gaussmf",0.)

    def test_ANFIS_membership_pattern_param_len(self):
        anfis = ANFIS(10.1,3,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        with self.assertRaises(TypeError):
            anfis.membership_pattern("gaussmf",[0.,1.,2.])

    def test_ANFIS_membership_pattern_param_el1(self):
        anfis = ANFIS(10.1,3,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        with self.assertRaises(TypeError):
            anfis.membership_pattern("gaussmf",["0.",1.])

    def test_ANFIS_membership_pattern_param_el2(self):
        anfis = ANFIS(10.1,3,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        with self.assertRaises(TypeError):
            anfis.membership_pattern("gaussmf",[0.,"1."])
    
    def test_ANFIS_train_error_type(self):
        anfis = ANFIS(10e-4,5,False)
        anfis.dataset_prepare("trainingSet.txt",2)
        anfis.membership_pattern("gaussmf",[0. , 1.])
        with self.assertRaises(TypeError):
            anfis.train(1)

    def test_ANFIS_train_error_value(self):
        anfis = ANFIS(10e-4,5,False)
        anfis.dataset_prepare("trainingSet.txt",2)
        anfis.membership_pattern("gaussmf",[0. , 1.])
        with self.assertRaises(TypeError):
            anfis.train("lse")

    def test_ANFIS_train_converge_type(self):
        anfis = ANFIS(10e-4,5,False)
        anfis.dataset_prepare("trainingSet.txt",2)
        anfis.membership_pattern("gaussmf",[0. , 1.])
        with self.assertRaises(TypeError):
            anfis.train("se","0.05")

    def test_ANFIS_train_converge_value(self):
        anfis = ANFIS(10e-4,5,True)
        anfis.dataset_prepare("trainingSet.txt",2)
        anfis.membership_pattern("gaussmf",[0. , 1.])
        with self.assertRaises(TypeError):
            anfis.train("se",1.5)

            
    def test_Anfis_Neural_Network(self):
        anfis = ANFIS(10e-4,5,False)
        anfis.dataset_prepare("trainingSet.txt",2)
        anfis.membership_pattern("gaussmf",[0. , 1.])
        error,converge = anfis.train("se",10e-3)
        print("\nerror cost is",error,"\nconverge value is",converge)
        self.assertEqual(error[-2] >= error[-1] or error[-2] - error[-1] < 0.0001, True)

if __name__ == '__main__':
    unittest.main()
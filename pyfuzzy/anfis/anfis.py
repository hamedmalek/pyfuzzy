from pyfuzzy.mf.gaussmf import gaussmf
from pyfuzzy.mf.sigmf import sigmf
import numpy as np 


class ANFIS:
   def __init__(self,learning_rate,epochs,plot):
      if not isinstance(learning_rate, float):
        raise TypeError ("learning_rate should be a float.")

      if not isinstance(epochs, int):
        raise TypeError ("epochs should be a int.")

      if epochs < 2:
        raise TypeError ("epochs should be at least two.")

      if not isinstance(plot, bool):
        raise TypeError ("plot should be a bool.")

      self.learning_rate = learning_rate
      self.epochs = epochs
      self.plot = plot

   def dataset_prepare(self,dataset_path,input_dim):

      if not isinstance(dataset_path, str):
        raise TypeError ("dataset_path should be a string.")

      if not isinstance(input_dim, int):
        raise TypeError ("input_dim should be a int.")

      self.input_dim = input_dim
      try:
         dataset = np.loadtxt(dataset_path, usecols=[1,2,3])
      except OSError:
         print("dataset path did not correct! use default dataset.")
         dataset = np.loadtxt("trainingSet.txt", usecols=[1,2,3])
         self.input_dim=2

      self.x = dataset[:,0:input_dim] #on everything , just collect col 0 to 2
      self.y = dataset[:,input_dim] #on everything , just collect col 2
      self.rule_number = len(self.y)
   
   def membership_pattern(self,membership,param):
      if not isinstance(membership, str):
        raise TypeError ("membership should be a string.")

      if not(membership == "gaussmf" or membership == "sigmf"):
        raise TypeError ("membership should be a gaussmf or sigmf.")

      if not isinstance(param, list):
        raise TypeError ("param should be a list. [sigma , offset]")

      if len(param)!=2:
        raise TypeError ("param should be a have two element")

      self.membership_sample = np.zeros_like(self.x)
      for (a,b), value in np.ndenumerate(self.x):
         if membership == "gaussmf":
            self.membership_sample[a][b] = gaussmf(value , param)
         if membership == "sigmf":
            self.membership_sample[a][b] = sigmf(value , param)  

   def get_result(self):
      return self.w , self.Q

   def train(self,error_mode,converge_value=10e-3):
      if not isinstance(error_mode, str):
         raise TypeError ("error_mode should be a string.")
        
      if not(error_mode == "mse" or  error_mode == "se"):
        raise TypeError ("error_mode should be a \"mse\" for mean square error or \"se\" for square error.")

      if not isinstance(converge_value, float):
        raise TypeError ("converge value should be float")

      if converge_value > 1:
        raise TypeError ("converge value should be lower than 1")

      w1 = np.random.rand(self.input_dim,self.rule_number)  
      Q = np.random.rand(self.rule_number) 
      lr = self.learning_rate
      error_cost = [ ]

      for epoch in range(self.epochs): 
         ###### forward phase 1 #####
         z1 = np.dot(self.membership_sample,w1) 
         z1 = z1 / np.linalg.norm(z1)

         ###### forward phase 2 #####
         y_predict = np.dot(z1,Q)

         ###### forward phase 3 #####
         mse = ((self.y - y_predict)**2).mean(axis=None)
         se = np.sum((self.y - y_predict)**2)

         if error_mode == "mse":
            error_cost.append(mse)
         if error_mode == "se":
            error_cost.append(se)

         ###### backward phase 1 #####
         p1 = np.dot(z1,np.transpose(z1))
         try:
            p2 = np.linalg.pinv(p1)
         except np.linalg.LinAlgError:
            print("SVD not converge change membership function sigma and bias to correct value")
            p2 = p1

         Q = np.dot( np.dot(p2,np.transpose(z1)) , self.y)

         ####### backward phase 2 #####
         # dL_dw1 =  derror_da1 * da1_dz1 * dz1_dw1
         derror_da1 = mse
         da1_dz1 = z1
         dz1_dw1 = self.membership_sample
         dL_dw1 = np.dot(np.transpose(self.membership_sample),da1_dz1) * derror_da1

         w1 -= lr * dL_dw1

         if len(error_cost) >= 2 and error_cost[-2] - error_cost[-1] < converge_value:
            self.converge = True
            break
         else:
            self.converge = False


      self.w = w1
      self.Q = Q

      if self.plot:
         import matplotlib.pyplot as plt
         plt.title("Error cost")
         plt.xlabel("epochs")
         plt.ylabel("Errors per epoch")
         plt.plot(range(len(error_cost)),error_cost,color="r",marker="o")
         plt.show()

      return error_cost,self.converge

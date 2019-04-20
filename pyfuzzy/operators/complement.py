def complement(U, A):
   
    if not isinstance(U, dict):
        raise TypeError ("First Set should be a dictionary.")
    if not isinstance(A, dict):
        raise TypeError ("Second set should be a dictionary.")
    if  set(A.keys()).issubset(set(U.keys())) == False:
        raise TypeError ("Second Set should be a subset of the first set.")
    
    for key in U.keys():
        try:
           valueA = float(A.get(key, 0))
           if not(0 <= valueA <=1) :
               raise TypeError ("Value of corresponding key "+str(key)+" of second set should be between 0 and 1 ")
        except ValueError :
           raise TypeError ( A.get(key, 0) + " should be float.")
    
     
    previousKeyType=""
    for key,value in U.items():
        if previousKeyType=="" :
           previousKeyType=type(key)
        if type(key)!= previousKeyType :
           raise TypeError ("type ("+str(key)+") is " + str(type(key)) + " not " + str(previousKeyType) )
        try:
         val = float(value)
         if val !=1 :
             raise TypeError ("value should be equal to 1.0 ")
        except ValueError:
           raise TypeError ( value + " should be a number")
    
   
    complementResultDict = dict()
    for key in A.keys():
        mfA = A.get(key, 0)
        complementResultDict[key]= 1-mfA
    
    
    return complementResultDict


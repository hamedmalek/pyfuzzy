import math
def slightly(A):



    if not isinstance(A, dict):



        raise TypeError ("A should be a dictionary.")







    for key,value in A.items():



        try:



           val = float(value)



           if not(0 <= val <=1) :



               raise TypeError ("mfA("+str(key)+"):=> '" + str(value) + "' is not between [0,1] ")



        except ValueError :



           raise TypeError ("mfA("+str(key)+"):=> '" + value + "' is not a float!")







    for key in A.keys():



        try:



           val = float(key)



        except ValueError :



           raise TypeError ("Key:=> '"+str(key)+"' is not a float!")







    slightlyA = dict()



    for key,value in A.items():



        slightlyA[key]=round(sqrt(value), 4)







    return slightlyA

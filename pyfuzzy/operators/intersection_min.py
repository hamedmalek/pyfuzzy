def intersection_min(U, A, B):
    if not isinstance(U, dict):
        raise TypeError ("U should be a dictionary.")
    if not isinstance(A, dict):
        raise TypeError ("A should be a dictionary.")
    if not isinstance(B, dict):
        raise TypeError ("B should be a dictionary.")
    if  set(A.keys()).issubset(set(U.keys())) == False:
        raise TypeError ("Dictionary A is not subset of U.")
    if  set(B.keys()).issubset(set(U.keys())) == False:
        raise TypeError ("Dictionary B is not subset of U.")

    for key in U.keys():
        try:
           val = float(A.get(key, 0))
           if not(0 <= val <=1) :
               raise TypeError ("mfA("+str(key)+"):=> '" + str(val) + "' is not between [0,1] ")
        except ValueError :
           raise TypeError ("mfA("+str(key)+"):=> '" + A.get(key, 0) + "' is not a float!")

    for key in U.keys():
        try:
           val = float(B.get(key, 0))
           if not(0 <= val <=1) :
               raise TypeError ("mfB("+str(key)+"):=> '" + str(val) + "' is not between [0,1] ")
        except ValueError:
           raise TypeError ("mfB("+str(key)+"):=> '" + B.get(key, 0) + "' is not a float!")

    previousKeyType=""
    for key,value in U.items():
        print(key)
        if previousKeyType=="" :
            previousKeyType=type(key)
        if type(key)!= previousKeyType :
            raise TypeError ("type ("+str(key)+") is " + str(type(key)) + " not " + str(previousKeyType) )
        try:
           val = float(value)
           if val !=1 :
               raise TypeError ("mfU("+str(key)+"):=> '" + str(val) + "' is not egual 1.0 ")
        except ValueError:
           raise TypeError ("mfU("+str(key)+"):=> '" + value + "' is not a number!")



    intersection_min_dic = dict()
    for key in U.keys():
        mfA = A.get(key, 0)
        mfB = B.get(key, 0)
        intersection_min_dic[key]= min(mfA, mfB)

    return intersection_min_dic
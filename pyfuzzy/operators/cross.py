
def cross(mf1,mf2):

    #validatig data:
    if not isinstance(mf1, dict):
        raise TypeError("first input argument should be a dictionery.")
    if not isinstance(mf2, dict):
        raise TypeError("second input argument should be a dictionery.")

    if len( list(mf1.keys()) ) < 1 :
        raise ValueError("fisrt input argument should have at least one set.")
    if len( list(mf2.keys()) ) < 1 :
        raise ValueError("second input argument should have at least one set.")

    for key , value in mf1.items():
        if not isinstance(key, int):
            raise TypeError("key of first input argument should be a int.")

        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("value of first input argument should be a float or int.")

        if value > 1 or value < 0:
            raise ValueError("value of first input argument should be between 0 or 1.")

    for key , value in mf2.items():
        if not isinstance(key, int):
            raise TypeError("key of second input argument should be a int.")

        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("value of second input argument should be a float or int.")

        if value > 1 or value < 0:
            raise ValueError("value of second input argument should be between 0 or 1.")

    max_set=[]
    for item1,item2 in zip(mf1.values(),mf2.values()):
        max_set.append(max(item1,item2))

    return min(max_set)

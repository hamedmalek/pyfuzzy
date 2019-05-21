def intensify (A):

    if not isinstance(A, dict):
        raise TypeError("A should be a dict as a fuzzy set.")

    result = dict()



    for key in A.keys():

        x = A.get(key,0)

        if not isinstance(x, float):
            raise TypeError("The amount of membership for " + str(key) + "th position is not float.")
        else:
            value = 0.0
            if 0 <= x <= 0.5:
                value = 2 * (x ** 2)
            elif 0.5 < x <= 1:
                value = 1 - 2 * ((1 - x) ** 2)
            else:
                raise TypeError("The amount of membership for " + str(key) + "th position is not between [0,1] ")

            result[key] = value


    return result

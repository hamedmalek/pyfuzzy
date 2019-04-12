import numpy

def trapmf (x, params):
    
    
        if not isinstance(params, list):
            raise TypeError("Params should be a list with four values.")
        if not isinstance(x, float):
            raise TypeError("Params should be float.")
        if len(params) != 4:
            raise TypeError("Number of parameters are incorrect. Expected 4 values in the list.")
        if not ((isinstance(params[0], float) and isinstance(params[1], float))
                and isinstance(params[2], float) and isinstance(params[3], float)):
            raise TypeError("Parameters should be in float.")
        if not (params[0] <= params[1] <= params[2] <= params[3]):
            raise TypeError("Parameters should be smaller to greater.")

        a = params[0]  # locate the “feet” of the trapezoid
        b = params[1]  # locate the “shoulders” of the trapezoid
        c = params[2]  # locate the “shoulders” of the trapezoid
        d = params[3]  # locate the “feet” of the trapezoid

        if x <= a:
            return 0

        elif a <= x <= b:
            return (x - a) / (b - a)

        elif b <= x <= c:
            return 1

        elif c <= x <= d:
            return (d - x) / (d - c)

        elif x >= d:
            return 0

import numpy as np

def trimf (x, params):

    if not isinstance(params, list):
        raise TypeError ("Params should be a list with three values.")
    if len(params) != 3:
        raise TypeError ("Number of parameters are incorrect. Expected 3 values in the list.")
    if not (isinstance(params[0], float) and isinstance(params[1], float) and isinstance(params[2], float)):
        raise TypeError ("Parameters should be in float.")
    if not(params[0] <= params[1]):
        raise TypeError("First value in list should be smaller than second one.")
    if not (params[1] <= params[2]):
        raise TypeError("Second value in list should be smaller than third one.")


    a = params[0]
    b = params[1]
    c = params[2]

    result = 0.0

    if x <= a:
        result = 0.0

    elif a <= x <= b:
        result = (x-a)/(b-a)

    elif b <= x <= c:
        result = (c-x)/(c-b)

    elif c <= x:
        result = 0


    return result

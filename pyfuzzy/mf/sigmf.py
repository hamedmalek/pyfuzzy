import numpy as np


def sigmf(x, params):
    if not isinstance(params, list):
        raise TypeError("Params should be a list with two values.")
    if len(params) != 2:
        raise TypeError("Number of parameters are incorrect. Expected 2 values in the list.")
    if not (isinstance(params[0], float) and isinstance(params[1], float)):
        raise TypeError("Parameters should be in float.")

    a = params[0] # Controls width of the sigmoid region
    c = params[1] # Offset or bias. This is the center value of the sigmoid
    return 1/(1 + np.exp(-a*(x - c)))

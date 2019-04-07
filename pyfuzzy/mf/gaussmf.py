import numpy

def gaussmf (x, params):

    if not isinstance(params, list):
        raise TypeError ("Params should be a list with two values.")
    if len(params) != 2:
        raise TypeError ("Number of parameters are incorrect. Expected 2 values in the list.")
    if not (isinstance(params[0], float) and isinstance(params[1], float)):
        raise TypeError ("Parameters should be in float.")

    c = params[0]
    sigma = params[1]

    return numpy.exp(-((x-c)**2)/(2*sigma**2))

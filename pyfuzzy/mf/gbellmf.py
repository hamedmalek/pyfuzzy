def gbellmf (x, params):

    if not isinstance(params, list):
        raise TypeError ("Params should be a list with three values.")
    if len(params) != 3:
        raise TypeError ("Number of parameters are incorrect. Expected 3 values in the list.")
    if not (isinstance(params[0], float) and isinstance(params[1], float) and isinstance(params[2], float)):
        raise TypeError ("Parameters should be in float.")
    if (params[0] == 0):
        raise TypeError ("The GeneralizedBell MF needs a non-zero a.")

    a = params[0]
    b = params[1]
    c = params[2]

    tmp = ((x - c)/a)**2
    if (tmp == 0 and b == 0):
        y = 0.5
    elif  (tmp == 0 and b < 0):
        y = 0
    else:
        tmp = tmp**b
        y = 1/(1 + tmp)
    

    return y

def pimf(x, params):

    if not isinstance(params, list):
        raise TypeError("Params should be a list with four values.")
    if len(params) != 4:
        raise TypeError("Number of parameters are incorrect. Expected 4 values in the list.")
    if not ((isinstance(params[0], float) and isinstance(params[1], float))
            and isinstance(params[2], float) and isinstance(params[3], float)):
        raise TypeError("Parameters should be in float.")

    # This membership function is the product of SMF and ZMF.
    # PIMF(X, PARAMS) = SMF(X, PARAMS[:2]) * ZMF(X, PARAMS[2:])

    return smf(x, params[:2]) * zmf(x, params[2:])


def zmf(x, params):
    a = params[0]
    b = params[1]
    if a >= b:
        if x <= (a + b)/2:
            return 1
        else:
            return 0

    if x <= a:
        return 1
    elif a <= x <= (a + b)/2:
        return 1 - 2 * ((x - a)/(b - a))**2
    elif (a + b)/2 <= x <= b:
        return 2 * ((x - b)/(b - a))**2
    elif x >= b:
        return 0


def smf(x, params):
    a = params[0]
    b = params[1]

    if a >= b:
        if x >= (a + b)/2:
            return 1
        else:
            return 0

    if x <= a:
        return 0
    elif a <= x <= (a + b)/2:
        return 2 * ((x - a)/(b - a))**2
    elif (a + b)/2 <= x <= b:
        return 1 - 2 * ((x - b)/(b - a))**2
    elif x >= b:
        return 1
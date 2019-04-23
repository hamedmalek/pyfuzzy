def mf2dict(U, func_name, params):

    if not isinstance(U, list):
        raise TypeError("U should be a list of numbers.")
    if not isinstance(func_name, str):
        raise TypeError("func_name should be a string that shows name of the membership function.")
    if not isinstance(params, list):
        raise TypeError("Params should be a list of function params.")

    result = dict()

    for x in U:

        value = globals()[func_name](x, params)
        result[x] = value


    return result

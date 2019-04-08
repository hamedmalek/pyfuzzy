def pimf(x, params):

    if not isinstance(params, list):
        raise TypeError("Params should be a list with four values.")
    if len(params) != 4:
        raise TypeError("Number of parameters are incorrect. Expected 4 values in the list.")
    if not ((isinstance(params[0], float) and isinstance(params[1], float))
            and isinstance(params[2], float) and isinstance(params[3], float)):
        raise TypeError("Parameters should be in float.")

    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    if x <= a:
        return 0

    elif a <= x <= (a + b) / 2:
        return 2 * ((x - a)/(b - a)) ** 2

    elif (a + b) / 2 <= x <= b:
        return 1 - (2 * ((x - b)/(b - a)) ** 2)

    elif b <= x <= c:
        return 1

    elif c <= x <= (c + d) / 2:
        return 1 - (2 * ((x - c) / (d - c)) ** 2)

    elif (c + d) / 2 <= x <= d:
        return 2 * ((x - d) / (d - c)) ** 2

    elif x >= d:
        return 0

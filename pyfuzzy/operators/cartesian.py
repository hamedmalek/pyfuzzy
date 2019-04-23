def cartesian(U1, U2, A, B, func_name="min"):
    # checking input type for error
    if not isinstance(U1, list):
        raise TypeError("first input U1 should be a list.")
    if not isinstance(U2, list):
        raise TypeError("second input U2 should be a list.")

    if not isinstance(A, dict):
        raise TypeError("third input A should be a dictionary.")
    if not isinstance(B, dict):
        raise TypeError("fourth input B should be a dictionary.")

    if not set(A).issubset(set(U1)):
        raise TypeError("A should be a subset of U1.")
    if not set(B).issubset(set(U2)):
        raise TypeError("B should be a subset of U2.")

    if not (func_name == "product" or func_name == "min"):
        raise TypeError("func_name should be either 'min' or 'product'")


    for member in U1:
        if not isinstance(member, int):
            raise TypeError("U1 memebr at index " + str(U1.index(member)) + " should be int")

    for member in U2:
        if not isinstance(member, int):
            raise TypeError("U2 memebr at index " + str(U2.index(member)) + " should be int")

    for key in U1:
        try:
            value = float(A.get(key, 0))
            if not 0 <= value <= 1:
                raise ValueError("Value of A(" + str(key) + "): " + str(value) + " should be between [0, 1].")
        except ValueError:
            raise TypeError(A.get(key, 0) + " should be float.")

    for key in U2:
        try:
            value = float(B.get(key, 0))
            if not 0 <= value <= 1:
                raise ValueError("Value of B(" + str(key) + "): " + str(value) + " should be between [0, 1].")
        except ValueError:
            raise TypeError(B.get(key, 0) + " should be float.")

    result = dict()
    if func_name == "product":
        for memberA in U1:
            mfA = A.get(memberA, 0.)
            for memberB in U2:
                mfB = B.get(memberB, 0.)
                key = (memberA, memberB)    # tuple of members name
                result[key] = mfA*mfB
    else:
        for memberA in U1:
            mfA = A.get(memberA, 0.)
            for memberB in U2:
                mfB = B.get(memberB, 0.)
                key = (memberA, memberB)    # tuple of members name
                result[key] = min(mfA, mfB)

    return result

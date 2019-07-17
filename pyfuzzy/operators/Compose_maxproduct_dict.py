def compose_maxproduct(S, R):
    """
    Inputs
    -------
    S : Relation #1 Dictionary
        Fuzzy relation matrix #1 in dictionary data type.
        Keys must be 2-tuples of (i,j) indicating row and column indexes in the relation matrix (1-based)
        Sample: S = {(1, 1): '0.2', (1, 2): '0.7', (1, 3): '0.3', (2, 1): '0.1', (2, 2): '1', (2, 3): '0.1', (3, 2): '0.5'}
    R : Relation #1 Dictionary
        Fuzzy relation matrix #2 in dictionary data type.
        Keys must be 2-tuples of (i,j) indicating row and column indexes in the relation matrix (1-based)
        Sample: R = {(1, 1): '0.2', (1, 2): '0.7', (1, 3): '0.3', (2, 1): '0.1', (2, 2): '1', (2, 3): '0.1', (3, 2): '0.5'}


    Returns
    -------
    res : Resulting Relation Dictionary
        maxproduct composition matrix dictionary
    """

    # Checking input types
    if not isinstance(S, dict):
        raise TypeError("S should be a dictionary.")

    if not isinstance(R, dict):
        raise TypeError("R should be a dictionary.")

    # Checking input lengths
    if (len(R) == 0):
        raise ValueError("Input argument R should be non-empty.")

    if (len(S) == 0):
        raise ValueError("Input argument S should be non-empty.")

    # Checking relation keys and values
    S_max_i = 0
    S_max_j = 0
    for key in S.keys():
        try:
            i, j = key
            if (i > S_max_i):
                S_max_i = i
            if (j > S_max_j):
                S_max_j = j
            val = float(S.get(key, 0))
            if not (0 <= val <= 1):
                raise ValueError()
        except ValueError:
            raise ValueError("S(" + str(key) + "):=> '" + str(val) + "' is not between 0 and 1 ")
        except:
            raise TypeError("Input argument S is not of correct data type.")

    R_max_i = 0
    R_max_j = 0
    for key in R.keys():
        try:
            i, j = key
            if (i > R_max_i):
                R_max_i = i
            if (j > R_max_j):
                R_max_j = j
            val = float(R.get(key, 0))
            if not (0 <= val <= 1):
                raise ValueError()
        except ValueError:
            raise ValueError("R(" + str(key) + "):=> '" + str(val) + "' is not between 0 and 1 ")
        except:
            raise TypeError("Input argument R is not of correct data type.")

    # Checking relation dimensions
    if not (S_max_j == R_max_i):
        raise TypeError("Input arguments dimensions are not consistent.")

    # Computing result
    result = {}
    for i in range(S_max_i):
        for j in range(R_max_j):
            _max = 0
            for k in range(S_max_j):
                val = S.get((i+1, k+1),0)*R.get((k+1,j+1),0)
                val = round(val*100)/100
                if (val > _max):
                    _max = val
            result[(i+1, j+1)] = _max
    return result

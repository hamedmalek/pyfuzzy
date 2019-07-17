def compose_maxmin(R, S):
    """
    X = {1: 0, 2: 0.2, 3: 0.4}
    Y = {1: 0, 2: 0.2}
    Relation (X*Y) = {(1, 1): 0, (1, 2): 0, (2, 1): 0, (2, 2): 0.04, (3, 1): 0, (3, 2): 0.08}
    :param R: a dictionary like above example that
    :param S: a dictionary like above example
    :return: RoS a composition of R to S
    For example:
    R = {(1,1):0.7, (1,2):0.3, (2,1):0.8, (2,2):0.4}
    S = {(1,1):0.9, (1,2):0.6, (1,3):0.2, (2,1):0.1, (2,2):0.7, (2,3):0.5}
    RoS = {(1, 2): 0.6, (1, 3): 0.3, (2, 3): 0.4, (2, 2): 0.6, (1, 1): 0.7, (2, 1): 0.8}
    """
    if not isinstance(R, dict):
        raise TypeError("input argument should be a dictionary.")
    if not isinstance(S, dict):
        raise TypeError("input argument should be a dictionary.")

    if len(list(R.keys())) < 1:
        raise ValueError("dictionary 'R' should have at least one member.")
    if len(list(S.keys())) < 1:
        raise ValueError("dictionary 'S' should have at least one member.")

    X = []
    Yx = []
    Yz = []
    Z = []

    for key, _ in R.items():
        X.append(key[0])
        Yx.append(key[1])

    for key, _ in S.items():
        Yz.append(key[0])
        Z.append(key[1])

    # check Yx equal Yz
    if set(Yx) != set(Yz):
        raise ValueError("(X --> Y --> Z) Y's in relation R not equal with relation S")

    RoS = {}
    for x in set(X):
        for z in set(Z):
            max_membership = 0.0
            for y in set(Yx):
                min_membership = min(R[(x, y)], S[(y, z)])
                if min_membership > max_membership:
                    max_membership = min_membership
            RoS[(x, z)] = max_membership

    return RoS
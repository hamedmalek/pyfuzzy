def defuzz_lom(mf1):

#validatig data:
    if not isinstance(mf1, dict):
        raise TypeError("input argument should be a dictionery.")

    if len( list(mf1.keys()) ) < 1 :
        raise ValueError("dictionery should have at least one set.")

    for key , value in mf1.items():
        if not isinstance(key, int):
            raise TypeError("key of dictionery should be a int.")

        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("value of dictionery should be a float or int.")

        if value > 1 or value < 0:
            raise ValueError("value should be between 0 or 1.")
    
    #finding lom:
    largest_item , largest_value = sorted(mf1.items())[0]

    for item , value in sorted(mf1.items()):
        if value >= largest_value:
            largest_value = value
            largest_item = item

    return largest_item

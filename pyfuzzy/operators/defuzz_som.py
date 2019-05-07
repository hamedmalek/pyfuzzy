def defuzz_som(m):
    # validating data:
    if not isinstance(m, dict):
        raise TypeError("input argument should be a dictionary.")

    if len(list(m.keys())) < 1:
        raise ValueError("dictionary should have at least one member.")

    for key, value in m.items():
        if not isinstance(key, int):
            raise TypeError("key :" + str(key) + " in dictionary should be a integer.")

        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("value" + str(value) + " in dictionary should be a float or integer.")

        if value > 1 or value < 0:
            raise ValueError("value:" + str(value) + " should be between 0 or 1.")

    # finding som:
    min_item, max_value = sorted(m.items())[0]

    for item, value in sorted(m.items()):
        if value > max_value:
            max_value = value
            min_item = item

    return min_item



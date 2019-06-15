def defuzz(fset, type):

    # check for input type
    if not isinstance(fset, dict):
        raise TypeError("First input argument should be a dictionary.")
    # check input dictionary length
    if len(list(fset.keys())) < 1:
        raise ValueError("dictionary should have at least one member.")

    for key, value in fset.items():
        if not isinstance(key, int) and not isinstance(value, float):
            raise TypeError("key :" + str(key) + " in dictionary should be a float or integer.")

        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("value" + str(value) + " in dictionary should be a float or integer.")

        if value > 1 or value < 0:
            raise ValueError("value:" + str(value) + " should be between 0 or 1.")

    if not isinstance(type, str):
        raise TypeError("Second input argument should be a String.")

    if type.lower() == "centroid":
        # finding centroid:
        sum_moment_area = 0.0
        sum_area = 0.0
        k = list(fset.keys())
        k.sort()
        # If the membership function is a singleton fuzzy set:
        if len(fset) == 1:
            return k[0] * fset[k[0]] / fset[k[0]]
        # else return the sum of moment*area/sum of area
        for i in range(1, len(k)):
            x1 = k[i - 1]
            x2 = k[i]
            y1 = fset[k[i - 1]]
            y2 = fset[k[i]]
            # if y1 == y2 == 0.0 or x1==x2: --> rectangle of zero height or width
            if not (y1 == y2 == 0.0 or x1 == x2):
                if y1 == y2:  # rectangle
                    moment = 0.5 * (x1 + x2)
                    area = (x2 - x1) * y1
                elif y1 == 0.0 and y2 != 0.0:  # triangle, height y2
                    moment = 2.0 / 3.0 * (x2 - x1) + x1
                    area = 0.5 * (x2 - x1) * y2
                elif y2 == 0.0 and y1 != 0.0:  # triangle, height y1
                    moment = 1.0 / 3.0 * (x2 - x1) + x1
                    area = 0.5 * (x2 - x1) * y1
                else:
                    moment = (2.0 / 3.0 * (x2 - x1) * (y2 + 0.5 * y1)) / (y1 + y2) + x1
                    area = 0.5 * (x2 - x1) * (y1 + y2)
                sum_moment_area += moment * area
                sum_area += area
        return sum_moment_area / sum_area

    elif type.lower() == "mom":
        # finding mom:
        items = [k for k, v in fset.items() if v == max(fset.values())]
        return sum(items)/len(items)

    elif type.lower() == "som":
        # finding som:
        min_item, max_value = sorted(fset.items())[0]
        for item, value in sorted(fset.items()):
            if value > max_value:
                max_value = value
                min_item = item
        return min_item

    elif type.lower() == "lom":
        # finding lom:
        largest_item, largest_value = sorted(fset.items())[0]
        for item, value in sorted(fset.items()):
            if value >= largest_value:
                largest_value = value
                largest_item = item
        return largest_item

    else:
        raise ValueError("defuzzification type is unknown.")

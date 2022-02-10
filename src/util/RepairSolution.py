def repairSolutionVariableValue(value, lowerbound, upperbound):
    if value < lowerbound:
        value = lowerbound
    elif value > upperbound:
        value = upperbound

    return value

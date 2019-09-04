def div(a, b):
    if a == 0 and b == 0:
        return float('NaN')
    elif a != 0 and b == 0:
        if a >= 0:
            return float('Inf')
        else:
            return float('-Inf')
    return a/b

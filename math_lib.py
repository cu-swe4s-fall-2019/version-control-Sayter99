def div(a, b):
    if not isinstance(a, float) and not isinstance(a, int):
        return float('NaN')
    if not isinstance(b, float) and not isinstance(b, int):
        return float('NaN')
    if a == 0 and b == 0:
        return float('NaN')
    elif a != 0 and b == 0:
        if a >= 0:
            return float('Inf')
        else:
            return float('-Inf')
    return float(a)/float(b)

def add(a, b):
    if not isinstance(a, float) and not isinstance(a, int):
        return float('NaN')
    if not isinstance(b, float) and not isinstance(b, int):
        return float('NaN')
    return a + b

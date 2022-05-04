# implementing math pow function
def pow(a, b):

    negative = True if b < 0 else False
    b = abs(b)

    if b == 0:
        return 1.0
    elif b == 1:
        return float(a)
    elif b == 2:
        return float(a * a)

    if b % 2 == 0:
        result = pow(a, b // 2) * pow(a, b // 2)
    else:
        result = a * pow(a, b - 1)

    return 1.0/result if negative else (result * 1.0)


print(pow(2, 4))
print(pow(2, 5))
print(pow(2, -4))
print(pow(-2, 3))
print(pow(-2, 4))
print(pow(-3, 4))
print(pow(0, 4))
print(pow(3, 0))
print(pow(3, 3))
print(pow(0, 0))

def evenDigitsOnly(n):
    x = len(str(n))
    for i in range(x):
        if int(str(n)[i]) % 2 != 0:
            return False
    return True

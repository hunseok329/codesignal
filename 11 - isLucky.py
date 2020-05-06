def isLucky(n):
    fir = 0
    sec = 0
    long = (len(str(n)))
    a = str(n)[:long//2]
    b = str(n)[long//2:]
    for num in list(a):
        fir += int(num)
    for num in list(b):
        sec += int(num)
    if fir == sec:
        return True
    else:
        return False
def makeArrayConsecutive2(statues):
    a = sorted(statues)
    n = len(statues)
    num = 0
    for i in range(1, n):
        num += a[i]-a[i-1]
    return num - (n - 1)
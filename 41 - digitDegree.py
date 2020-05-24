def digitDegree(n):
    if n < 10:
        return 0
    count = 0
    while True:
        Sum = 0
        for num in str(n):
            Sum += int(num)
        n = Sum
        count += 1
        if n < 10:
            return count

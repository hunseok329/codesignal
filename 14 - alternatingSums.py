def alternatingSums(a):
    result = [0,0]
    for num in range(len(a)):
        if num % 2 == 0:
            result[0] += a[num]
        else:
            result[1] += a[num]

    return result

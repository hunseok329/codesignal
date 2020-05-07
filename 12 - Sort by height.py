def sortByHeight(a):
    tree = []
    tall = []
    result = []
    j = 0
    for num in range(len(a)):
        if a[num] == -1:
            tree.append(num)
        else:
            tall.append(a[num])
    tall = sorted(tall)
    for num in range(len(a)):
        if num in tree:
            result.append(-1)
        else:
            result.append(tall[j])
            j += 1
    return result
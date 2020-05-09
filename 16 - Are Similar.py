def areSimilar(a, b):
    s = 0
    for num in range(len(a)):
        if a[num] != b[num]:
            s += 1
    if s > 2:
        return False
    if sorted(a) == sorted(b):
        return True
    else:
        return False
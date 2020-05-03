def centuryFromYear(year):
    num = year%100
    result = math.trunc(year/100)
    if num == 0:
        return result
    else:
        return result+1
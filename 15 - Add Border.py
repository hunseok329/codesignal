def addBorder(picture):
    result = []
    n = len(picture[0])
    result.append("*"*(n+2))
    for word in picture:
        result.append('*'+ word + '*')
    result.append("*"*(n+2))
    return result

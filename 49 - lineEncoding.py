def lineEncoding(s):
    find = 0
    lineList = []
    result = ''
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lineList.append(s[find:i+1])
            find = i+1
    lineList.append(s[find:])
    for word in lineList:
        if len(word) == 1:
            result += word[-1]
        else:
            result += str(len(word)) + word[-1]
    return result

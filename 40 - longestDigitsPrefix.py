def longestDigitsPrefix(inputString):
    result = ''
    try:
        for word in inputString:
            result += str(int(word))
        return result
    except ValueError:
        return result

def alphabeticShift(inputString):
    result = ''
    for word in inputString:
        result += chr(ord(word)+1)
    result = result.replace("{", "a")
    return result

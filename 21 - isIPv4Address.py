def isIPv4Address(inputString):
    address = inputString.split('.')
    result = 0
    if len(address) != 4:
        return False
    for word in address:
        if word == '' or len(word) > 3: 
            return False
        if word.isdigit():
            if word == str(int(word)) and (int(word)) >= 0 and (int(word))<=255:
                result += 1
        else:
            return False
    if result == 4:
        return True
    else:
        return False
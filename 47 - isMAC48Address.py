def isMAC48Address(inputString):
    String = inputString.split('-')
    if len(String) != 6:
        return False
    for num in String:
        if len(num) != 2:
            return False
        for number in num:
            if 65 <= ord(number) < 71 or 48 <= ord(number) < 58:
                continue
            else:
                return False
    return True

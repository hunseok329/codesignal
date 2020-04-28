def checkPalindrome(inputString):
    reverseString = inputString[::-1]
    if reverseString == inputString:
        return True
    else:
        return False
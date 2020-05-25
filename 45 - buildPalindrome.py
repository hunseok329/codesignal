def buildPalindrome(st):
    for i in range(len(st)):
        result = st + st[:i][::-1]
        if result == result[::-1]:
            return result

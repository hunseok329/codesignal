import re


def reverseInParentheses(inputString):
    while "(" in inputString:
        match = re.search("\([^()]*\)", inputString)
        string = match.group(0)[1:len(match.group(0))-1]
        revers = string[::-1]
        inputString = inputString[:match.start()] + \
            revers + inputString[match.end():]
    return inputString

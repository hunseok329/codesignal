import re


def sumUpNumbers(inputString):
    number = re.findall("\d+", inputString)
    result = 0
    for num in number:
        result += int(num)
    return result

import re


def longestWord(text):
    p = re.compile('[a-zA-Z]+')
    text = p.findall(text)
    result = ''
    for word in text:
        if len(result) < len(word):
            result = word
    return result

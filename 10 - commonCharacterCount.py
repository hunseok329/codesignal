def commonCharacterCount(s1, s2):
    a = [] 
    a = sorted(list(set(s1 + s2)))
    result = 0
    for word in a:
        if s1.find(word) != -1 and s2.find(word) != -1:
            if s1.count(word) <= s2.count(word):
                result += s1.count(word)
            else:
                result += s2.count(word)
    return result
def fileNaming(names):
    result = []
    for word in names:
        if word not in result:
            result.append(word)
            continue
        if word in result:
            count = 1
            while True:
                words = word + "(" + str(count) + ")"
                if words in result:
                    count += 1
                else:
                    result.append(words)
                    break
    return result

def boxBlur(image):
    row = len(image)-2
    col = len(image[0])-2
    result = []  
    for i in range(row):
        sumList = []
        for j in range(col):
            su = 0
            for w in range(3):
                su += (image[i+w][j]+image[i+w][j+1]+image[i+w][j+2])
            sumList.append(su//9)
        result.append(sumList)
    return result
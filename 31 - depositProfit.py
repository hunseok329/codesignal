def depositProfit(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit += deposit*(rate/100)
        count += 1
    return count

def avoidObstacles(inputArray):
    last = max(inputArray)
    master = False
    jump = 1
    step = 0

    while not master:
        step += jump
        if step in inputArray:
            jump += 1
            step =0
        elif step > last:
            master = True
    return jump
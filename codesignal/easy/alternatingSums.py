def alternatingSums(a):
    # if index is divisible by 2 sum1 otherwise sum2
    sum1, sum2 = 0, 0
    for i, val in enumerate(a):
        if i % 2 == 0:
            sum1 += val
        else:
            sum2 += val

    return [sum1, sum2]



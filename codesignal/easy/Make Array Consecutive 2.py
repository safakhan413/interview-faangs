import array as arr


def makeArrayConsecutive2(statues):
    maxval, minval = max(statues), min(statues)
    ##make a list from min to max+1
    sum = 0
    for i in range(minval, maxval + 1):
        if i in statues: continue
        sum += 1
    return sum

statues = [6, 2, 3, 8]
makeArrayConsecutive2(statues)

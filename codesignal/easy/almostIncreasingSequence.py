def almostIncreasingSequence(sequence):
    print(sequence)
    # observation: if two times the value goes down or anytime more than 1 there cant be only 1 element after whose removal it becomes
    # l = list()
    s = 0
    for i in range(0, len(sequence) - 1):
        if sequence[i + 1] - sequence[i] <= 0: s += 1
    if s > 1:
        return False
    else:
        return True
    #     l.append(sequence[i+1]- sequence[i])
    # for i in l:

    print(l)




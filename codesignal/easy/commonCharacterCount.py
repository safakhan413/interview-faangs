import collections as c


def commonCharacterCount(s1, s2):
    # output: count common strings
    # input: two strings s1 s2
    # Algo:1. use dictionary to count
    # 2. get min count from both for the letters in both dics
    # 3. add those min counts
    # for l1 in s1:
    a = c.Counter(s1)
    b = c.Counter(s2)
    arrCount = list()
    for key1, v1 in a.items():
        for key2, v2 in b.items():
            if key1 == key2:
                arrCount.append(min(v1, v2))

    return sum(arrCount)
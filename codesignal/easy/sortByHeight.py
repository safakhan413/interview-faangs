from collections import deque


def sortByHeight(a):
    ##algo:
    # extract all vals of array and put in new array
    # sort new arr
    # put all vals back where its not -1

    newArr = list()
    for i in a:
        if i != -1:
            newArr.append(i)

    # nwA = sort(newArr,reverse=true)
    newArr.sort()
    print(newArr)
    l = deque(newArr)

    for i, val in enumerate(a):
        if val != -1:
            a[i] = l.popleft()

            # newArr.remove(0)
            print(i)
    print(a)
    return a



# path: Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.
def isLucky(n):
    newS = str(n)
    lenN = len(newS)
    halfLen = lenN // 2
    print(lenN // 2)
    sum1 = sum(int(n) for n in newS[:halfLen])
    print(sum1)
    sum2 = sum(int(n) for n in newS[halfLen:])
    print(f'im sum2 {sum2}')
    if sum1 == sum2:
        return True
    else:
        return False





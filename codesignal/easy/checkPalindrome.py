def checkPalindrome(inputString):
    revStr = ''
    lenstr = len(inputString)
    print('hey')
    for i in range(lenstr - 1, -1,-1):
        # print(i)
        revStr = revStr + ''.join(inputString[i])
    print(f'im rev {revStr}')
    return (revStr==inputString)

print(checkPalindrome('aabac'))
# import re

def reverseInParentheses(inputString):
    ##algo
    # create a new strin
    # 1.for all
    #     find all ()
    #     rev the string between them and join it with newString
    #     do taht for all ()
    newStr = ''
    i = 0
    while i < len(inputString):
        if inputString[i] != '(':
            newStr = newStr + ''.join(inputString[i])
        elif inputString[i] == '(':

            start = i
            end = inputString.find(')', i, len(inputString))  ## will find closing brackets after i
            revS = inputString[start + 1:end]
            newStr = newStr + revS[::-1]
            i = end + 1
            continue
        i += 1

    return newStr




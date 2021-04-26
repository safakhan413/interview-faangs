# Python3 implementation of the approach

# Function to return the modified strring
def reverseParentheses(strr):
    st = []
    lenn = len(strr)
    for i in range(lenn):

        # Push the index of the current
        # opening bracket
        if (strr[i] == '('):
            st.append(i)

        # Reverse the substarting
        # after the last encountered opening
        # bracket till the current character
        elif (strr[i] == ')'):
            print(st[-1])
            temp = strr[st[-1]:i + 1]

            strr = strr[:st[-1]] + temp[::-1] + \
                   strr[i + 1:]
            print(strr)
            del st[-1]

    # To store the modified strring
    res = ""
    for i in range(lenn):
        if (strr[i] != ')' and strr[i] != '('):
            res += (strr[i])
    return res

inputString = "foo(bar(baz))blim"
print(reverseParentheses(inputString))

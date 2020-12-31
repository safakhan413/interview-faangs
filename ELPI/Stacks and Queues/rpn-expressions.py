def evaluate(RPNS):
    intermediate_results = []
    delimiter = ','
    operators = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y, '*': lambda y, x: x * y,
        '/': lambda y, x: int(x/y)
    }
    for t in RPNS.split(delimiter):
        if t in operators:
            intermediate_results.append(operators[t](intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(t))
    return intermediate_results[-1]

str1 = "3,4,+,2,*,1,+"
print(evaluate(str1))

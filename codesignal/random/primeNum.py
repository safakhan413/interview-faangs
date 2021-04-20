def primeNumBtw(num1,num2):
    for num in range(num1,num2):
        if all(num%i != 0 for i in range(2,num)): ##if for all num btw 2 and num
            #do not have a divsior
            print(num)

primeNumBtw(100,200)
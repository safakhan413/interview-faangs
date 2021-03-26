def centuryFromYear(year):
    count = 0
    for i in range(0,year,100):
        print(i)
        count +=1
        print(count)
    return count

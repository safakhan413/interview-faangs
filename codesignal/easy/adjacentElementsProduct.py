def adjacentElementsProduct(inputArray):
    length = len(inputArray)

    sum = []

    for i in range(length - 1):
        sum.append(inputArray[i] * inputArray[i + 1])  # append all the values of the product into the array

    return max(sum)
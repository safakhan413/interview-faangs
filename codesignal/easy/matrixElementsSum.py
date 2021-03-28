# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
import numpy as np
def matrixElementsSum(matrix):
    ## output: sum of all int not below 0
    #input: a mtarix of room costs
    rows = len(matrix)
    columns = len(matrix[0])
    arrind = list()

    for i in range(rows):
        for j in range(columns):
            ##store all the zero indices i and j and indices below them in array
            if matrix[i][j] == 0:
                arrind.append((i,j))
    for ind, elem in enumerate(arrind):
        i,j = elem[0], elem[1]
        valuesBelowLen = rows - (i) ##check how many elem below
        for x in range(valuesBelowLen):
            matrix[x+i][j] = 0 ## for all elem after i assign value 0
    return np.sum(matrix)





matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
matrixElementsSum(matrix)
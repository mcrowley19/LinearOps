from .shared import isValid, order


def isSquare(matrix: list):
    if isValid(matrix) and len(matrix) == len(matrix[0]):
        return True
    return False

def add(matrix1: list,*args: list):
    for matrix in args:
        if order(matrix1) != order(matrix):
            raise Exception("Matrices cannot be added as they are of different orders")
        for row in range(len(matrix1)):
            for column in range(len(matrix1[0])):
                matrix1[row][column] += matrix[row][column]

    return matrix1

def transpose(matrix1: list):
    if not isValid(matrix1):
        raise Exception("The supplied matrix is not a valid matrix")
    result = [[0 for row in matrix1] for column in matrix1[0]]
    for rowIndex in range(len(matrix1)):
        for colIndex in range(len(matrix1[0])):
            result[colIndex][rowIndex] = matrix1[rowIndex][colIndex]
    return result

def mul(matrix1: list, matrix2: list):
    if not isValid(matrix1, matrix2):
        raise Exception("One of the matrices supplied is not a valid matrix")
    if len(matrix1[0]) != len(matrix2):
        raise Exception("The number of columns in the first matrix must equal the number of rows in the second matrix")
    
    result = [[0 for cols in matrix2[0]] for rows in matrix1]

    for rowIndex in range(len(matrix1)):
        for matrix2Col in range(len(matrix2[0])):
            for matrix1Col in range(len(matrix1[0])):
                product = matrix1[rowIndex][matrix1Col] * matrix2[matrix1Col][matrix2Col]
                result[rowIndex][matrix2Col] += product
    return result


def identity(size: int):
    if size < 1:
        raise Exception("The identity matrix must have be at least 1x1 sized")
    inverse = [[0 for col in range(size)] for row in range(size)]
    for index in range(size):
        inverse[index][index] = 1
    return inverse

def rre(matrix):
    if not isValid(matrix):
        raise Exception("The matrix supplied is not valid")
    
    # Swaps rows in the matrix so that a row with the leftmost non-zero digit will come first
    selectedRow = 0
    while selectedRow < len(matrix):
        for rowIndex in range(len(matrix)-1):
            firstSigIndex = len(matrix[0])
            secondSigIndex = len(matrix[0])
            for entry in range(len(matrix[rowIndex])):
                if matrix[rowIndex][entry] != 0 and entry < firstSigIndex:
                    firstSigIndex = entry
            for entry in range(len(matrix[rowIndex+1])):
                if matrix[rowIndex+1][entry] != 0 and entry < secondSigIndex:
                    secondSigIndex = entry
            if secondSigIndex < firstSigIndex:
                tempRow = matrix[rowIndex].copy()
                matrix[rowIndex] = matrix[rowIndex+1]
                matrix[rowIndex+1] = tempRow
        
    # Divides each element in the selected row by the leftmost non-zero number in selectedRow
        sigValueIndex = [0,0] # Value, index
        for entryIndex in range(len(matrix[selectedRow])):
            if sigValueIndex[0] == 0:
                sigValueIndex = [matrix[selectedRow][entryIndex],entryIndex]
            if sigValueIndex[0] != 0:
                matrix[selectedRow][entryIndex] = round(matrix[selectedRow][entryIndex] / sigValueIndex[0], 5)


    # Loops through rows in matrix other than the selected row. 
    # For each row, defines multiplier as the entry that shares an index with the leftmost non-zero figure in selected Row
    # Subtracts selectedRow times the multiplier

        for rowIndex in range(len(matrix)):
            if rowIndex != selectedRow:
                multiplier = matrix[rowIndex][sigValueIndex[1]]
                if multiplier != 0:
                    for entryIndex in range(len(matrix[0])):
                        matrix[rowIndex][entryIndex] = round(matrix[rowIndex][entryIndex] - (matrix[selectedRow][entryIndex] * multiplier),5)

        selectedRow += 1
    return matrix   

def inverse(matrix):
    import copy
    if not isSquare(matrix):
        raise Exception("Only square matrices have an inverse")
    dimensions = len(matrix)
    identityMatrix = identity(dimensions)

    copyMatrix = copy.deepcopy(matrix)

    for rowIndex in range(len(copyMatrix)):
        copyMatrix[rowIndex] += identityMatrix[rowIndex]

    inverse = rre(copyMatrix)
    for rowIndex in range(len(inverse)):
        inverse[rowIndex] = inverse[rowIndex][dimensions:]
    
    return inverse

def determinant(matrix):
    import copy
    if not isSquare(matrix):
        raise Exception("The determinant can only be calculated for matrices which are valid and square")
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    colNums = len(matrix[0])
    multiplicant = 1
    result = 0
    for valueIndex in range(colNums):
        minorMatrix = copy.deepcopy(matrix)
        minorMatrix = minorMatrix[1:]
        for row in minorMatrix:
            row.pop(valueIndex)
        
        result += multiplicant * matrix[0][valueIndex] * determinant(minorMatrix)
        multiplicant *= -1
    
    return result




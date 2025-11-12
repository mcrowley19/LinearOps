
def isValid(*args: list):
    for matrix in args:
        if len(matrix) < 1:
            return False
        columnCount = len(matrix[0])
        for row in matrix:
            if len(row) != columnCount:
                return False
    return True

def order(matrix: list):
    if not isValid(matrix):
        raise Exception("Entry is not a valid matrix.")
    else:
        return [len(matrix),len(matrix[0])]
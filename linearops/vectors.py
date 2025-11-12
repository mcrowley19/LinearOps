import math

from .shared import order, isValid
def dot(vector1: list, vector2: list):
    if not isValid(vector1, vector2):
        raise Exception("One of the vectors supplied is not valid")
    if len(vector1[0]) > 1:
        raise Exception("The dot product cannot be conducted on matrices with more than one column")
    if not order(vector1) == order(vector2):
        raise Exception("Both vectors must have the same number of columns")

    dotProduct = 0
    for row in range(len(vector1)):
       dotProduct += vector1[row][0] * vector2[row][0]
    
    return dotProduct

def magnitude(vector: list):
    if not isValid(vector):
        raise Exception("The vector supplied is not valid")
    if len(vector[0]) > 1:
        raise Exception("You cannot find the magnitude of matrices with more than one column")
    magnitude = math.sqrt(sum([row[0]*row[0] for row in vector]))
    return magnitude

def vecAngle(vector1,vector2, Radians = False):
    dotProduct = dot(vector1,vector2)
    radianProduct = math.acos(dotProduct / (magnitude(vector1) * magnitude(vector2)))
    if Radians:
        return radianProduct
    return math.degrees(radianProduct)


def cross(vector1: list,vector2: list):
    if not isValid(vector1, vector2):
        raise Exception("One of the vectors supplied is not valid")
    if len(vector1[0]) > 1:
        raise Exception("The cross product cannot be conducted on matrices with more than one column")
    if not order(vector1) == order(vector2):
        raise Exception("Both vectors must have the same number of columns to conduct the cross product")
    if len(vector1) != 3:
        raise Exception("The cross product can only be done on vectors with 3 dimensions") 
    
    resultX = [(vector1[1][0]*vector2[2][0]) - (vector1[2][0]*vector2[1][0])]
    resultY = [(vector1[2][0]*vector2[0][0]) - (vector1[0][0]*vector2[2][0])]
    resultZ = [(vector1[0][0]*vector2[1][0]) - (vector1[1][0]*vector2[0][0])]
    crossProduct = [resultX, resultY, resultZ]
    return crossProduct

def orthProj(vector1: list,vector2: list):
    if not isValid(vector1, vector2):
        raise Exception("One of the vectors supplied is not valid")
    if len(vector1[0]) > 1:
        raise Exception("Orthographic projection cannot be conducted on matrices with more than one column")
    vec2Magnitude = magnitude(vector2)
    scalar = dot(vector1,vector2) / (vec2Magnitude * vec2Magnitude)
    orthProjection = [[0 for column in vector1[0]]for row in vector1 ]
    for rowIndex in range(len(vector2)):
        orthProjection[rowIndex][0] = vector2[rowIndex][0] * scalar
    
    return orthProjection
        

    


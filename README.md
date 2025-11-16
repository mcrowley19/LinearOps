# LinearOps

LinearOps is a python library that offers a variety of linear algebra operations

## Usage

```python
import linearops

# Returns if a matrix or vector has the same number of columns in each row
isValid([[1,2,3],[4,5,6]])

# Vector operations
vector = [[1,2,3]]

# Returns the magnitude of a vector
linearops.magnitude(vector)

vector2 = [[4,5,6]]
# Returns the dot product of two vectors
linearops.dot(vector, vector2)

# Returns the angle between two vectors in degrees. Including Radians = True as an argument produces the output in Radians.
linearops.vecAngle(vector, vector2)
linearops.vecAngle(vector, vector2, Radians = True)

# Returns the cross product of two vectors
linearops.cross(vector, vector2)

# Returns the orthographic projection of the first vector onto the second
linearops.orthProj(vector, vector2)


# Matrix operations
matrix = [[1,2,3],[4,5,6]]

# Returns the order a matrix in the form of a list [number of rows, number of cols]
order(matrix)

# Checks if a matrix has the same number of rows as columns
isSquare(matrix)

# Returns the matrix transposed
transpose(matrix)

# Converts the matrix to reduced row echelon form and returns the result
rre(matrix)

matrix2 = [[7,8,9],[10,11,12]]
# Returns the result of the addition of two matrices
add(matrix, matrix2)

# Multiplies two matrices and returns the result
mul(matrix, matrix2)

# Returns an identity matrix with a size specified by a supplied integer
identity(5)

# Returns the inverse matrix of a matrix if it is inversable
inverse(matrix)

# Returns the determinant of the matrix as an integer value
determinant(matrix)

```

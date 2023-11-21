import numpy as np

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# c = a + b
# print("Matrix Addition ", c)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# c = a - b
# print("Matrix Subtraction", c)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5,6],[7, 8]])
# c = np.dot(a,b)
# print("DOT Product, c)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5,6],[7, 8]])
# c = a * b
# print("Element wise mul", c)


# a = np.array([[1, 2], [3, 4]])
# c = a.T
# print("Matrix Transpose of A ", c)

# a = np.array([[1, 2], [3, 4]])
# c = np.linalg.inv(a)
# print("Matrix Inverse of A ", c)

# a = np.array([[1, 2], [3, 4]])
# c = np.trace(a)
# print("Matrix Trace of A ", c)

# a = np.array([[1, 2], [3, 4]])
# c = np.linalg.det(a)
# print("Matrix Determinant of A ", c)

# a = np.array([[1, 2], [3, 4]])
# c = np.sum(a)
# print(c)



def matrix_addition(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    print(result)

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
matrix_addition(matrix1, matrix2)


def matrix_subtraction(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    print(result)


matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
matrix_subtraction(matrix1, matrix2)


def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix2)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    print(result)

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
matrix_multiplication(matrix1, matrix2)


def matrix_sum(matrix):
    row = len(matrix)
    col = len(matrix[0])
    total = 0
    for i in range(row):
        for j in range(col):
            total += matrix[i][j]
    print(total)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_sum(matrix)



def transpose(matrix):
    transpose_matrix = list(zip(*matrix))
    print(transpose_matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)




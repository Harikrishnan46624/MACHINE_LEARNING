import numpy as np

# def compute_eigenvalues(matrix):
#     eigenvalues = np.linalg.eigvals(matrix)
#     return eigenvalues

# matrix = np.array([[1, 2], [3, 4]])
# eigenvalue = compute_eigenvalues(matrix)
# print("EigenValues", eigenvalue)



def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def matrix_vector_product(matrix, vector):
    return [dot_product(row, vector) for row in matrix]

def subtract_matrices(matrix1, matrix2):
    return [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

def normalize_vector(vector):
    magnitude = (sum(x ** 2 for x in vector)) ** 0.5
    return [x / magnitude for x in vector]

def find_eigenvalues(matrix, epsilon=1e-10, max_iterations=100):
    n = len(matrix)
    eigenvalues = []

    for _ in range(n):
        vector = [1] * n

        for _ in range(max_iterations):
            new_vector = matrix_vector_product(matrix, vector)
            new_vector = normalize_vector(new_vector)

            if dot_product(new_vector, vector) < epsilon:
                break
            vector = new_vector

        eigenvalue = dot_product(new_vector, matrix_vector_product(matrix, new_vector))
        eigenvalues.append(eigenvalue)

        matrix = subtract_matrices(matrix, [[eigenvalue * v_i * v_j for v_i, v_j in zip(new_vector, new_vector)]])
    
    return eigenvalues

matrix = [[2, 1],
          [1, 3]]
eigenvalues = find_eigenvalues(matrix)
print("Eigenvalues:", eigenvalues)



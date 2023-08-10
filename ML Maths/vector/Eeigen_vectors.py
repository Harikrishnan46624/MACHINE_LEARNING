# import numpy as np

# def compute_eigenvectors(matrix):
#     eigenvalues, eigenvectors = np.linalg.eig(matrix)
#     return eigenvectors
# matrix = np.array([[5, 4], [1, 2]])
# eigenvectors = compute_eigenvectors(matrix)
# print("Eigenvectors:")
# for i in range(len(eigenvectors)):
#     print(eigenvectors[:, i])



def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def matrix_vector_product(matrix, vector):
    return [dot_product(row, vector) for row in matrix]

def subtract_matrices(matrix1, matrix2):
    return [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

def normalize_vector(vector):
    magnitude = (sum(x ** 2 for x in vector)) ** 0.5
    return [x / magnitude for x in vector]

def find_eigenvalues_eigenvectors(matrix, epsilon=1e-10, max_iterations=100):
    n = len(matrix)
    eigenvalues = []
    eigenvectors = []

    for _ in range(n):
        vector = [1] * n  # initial guess for the eigenvector

        for _ in range(max_iterations):
            new_vector = matrix_vector_product(matrix, vector)
            new_vector = normalize_vector(new_vector)

            if dot_product(new_vector, vector) < epsilon:
                break

            vector = new_vector

        eigenvalue = dot_product(new_vector, matrix_vector_product(matrix, new_vector))
        eigenvalues.append(eigenvalue)
        eigenvectors.append(new_vector)

        matrix = subtract_matrices(matrix, [[eigenvalue * v_i * v_j for v_i in new_vector] for v_j in new_vector])

    return eigenvalues, eigenvectors


matrix = [[1, 2],
          [3, 4]]

eigenvalues, eigenvectors = find_eigenvalues_eigenvectors(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
for vector in eigenvectors:
    print(vector)
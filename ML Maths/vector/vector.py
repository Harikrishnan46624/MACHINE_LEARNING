# import numpy as np

# def vector_addition(vector1, vector2):
#     result = np.add(vector1, vector2)
#     return result

# vector1 = np.array([1, 2, 3])
# vector2 = np.array([4, 5, 6])
# add = vector_addition(vector1, vector2)
# print("Vector addition",add)


# def vector_subtraction(vector1, vector2):
#     result = np.subtract(vector1, vector2)
#     return result

# vector1 = np.array([1, 2, 3])
# vector2 = np.array([4, 5, 6])
# sub = vector_subtraction(vector1, vector2)
# print("Vector Subtraction",sub)

# def vector_multiplication(vector1, vector2):
#     result = np.multiply(vector1,vector2)
#     return result

# vector1 = np.array([1, 2, 3])
# vector2 = np.array([4, 5, 6])
# mul = vector_multiplication(vector1, vector2)
# print("Vector Multiplication",mul)

# def scalar_vector_multiplication(scalar, vector):
#     result = np.multiply(scalar, vector)
#     return result

# vector = np.array([1, 2, 3])
# scalar = 2
# scalar_mul = scalar_vector_multiplication(vector, scalar)
# print("Scalar multiplication", scalar_mul)

 


# def vector_addition(vector1, vector2):
#     if len(vector1) != len(vector2):
#         raise ValueError("Must have the same length")
#     result = []
#     for i in range(len(vector1)):
#         result.append(vector1[i] + vector2[i])
#     print("Addition:", result)

# vector1 = [1, 2, 3]
# vector2 = [4, 5, 6]
# vector_addition(vector1, vector2)


# def vector_subtraction(vector1, vector2):
#     if len(vector1) != len(vector2):
#         raise ValueError("Must have same value")
#     result = []
#     for i in range(len(vector1)):
#         result.append(vector1[i] - vector2[i])
#     print("Subtraction: ", result)

# vector1 = [1, 2, 3]
# vector2 = [4, 5, 6]
# vector_subtraction(vector1, vector2)


# def scalar_multiplication(scalar, vector):
#     result = []
#     for i in range(len(vector)):
#         result.append(scalar * vector[i])
#     print("Multiplication: ", result)

# scalar = 2
# vector = [1, 2, 3]
# scalar_multiplication(scalar, vector)


def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Cross product is only defined for 3-dimensional vectors.")

    result = [vector1[1] * vector2[2] - vector1[2] * vector2[1],
              vector1[2] * vector2[0] - vector1[0] * vector2[2],
              vector1[0] * vector2[1] - vector1[1] * vector2[0]]

    print(result)

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
cross_product(vector1, vector2)



def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Dot product is only defined for vectors of the same length.")
    result = sum(a * b for a, b in zip(vector1, vector2))
    print(result)
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
dot_product(vector1, vector2)
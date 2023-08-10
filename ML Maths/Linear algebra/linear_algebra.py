# import numpy as np

# coefficents = np.array([[2, 3], [1, -2]])
# constants = np.array([15, 5])
# solution = np.linalg.solve(coefficents, constants)
# print("Solution ", solution)



def solve_linear_equations(coefficients, constants):
    n = len(coefficients)
    for i in range(n):
        # Partial Pivoting
        max_row = i
        for j in range(i + 1, n):
            if abs(coefficients[j][i]) > abs(coefficients[max_row][i]):
                max_row = j
        coefficients[i], coefficients[max_row] = coefficients[max_row], coefficients[i]
        constants[i], constants[max_row] = constants[max_row], constants[i]

        # Elimination
        for j in range(i + 1, n):
            factor = coefficients[j][i] / coefficients[i][i]
            constants[j] -= factor * constants[i]
            for k in range(i, n):
                coefficients[j][k] -= factor * coefficients[i][k]

    # Back Substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = constants[i]
        for j in range(i + 1, n):
            solution[i] -= coefficients[i][j] * solution[j]
        solution[i] /= coefficients[i][i]

    print(solution)

# Example usage
coefficients = [[2, 1, -1],
                [-3, -1, 2],
                [-2, 1, 2]]
constants = [8, -11, -3]

solve_linear_equations(coefficients, constants)



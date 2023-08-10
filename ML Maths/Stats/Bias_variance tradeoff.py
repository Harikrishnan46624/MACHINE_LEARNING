
# Bias-Variance Tradeoff without libraries - Simple Problem

import random

# Generate a synthetic dataset
def generate_dataset(n):
    X = []
    Y = []
    for _ in range(n):
        x = random.uniform(-1, 1)  # Generate random x values between -1 and 1
        y = x**2 + random.gauss(0, 0.1)  # Generate y values with a quadratic relationship and some noise
        X.append(x)
        Y.append(y)
    return X, Y

# Fit a polynomial regression model to the data
def fit_polynomial_regression(X, Y, degree):
    n = len(X)
    X_poly = [[x**i for i in range(degree+1)] for x in X]  # Create polynomial features
    XT_X = [[sum(X_poly[i][j] * X_poly[k][j] for k in range(n)) for j in range(degree+1)] for i in range(degree+1)]
    XT_Y = [sum(X_poly[j][i] * Y[j] for j in range(n)) for i in range(degree+1)]
    coefficients = [0] * (degree+1)

    # Solve the system of equations to obtain the coefficients
    for i in range(degree+1):
        for j in range(degree+1):
            if XT_X[i][j] != 0:
                coefficients[i] = XT_Y[i] / XT_X[i][j]
                break

    return coefficients

# Calculate the mean squared error (MSE) on the test set
def calculate_mse(X, Y, coefficients, degree):
    n = len(X)
    X_poly = [[x**i for i in range(degree+1)] for x in X]
    squared_errors = [(Y[i] - sum(coefficients[j] * X_poly[i][j] for j in range(degree+1)))**2 for i in range(n)]
    mse = sum(squared_errors) / n
    return mse

# Perform bias-variance tradeoff analysis
def bias_variance_tradeoff_analysis():
    n = 100  # Number of data points
    test_ratio = 0.2  # Ratio of data to be used for testing
    num_iterations = 100  # Number of iterations for the analysis
    degree = 2  # Degree of the polynomial regression model

    total_mse = 0
    for _ in range(num_iterations):
        X, Y = generate_dataset(n)
        split_index = int(test_ratio * n)
        X_train, Y_train = X[split_index:], Y[split_index:]
        X_test, Y_test = X[:split_index], Y[:split_index]
        coefficients = fit_polynomial_regression(X_train, Y_train, degree)
        mse = calculate_mse(X_test, Y_test, coefficients, degree)
        total_mse += mse

    average_mse = total_mse / num_iterations
    print("Average MSE:", average_mse)

bias_variance_tradeoff_analysis()

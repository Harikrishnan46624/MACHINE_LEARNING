
# data = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# element = data[0][1]
# print(element)

# row = data[1]
# column = [row[2] for row in data]
# print("Senond row", row)
# print("Third column", column)

# data[0][2] = 10
# print("Modified data",data)




def mean(data):
    return sum(data) / len(data)

def variance(data):
    data_mean = mean(data)
    return sum((x - data_mean) ** 2 for x in data) / len(data)

def covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Data sets must have the same length.")

    x_mean = mean(x)
    y_mean = mean(y)

    return sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))) / len(x)

def correlation_coefficient(x, y):
    cov_xy = covariance(x, y)
    var_x = variance(x)
    var_y = variance(y)

    return cov_xy / (var_x ** 0.5 * var_y ** 0.5)

def correlation_matrix(data):
    num_variables = len(data)
    matrix = [[0.0] * num_variables for _ in range(num_variables)]

    for i in range(num_variables):
        for j in range(num_variables):
            matrix[i][j] = correlation_coefficient(data[i], data[j])

    return matrix

if __name__ == "__main__":
    # Example multivariate dataset (each sublist represents a variable)
    data = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [5, 10, 15, 20, 25]
    ]

    # Calculate the mean of each variable
    means = [mean(variable) for variable in data]
    print("Means:", means)

    # Calculate the variance of each variable
    variances = [variance(variable) for variable in data]
    print("Variances:", variances)

    # Calculate the covariance matrix
    covariance_matrix = [[covariance(data[i], data[j]) for j in range(len(data))] for i in range(len(data))]
    print("Covariance Matrix:")
    for row in covariance_matrix:
        print(row)

    # Calculate the correlation matrix
    correlation_matrix_result = correlation_matrix(data)
    print("Correlation Matrix:")
    for row in correlation_matrix_result:
        print(row)

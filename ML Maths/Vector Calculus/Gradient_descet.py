def gradient_descent(x, y, learning_rate, num_iterations):
    num_samples = len(x)
    num_features = len(x[0])
    theta = [0] * num_features  # initialize theta with zeros

    for _ in range(num_iterations):
        gradient = [0] * num_features

        for i in range(num_samples):
            predicted = sum(theta[j] * x[i][j] for j in range(num_features))
            error = predicted - y[i]
            
            for j in range(num_features):
                gradient[j] += error * x[i][j]

        for j in range(num_features):
            theta[j] -= (learning_rate / num_samples) * gradient[j]

    return theta

# Example usage:
x = [[1, 3], [1, 4], [1, 5]]  # input features
y = [5, 6, 7]  # target values
learning_rate = 0.01
num_iterations = 1000

theta = gradient_descent(x, y, learning_rate, num_iterations)
print("Theta:", theta)

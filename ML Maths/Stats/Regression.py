
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Calculate the coefficients (slope and intercept) of the regression line

numerator = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))])
denominator = sum([(x[i] - mean_x) ** 2 for i in range(len(x))])
slope = numerator / denominator
intercept = mean_y - (slope * mean_x)

# Predict the values for X using the regression line
predicted_y = [slope * x + intercept for x in x]

# Print the coefficients
print("Slope Coefficent: ", slope)
print("Intercept: ", intercept)

# Print the predicted values
print("Predicted value: ", predicted_y)
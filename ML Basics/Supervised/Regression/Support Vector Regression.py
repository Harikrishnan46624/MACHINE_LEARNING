# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate some example data
np.random.seed(42)
X = np.sort(5 * np.random.rand(100, 1), axis=0)  # Random input features
y = np.sin(X).ravel() + np.random.randn(100) * 0.1  # Random target variable with some noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Support Vector Regression model
svr = SVR(kernel='rbf', C=1.0, epsilon=0.2)

# Train the model on the training data
svr.fit(X_train, y_train)

# Make predictions on the test data
y_pred = svr.predict(X_test)

# Calculate and print the mean squared error (MSE) of the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot the data and the fitted SVR curve
plt.scatter(X, y, label='Data')
plt.plot(X_test, y_pred, color='red', label='Fitted SVR')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Generate some example data
np.random.seed(42)
X = 3 * np.random.rand(100, 1)  # Random input features
y = 1 + 2 * X + np.random.randn(100, 1)  # Random target variable with some noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Ridge Regression model with alpha=1.0 (regularization strength)
ridge = make_pipeline(PolynomialFeatures(degree=2), Ridge(alpha=1.0))

# Train the model on the training data
ridge.fit(X_train, y_train)

# Make predictions on the test data
y_pred = ridge.predict(X_test)

# Calculate and print the mean squared error (MSE) of the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Sort the test data for better visualization
X_test_sorted = np.sort(X_test, axis=0)
y_pred_sorted = ridge.predict(X_test_sorted)

# Plot the data and the fitted Ridge Regression curve
plt.scatter(X, y, label='Data')
plt.plot(X_test_sorted, y_pred_sorted, color='red', label='Fitted Ridge Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

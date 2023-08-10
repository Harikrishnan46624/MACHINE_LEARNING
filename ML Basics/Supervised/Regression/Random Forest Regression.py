# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate some example data
np.random.seed(42)
X = np.sort(5 * np.random.rand(100, 1), axis=0)  # Random input features
y = np.sin(X).ravel() + np.random.randn(100) * 0.1  # Random target variable with some noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regression model with 100 trees
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
rf_reg.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_reg.predict(X_test)

# Calculate and print the mean squared error (MSE) of the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Sort the test data for better visualization
X_test_sorted = np.sort(X_test, axis=0)
y_pred_sorted = rf_reg.predict(X_test_sorted)

# Plot the data and the fitted Random Forest Regression curve
plt.scatter(X, y, label='Data')
plt.plot(X_test_sorted, y_pred_sorted, color='red', label='Fitted Random Forest')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

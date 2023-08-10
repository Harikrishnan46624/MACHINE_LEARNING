from sklearn.linear_model import LinearRegression

# Input features (house sizes in square feet)
X = [[1000], [1500], [2000], [2500], [3000]]

# Corresponding target labels (house prices in thousands of dollars)
y = [300, 450, 500, 550, 600]

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the price of a house with size 1750 square feet
predicted_price = model.predict([[1750]])

print("Predicted price:", predicted_price)

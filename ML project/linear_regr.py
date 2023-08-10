from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("house_prediction.xlsx")
print(df.columns)  # Print column names

plt.scatter(df.area, df.price, color='red', marker='+')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('House price vs. Area')
plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['Area']], df.price)

reg.predict(3300)
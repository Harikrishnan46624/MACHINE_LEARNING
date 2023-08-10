import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 5, 7, 9, 11])

# plt.scatter(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('scatter plot x and y')
# plt.show()

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x2 = sum(xi ** 2 for xi in x)
sum_y2 = sum(yi ** 2 for yi in y)

correlation = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
intercept = (sum_y - slope * sum_x) / n
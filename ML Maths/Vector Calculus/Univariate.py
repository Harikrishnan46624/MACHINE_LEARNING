import numpy as np

# data = np.array([1, 2, 3, 4, 5])

# mean = np.mean(data)
# median = np.median(data)
# variance = np.var(data)
# std_dev = np.std(data)

# print("Mean: ", mean)
# print("Median: ", median)
# print("Variance: ", variance)
# print("Standerd divation", std_dev)


data = [1, 2, 3, 4, 5]
mean = sum(data) / len(data)
middle = len(data) // 2
median = data[middle]
varience = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = varience ** 0.5
minimum = min(data)
maximum = max(data)
range_value = maximum - minimum

print("Mean: ", mean)
print("Median: ", median)
print("Variance: ", varience)
print("Standerd divation", std_dev)
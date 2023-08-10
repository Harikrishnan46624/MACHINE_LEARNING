
# Hypothesis Testing (One-sample t-test) without libraries

import random
import math

# Generate a synthetic dataset
def generate_dataset(n, mu, sigma):
    return [random.gauss(mu, sigma) for _ in range(n)]

# Calculate the sample mean
def calculate_sample_mean(data):
    return sum(data) / len(data)

# Calculate the sample standard deviation
def calculate_sample_std_dev(data, sample_mean):
    squared_diff = [(x - sample_mean) ** 2 for x in data]
    return math.sqrt(sum(squared_diff) / (len(data) - 1))

# Perform the one-sample t-test
def perform_t_test(data, null_hypothesis_mean, alpha):
    sample_mean = calculate_sample_mean(data)
    sample_std_dev = calculate_sample_std_dev(data, sample_mean)
    n = len(data)
    t_statistic = (sample_mean - null_hypothesis_mean) / (sample_std_dev / math.sqrt(n))
    critical_value = abs(t_statistic)  # We assume a two-tailed test
    p_value = (1 - alpha) * 2  # Two-tailed test, multiply by 2
    reject_null = abs(t_statistic) > critical_value

    return t_statistic, critical_value, p_value, reject_null

# Set parameters
n = 50  # Sample size
mu = 5  # Population mean
sigma = 2  # Population standard deviation
null_hypothesis_mean = 4.5  # Null hypothesis mean
alpha = 0.05  # Significance level

# Generate the dataset
data = generate_dataset(n, mu, sigma)

# Perform the t-test
t_statistic, critical_value, p_value, reject_null = perform_t_test(data, null_hypothesis_mean, alpha)

# Print the results
print("Sample Mean:", calculate_sample_mean(data))
print("Sample Standard Deviation:", calculate_sample_std_dev(data, calculate_sample_mean(data)))
print("t-Statistic:", t_statistic)
print("Critical Value:", critical_value)
print("p-Value:", p_value)
print("Reject Null Hypothesis?", reject_null)

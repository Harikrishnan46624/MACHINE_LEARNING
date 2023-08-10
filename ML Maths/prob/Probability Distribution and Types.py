
import math
# Discrete Probability Distribution: Binomial Distribution
def binomial_distribution(n, p, k):
    q = 1 - p
    coefficent = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    probability = coefficent * (p ** k) * (n - k)
    print("Binomial Probabaility: ", probability)

n = 10   # Number of trials
p = 0.5   # Probability of success
k = 5    # Number of successful outcomes
binomial_distribution(n, p, k)


# Discrete Probability Distribution: Poisson Distribution
def poisson_distribution(lmda, k):
    probability = (lmda ** k) * (math.exp(-lmda)) / math.factorial(k)
    print("Poisson probability: ", probability)
lmda = 3     # Average rate of events
k = 2       # Number of events
poisson_distribution(lmda, k)


# Continuous Probability Distribution: Normal Distribution
def normal_distribution(x ,mean, std_dev):
    coefficent = 1 / (std_dev * math.sqrt(2 * math.pi))
    exponent = ((x - mean) ** 2) / (2 * std_dev ** 2)
    prbability = coefficent * math.exp(exponent)
    print("Normal probaility: ", prbability)

x = 68
mean = 70
std_dev = 5
normal_distribution(x , mean, std_dev)

#  Continuous Probability Distribution: Exponential Distribution
def exponential_distribution(lmbda, x):
    probability = lmbda * math.exp(-lmbda * x)
    return probability

lmbda = 0.5  # Rate parameter
x = 2  # Value to calculate probability for

exponential_prob = exponential_distribution(lmbda, x)
print("Exponential probability:", exponential_prob)


# Continuous Probability Distribution: Uniform Distribution
def uniform_distribution(a, b, x):
    if x >= a and x <= b:
        probability = 1 / (b - a)
    else:
        probability = 0
    return probability

a = 0  # Lower bound of the range
b = 10  # Upper bound of the range
x = 5  # Value to calculate probability for

uniform_prob = uniform_distribution(a, b, x)
print("Uniform probability:", uniform_prob)
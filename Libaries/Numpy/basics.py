import numpy as np

a = np.array([1,2,3,4,5])

z = np.zeros(2)

o = np.ones(5)

e = np.empty(5)

ar = np.arange(4)
print(ar)

# first number, last number, and the step size.
ar2 = np.arange(2, 9, 2)
print(ar2)

# to create an array with values that are spaced linearly in a specified interval
l = np.linspace(0, 10, num=5)
print(l)

# explicitly specify which data type you want using the dtype keyword.
x = np.ones(5, dtype=np.int64)
print(x)

arr = np.array([1,2,3,4,5])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.sqrt(arr))
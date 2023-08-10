import numpy as np


# data = np.arange(6)
# print(data[1])
# print(data[1:])
# print(data[-2:])


# a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[a < 5])
# print(a[a >= 5])
# print(a[a%2 == 0])
# print(a[(a > 2) & (a < 11)])
# print((a > 5) | (a == 5))
# b = np.nonzero(a < 5)
# print(b)



# a1 = np.array([[1, 1],
#                [2, 2]])

# a2 = np.array([[3, 3],
#                [4, 4]])
# # stack them vertically
# print(np.vstack((a1, a2)))
# # stack them horizontally
# print(np.hstack((a1, a2)))



x = np.arange(1, 25).reshape(2, 12)
#  split this array into three equally shaped arrays
# print(np.hsplit(x, 3))
# split your array after the third and fourth column
# print(np.hsplit(x, (3, 4)))

# Generate a random 10x10 array with values between 0 and 99
random_array_2 = np.random.randint(0, 100, size=(10, 10))
print("\nRandom 10x10 array with values between 0 and 99:")
print(random_array_2)

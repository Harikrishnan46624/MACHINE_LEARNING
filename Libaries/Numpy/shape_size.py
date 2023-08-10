import numpy as np

arr = np.array([[[0, 1, 2, 3],
                [4, 5, 6, 7]],

                [[0, 1, 2, 3],
                [4, 5, 6, 7]],

                [[0 ,1 ,2, 3],
                [4, 5, 6, 7]]])

# To find the number of dimensions
# print(arr.ndim)
# find the shape of your array
# print(arr.shape)



# reshape your array
# a = np.arange(6)
# print(a)
# b = a.reshape(3, 2)
# print(b)


# increase the dimensions of your existing array
a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
b = a[np.newaxis, :]
print(b.shape)
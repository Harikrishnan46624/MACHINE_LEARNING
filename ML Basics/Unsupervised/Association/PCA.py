import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Sample data (replace this with your own dataset)
data = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

# Step 1: Standardize the data (optional but recommended)
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
data_std = (data - mean) / std

# Step 2: Create a PCA object and fit the data
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_std)

# Explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_

# Step 3: Get the principal components (eigenvectors)
components = pca.components_

# Step 4: Plot the transformed data along principal components
plt.figure(figsize=(8, 6))
plt.scatter(data_pca[:, 0], data_pca[:, 1], c='b', label='Transformed Data')
plt.xlabel('Principal Component 1 (Explained Variance: {:.2f}%)'.format(explained_variance_ratio[0] * 100))
plt.ylabel('Principal Component 2 (Explained Variance: {:.2f}%)'.format(explained_variance_ratio[1] * 100))
plt.legend()
plt.grid()
plt.show()

# Print the principal components
print("Principal Components:")
for i, component in enumerate(components, 1):
    print("PC{}: {}".format(i, component))

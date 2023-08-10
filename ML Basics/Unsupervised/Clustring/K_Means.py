# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate some example data
np.random.seed(42)
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# Create a KMeans model with K=4 (number of clusters)
kmeans = KMeans(n_clusters=4, random_state=42)

# Fit the model to the data and predict cluster labels
cluster_labels = kmeans.fit_predict(X)

# Get the cluster centers
cluster_centers = kmeans.cluster_centers_

# Plot the data points and cluster centers
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', edgecolors='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', s=200, c='red', label='Cluster Centers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.legend()
plt.show()

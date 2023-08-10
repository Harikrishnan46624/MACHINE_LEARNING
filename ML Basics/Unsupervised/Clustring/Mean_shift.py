# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift, estimate_bandwidth

# Generate some example data
np.random.seed(42)
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# Estimate the bandwidth (the radius for shifting points) using the data
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

# Create a MeanShift model with the estimated bandwidth
meanshift = MeanShift(bandwidth=bandwidth)

# Fit the model to the data and predict cluster labels
cluster_labels = meanshift.fit_predict(X)

# Get the cluster centers
cluster_centers = meanshift.cluster_centers_

# Plot the data points and cluster centers
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', edgecolors='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', s=200, c='red', label='Cluster Centers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Mean Shift Clustering')
plt.legend()
plt.show()

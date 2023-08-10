# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# Generate some example data
np.random.seed(42)
X, y = make_moons(n_samples=200, noise=0.05, random_state=42)

# Create a DBSCAN model with epsilon=0.3 (maximum distance between points in a cluster) and min_samples=5 (minimum number of points to form a cluster)
dbscan = DBSCAN(eps=0.3, min_samples=5)

# Fit the model to the data and predict cluster labels
cluster_labels = dbscan.fit_predict(X)

# Plot the data points and cluster assignments
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', edgecolors='k')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('DBSCAN Clustering')
plt.show()

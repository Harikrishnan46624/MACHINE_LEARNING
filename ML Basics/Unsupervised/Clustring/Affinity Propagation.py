import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data for demonstration purposes
# You can replace this with your own dataset
n_samples = 300
data, _ = make_blobs(n_samples=n_samples, centers=3, random_state=42)

# Create and fit the Affinity Propagation model
aff_prop = AffinityPropagation(damping=0.5, preference=-50)
aff_prop.fit(data)

# Get the cluster centers (exemplars) and labels for each data point
cluster_centers_indices = aff_prop.cluster_centers_indices_
labels = aff_prop.labels_

n_clusters_ = len(cluster_centers_indices)

print(f"Estimated number of clusters: {n_clusters_}")

# Plot the clusters and exemplars
plt.figure(figsize=(8, 6))
colors = plt.cm.tab20(np.linspace(0, 1, n_clusters_))

for cluster_idx, color in zip(range(n_clusters_), colors):
    cluster_center = data[cluster_centers_indices[cluster_idx]]
    cluster_points = data[labels == cluster_idx]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=color, label=f"Cluster {cluster_idx+1}")

    plt.scatter(cluster_center[0], cluster_center[1], s=200, color=color, marker='x', label=f"Exemplar {cluster_idx+1}")

plt.title("Affinity Propagation Clustering")
plt.legend()
plt.show()

import numpy as np
from sklearn.cluster import KMeans

# Sample customer data
customer_data = np.array([[25, 50000],
                          [30, 80000],
                          [35, 60000],
                          [40, 75000],
                          [45, 90000],
                          [50, 55000]])

# Create a K-means clustering model with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the customer data
kmeans.fit(customer_data)

# Get the cluster labels assigned to each customer
labels = kmeans.labels_

# Print the cluster labels
print(labels)

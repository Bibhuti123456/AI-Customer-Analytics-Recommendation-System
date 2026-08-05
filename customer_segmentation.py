import pandas
import sklearn
import matplotlib

# 1. Load Dataset
import pandas as pd
rfm = pd.read_csv(r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\customer_rfm.csv")

print(rfm.head()) # To preview 1st few Rows.
print(rfm.shape)  # To check the dimensions of a DataFrame tuple: (rows, columns).

# 2. Understand Data
"""Recency (Days since last purchase-Lower is better).
   Frequency (Number of orders-Higher is better).
   Monetary (Total spending-Higher is better)."""

# Pandas is treating the first row of data as column headers and there are no column names in the file. (Below code is to resolve that)
# Load Transformed Dataset.
import pandas as pd

rfm = pd.read_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\customer_rfm.csv",
    header=None,
    names=['CustomerID', 'Recency', 'Frequency', 'Monetary']
)

print(rfm.head()) # To preview 1st few Rows.
print(rfm.shape)  # To check the dimensions of a DataFrame tuple: (rows, columns).

# 3. Select Features (Machine Learning doesn't need CustomerID).
features = rfm[['Recency', 'Frequency', 'Monetary']]

print(features.head())

"""Why We Need Scaling

Example:

Recency = 2
Frequency = 8
Monetary = 4921

Monetary values are much larger.

AI may focus only on Monetary.

So we normalize data."""

# 4. Standardization
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_features = scaler.fit_transform(
    features
)

print(scaled_features[:5])

# 5. Elbow Method
from sklearn.cluster import KMeans

wcss = []

for i in range(1,11):

    kmeans = KMeans(
        n_clusters=i,
        random_state=42
    )

    kmeans.fit(scaled_features)

    wcss.append(
        kmeans.inertia_
    )

# 6. Plot Elbow Curve
import matplotlib.pyplot as plt

plt.plot(
    range(1,11),
    wcss,
    marker='o'
)

plt.xlabel('Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')

plt.show()

# 7. K-Means Clustering
kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

rfm['Cluster'] = kmeans.fit_predict(
    scaled_features
)

# 8. View Results
print(
    rfm[['CustomerID','Cluster']]
    .head()
)

# 9. Analyze Clusters
cluster_summary = rfm.groupby(
    'Cluster'
)[
    ['Recency',
     'Frequency',
     'Monetary']
].mean()

print(cluster_summary)

# 10. Create Business Labels
cluster_map = {
    0: 'At Risk',
    1: 'Regular',
    2: 'Loyal',
    3: 'VIP'
}

rfm['Segment'] = rfm['Cluster'].map(cluster_map)

print(
    rfm[
        ['CustomerID',
         'Cluster',
         'Segment']
    ].head(20)
)

# Check Segment Counts
segment_summary = pd.DataFrame({
    'Customers': rfm['Segment'].value_counts(),
    'Percentage': (
        rfm['Segment']
        .value_counts(normalize=True) * 100
    ).round(1).astype(str) + '%'
})

print(segment_summary)

# Save Final Output
rfm.to_csv(
    r"C:\Users\Asus\Downloads\AI_Ecommerce_Project\customer_segments.csv",
    index=False
)

print("Customer Segmentation Completed")
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Latest date in dataset
snapshot_date = df["InvoiceDate"].max()

# RFM Calculation
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Revenue": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print("Customers:", len(rfm))

# Scaling
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

print(
    rfm.groupby("Cluster")
       .agg({
           "Recency":"mean",
           "Frequency":"mean",
           "Monetary":"mean"
       })
)
print(rfm["Cluster"].value_counts())

# Save results
rfm.to_csv("customer_segments.csv")

print("\nSegmentation Completed!")
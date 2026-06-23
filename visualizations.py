import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# -----------------------------
# 1. Top 10 Products by Revenue
# -----------------------------
top_products = (
    df.groupby("Description")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# -----------------------------
# 2. Top 10 Countries by Revenue
# -----------------------------
top_countries = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))
top_countries.plot(kind="bar")
plt.title("Top 10 Countries by Revenue")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

# -----------------------------
# 3. Customer Segment Distribution
# -----------------------------
segments = pd.read_csv("customer_segments.csv")

segment_counts = segments["Cluster"].value_counts()

plt.figure(figsize=(6,6))
segment_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Customer Segments")
plt.ylabel("")
plt.tight_layout()
plt.savefig("customer_segments.png")
plt.close()

print("Visualizations Created Successfully!")
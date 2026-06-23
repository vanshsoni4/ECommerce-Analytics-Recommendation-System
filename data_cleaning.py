import pandas as pd

df = pd.read_csv(
    r"C:\Users\vansh\Downloads\archive\data.csv",
    encoding="latin1"
)

print("Rows:", len(df))
print("Null Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing customer id
df = df.dropna(subset=["CustomerID"])

# Create revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nCleaned Rows:", len(df))

df.to_csv("cleaned_data.csv", index=False)

print("Cleaning Completed!")
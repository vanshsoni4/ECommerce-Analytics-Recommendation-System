import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="projectuser",
    password="project123",
    database="ecommerce_project"
)

cursor = conn.cursor()

csv_file = r"C:\Users\vansh\Downloads\archive\data.csv"

query = """
INSERT INTO orders (
    invoice_no,
    stock_code,
    description,
    quantity,
    invoice_date,
    unit_price,
    customer_id,
    country
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

total_rows = 0

print("Reading CSV...")

for chunk in pd.read_csv(
    csv_file,
    chunksize=5000,
    encoding="latin1"
):

    chunk = chunk.fillna("")

    data = []

    for _, row in chunk.iterrows():

        customer_id = None if row["CustomerID"] == "" else str(row["CustomerID"])

        data.append((
            str(row["InvoiceNo"]),
            str(row["StockCode"]),
            str(row["Description"]),
            int(row["Quantity"]),
            str(row["InvoiceDate"]),
            float(row["UnitPrice"]),
            customer_id,
            str(row["Country"])
        ))

    cursor.executemany(query, data)
    conn.commit()

    total_rows += len(data)
    print(f"{total_rows} rows imported")

cursor.close()
conn.close()

print("Import Completed Successfully!")
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="projectuser",
        password="project123",
        database="ecommerce_project"
    )

    print("Connected Successfully!")
    conn.close()

except Exception as e:
    print("Error:", e)
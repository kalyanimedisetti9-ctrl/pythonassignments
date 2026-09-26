import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS college_db")

print("Database created successfully")

con.close()
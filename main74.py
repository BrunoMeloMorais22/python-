import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "passport",
    database = "empresa"
)

cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name FROM funcionario")

resultado = cursor.fetchall()
for x in resultado:
    print(x)
cursor.close()
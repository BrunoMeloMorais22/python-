import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'mercado',
    password = 'passport'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM funcionario")

resultado = cursor.fetchall()
for x in resultado:
    print(x)

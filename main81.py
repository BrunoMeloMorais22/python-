import mysql.connector


conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'passport',
    database = 'mercado'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM fornecedor")

resultado = cursor.fetchall()
for x in resultado:
    print(x)

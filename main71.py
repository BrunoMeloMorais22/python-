
import mysql.connector

config = mysql.connector.connect( 
    host = "localhost",
    user = "root",
    password = "passport",
    database = "mercado"
)

cursor = config.cursor()

cursor.execute("SELECT * FROM funcionario")

resultado = cursor.fetchall()
for x in resultado:
    print(x)

cursor.close()
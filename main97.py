


import mysql.connector
from mysql.connector import errorcode


config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "passport",
    "database" : "mercado"
}

def conectar():
    try:
        conn = mysql.connector.connect(**config)
        print("Conexão com o banco de dados estabelecida")
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acesso negado - Usuário ou senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados inexistente")
        else:
            print(err)
        return None

def consulta(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionario")
    exibir = cursor.fetchall()
    for x in exibir:
        print(x)
    cursor.close()

conn = conectar()

if conn:
    consulta(conn)
    conn.close()
    print("Conexão com o banco de dados fechada")
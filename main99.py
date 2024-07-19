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
            print("Erro de acesso - Usuário ou Senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)
        return None
conectar()

        

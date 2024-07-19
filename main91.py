import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'passport',
    database = 'sakila'
)

def conectar():
    try:
        conn = mysql.connector.connect(**conn)
        print("Conexão estabelecida")
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário ou senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)
        return None

def consulta(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM actor")
    show = cursor.fetchall()
    for x in show:
        print(x)
    cursor.close()

def inserir_funcionario(conn, actor_id, first_name, last_name):
    cursor = conn.cursor()
    query = 'INSERT INTO actor (actor_id, first_name, last_name) VALUES (%s, %s, %s)'
    value = (actor_id, first_name, last_name)
    try:
        cursor.execute(query, value)
        conn.commit()
        print("Novo usuário adicionado")
    except mysql.connector.Error as err:
        print("Falha ao inserir novo usuário: ", err)
    cursor.close()

conn == conectar

if conn is not None:
    inserir_funcionario(conn, 600, 'Bruno', 'Melo')
    conn.close()

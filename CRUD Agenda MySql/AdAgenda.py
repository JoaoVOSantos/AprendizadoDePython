import mysql.connector

def adicionar_usuario(nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    sql = "INSERT INTO pessoas (nome, email, fone) VALUES (%s, %s, %s)"
    val = (nome, email, fone)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
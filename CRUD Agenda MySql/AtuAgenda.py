import mysql.connector

def atualizar_usuario(id, nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    
    sql = "UPDATE pessoas SET nome = %s, email = %s, fone = %s WHERE id = %s"
    val = (nome, email, fone, id)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
import mysql.connector

def deletar_usuario(id):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    
    sql = "DELETE FROM pessoas WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
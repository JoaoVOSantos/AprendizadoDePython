import mysql.connector

def listar_usuario():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    sql = "SELECT * from pessoas"
    cursor.execute(sql)
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)
    conexao.commit()
    conexao.close()
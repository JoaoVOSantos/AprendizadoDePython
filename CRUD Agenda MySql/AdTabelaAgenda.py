import mysql.connector

def criar_tabela():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()
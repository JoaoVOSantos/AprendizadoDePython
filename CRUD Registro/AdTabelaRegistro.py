import sqlite3
#Função para criar a tabela
def criar_tabela():
    conexao = sqlite3.connect('example.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY NULL,
                    none TEXT NOT NULL,
                    idade INTEGER )''')
    conexao.commit()
    conexao.close()
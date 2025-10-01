import sqlite3

def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('example.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (?, ?)''', (nome, idade))
    conexao.commit()
    conexao.close()
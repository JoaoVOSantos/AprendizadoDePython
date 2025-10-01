import sqlite3
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('example.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, idade = ?, WHERE id = ? ''', (nome, idade, id))
    conexao.commit()
    conexao.close()
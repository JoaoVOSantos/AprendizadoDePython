import sqlite3

def deletar_usuario(id):
    conexao = sqlite3.connect('example.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()
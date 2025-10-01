import sqlite3

def deletar_musica(id):
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM Musicas WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()
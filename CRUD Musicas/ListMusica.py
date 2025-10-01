import sqlite3

def listar_musicas():
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM Musicas''')
    musicas = cursor.fetchall()
    for musica in musicas:
        print(musica)
    conexao.close()
import sqlite3

def adicionar_musica(titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo):
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO Musicas (titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo))
    conexao.commit()
    conexao.close()
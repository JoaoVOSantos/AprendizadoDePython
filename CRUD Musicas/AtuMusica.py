import sqlite3

def atualizar_musica(id, titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo):
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE Musicas SET titulo = ?, artista = ?, palavras_chaves = ?, album = ?, genero = ?, ano = ?, duracao_segundos = ?, compositor = ?, gravadora = ?, caminho_arquivo = ? WHERE id = ? ''', (titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo, id))
    conexao.commit()
    conexao.close()
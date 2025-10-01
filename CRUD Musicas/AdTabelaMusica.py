import sqlite3
#Função para criar a tabela
def criar_tabela():
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Musicas (
                    id INTEGER PRIMARY KEY NOT NULL,
                    titulo TEXT NOT NULL,
                    artista TEXT NOT NULL,
                    palavras_chaves TEXT,
                    album TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    duracao_segundos INTEGER NOT NULL,
                    compositor TEXT NOT NULL,
                    gravadora TEXT NOT NULL,
                    caminho_arquivo TEXT NOT NULL )''')
    conexao.commit()
    conexao.close()
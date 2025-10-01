import sqlite3

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
    
def adicionar_musica(titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo):
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO Musicas (titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo))
    conexao.commit()
    conexao.close()
    
def deletar_musica(id):
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM Musicas WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()
    
def listar_musicas():
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM Musicas''')
    musicas = cursor.fetchall()
    for musica in musicas:
        print(musica)
    conexao.close()
    
def atualizar_musica(id, titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo):
    conexao = sqlite3.connect('Repertorio.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE Musicas SET titulo = ?, artista = ?, palavras_chaves = ?, album = ?, genero = ?, ano = ?, duracao_segundos = ?, compositor = ?, gravadora = ?, caminho_arquivo = ? WHERE id = ? ''', (titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo, id))
    conexao.commit()
    conexao.close()
    
    
def menu():
    print("\n1. Adicionar Musica")
    print("\n2. Listar Musica")
    print("\n3. Atualizar Musica")
    print("\n4. Deletar Musica")
    print("\n5. Sair")
    
criar_tabela()

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha ==  '1':
        titulo = input("Digite o titulo da musica: ")
        artista = input("Digite o artista da musica: ")
        palavras_chaves = input("Digite as palavras chaves da musica: ")
        album = input("Digite nome do album da musica: ")
        genero = input("Digite o genero da musica: ")
        ano = int(input("Digite o ano da musica: "))
        duracao_segundos = int(input("Digite duração em segundos da musica: "))
        compositor = input("Digite o compositor da musica: ")
        gravadora = input("Digite a gravadora da musica: ")
        caminho_arquivo = input("Digite o caminho do arquivo da musica: ")
        
        adicionar_musica(titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo)
        print("Musica cadastrada com sucesso")
    elif escolha == '2':
        print("\n Todos os usuarios")
        listar_musicas()
    elif escolha == '3':
        id = int(input("Digite o ID da musica a ser atualizada: "))
        titulo = input("Digite o titulo da musica: ")
        artista = input("Digite o artista da musica: ")
        palavras_chaves = input("Digite as palavras chaves da musica: ")
        album = input("Digite nome do album da musica: ")
        genero = input("Digite o genero da musica: ")
        ano = int(input("Digite o ano da musica: "))
        duracao_segundos = int(input("Digite duração em segundos da musica: "))
        compositor = input("Digite o compositor da musica: ")
        gravadora = input("Digite a gravadora da musica: ")
        caminho_arquivo = input("Digite o caminho do arquivo da musica: ")
        atualizar_musica(id, titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo)
        print("Musica atualizado com sucesso")
    elif escolha == '4':
        id = int(input("Digite o ID da musica a ser deletada: "))
        deletar_musica(id)
        print("Musica deletada com sucesso")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção invalida. Por favor, escolha uma opção valida.")
        


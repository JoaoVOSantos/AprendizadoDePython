import sqlite3

def listar_usuarios_idade(idade):
    conexao = sqlite3.connect('example.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios WHERE idade <= ? ''',(idade,))
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()
    
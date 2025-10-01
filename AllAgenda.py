import mysql.connector

# Função para criar a tabela
def criar_tabela():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

def adicionar_usuario(nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    sql = "INSERT INTO pessoas (nome, email, fone) VALUES (%s, %s, %s)"
    val = (nome, email, fone)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
    
def listar_usuario():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    sql = "SELECT * from pessoas"
    cursor.execute(sql)
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)
    conexao.commit()
    conexao.close()
    
def atualizar_usuario(id, nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    
    sql = "UPDATE pessoas SET nome = %s, email = %s, fone = %s WHERE id = %s"
    val = (nome, email, fone, id)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
    
def deletar_usuario(id):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="agenda")
    cursor = conexao.cursor()
    
    sql = "DELETE FROM pessoas WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()


def menu():
    print("\n1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        fone = input("Digite o fone do usuário: ")
        adicionar_usuario(nome, email, fone)
        print("Usuário adicionado com sucesso!")


    elif escolha == '2':
        print("\n Todos os usuarios")
        listar_usuario()
        
    elif escolha == '3':
        id = int(input("Digite o ID do usuario a ser atualizade: "))
        nome = input("Digite o novo nome de usuario: ")
        email = input("Digite o novo email do usuario: ")
        telefone = input("Digite o novo telefone do usuario: ")
        atualizar_usuario(id, nome, email, telefone)
        print("Usuario atualizado com sucesso")
        
    elif escolha == '4':
        id = int(input("Digite o ID do usuario a ser deletado: "))
        deletar_usuario(id)
        print("Usuario deletado com sucesso")
    
    elif escolha == '5':
        print("Saindo do programa...")
        break
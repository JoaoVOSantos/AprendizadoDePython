import sqlite3
import random
import matplotlib.pyplot as plt

def criar_e_popular_banco():
    """
    Cria um banco de dados SQLite, uma tabela de produtos e a popula com dados de exemplo.
    """
    # Conecta ao banco de dados (cria o arquivo se nÃ£o existir)
    conn = sqlite3.connect('dados_vendas.db')
    cursor = conn.cursor()

    # Cria a tabela 'vendas' se ela nÃ£o existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')

    # Limpa dados antigos para garantir que o exemplo seja consistente a cada execuÃ§Ã£o
    cursor.execute('DELETE FROM vendas')

    # Lista de produtos de exemplo
    produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam']
    
    # Insere dados aleatÃ³rios na tabela
    for produto in produtos:
        quantidade_vendida = random.randint(20, 150)
        cursor.execute("INSERT INTO vendas (produto, quantidade) VALUES (?, ?)", 
                       (produto, quantidade_vendida))

    # Salva as alteraÃ§Ãµes (commit) e fecha a conexÃ£o
    conn.commit()
    conn.close()
    print("Banco de dados 'dados_vendas.db' criado e populado com sucesso!")

def ler_dados_do_banco():
    """
    LÃª os dados da tabela 'vendas' do banco de dados SQLite.
    """
    conn = sqlite3.connect('dados_vendas.db')
    cursor = conn.cursor()

    # Seleciona os produtos e suas respectivas quantidades
    cursor.execute("SELECT produto, quantidade FROM vendas ORDER BY quantidade DESC")
    dados = cursor.fetchall()  # Retorna uma lista de tuplas, ex: [('Notebook', 120), ...]

    conn.close()
    return dados

def gerar_grafico_colunas(dados):
    """
    Gera e exibe um grÃ¡fico de colunas a partir dos dados fornecidos.
    """
    if not dados:
        print("NÃ£o hÃ¡ dados para gerar o grÃ¡fico.")
        return

    # Separa os dados em duas listas: uma para os nomes dos produtos e outra para as quantidades
    produtos = [item[0] for item in dados]
    quantidades = [item[1] for item in dados]

    # Cria o grÃ¡fico de colunas
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura do grÃ¡fico
    plt.bar(produtos, quantidades, color='skyblue')

    # Adiciona tÃ­tulos e rÃ³tulos para maior clareza
    plt.title('Quantidade de Vendas por Produto')
    plt.xlabel('Produtos')
    plt.ylabel('Quantidade Vendida')
    
    # Melhora a visualizaÃ§Ã£o dos rÃ³tulos do eixo x, se forem muitos
    plt.xticks(rotation=45, ha="right")
    
    # Garante que tudo se encaixe bem na figura
    plt.tight_layout()

    # Exibe o grÃ¡fico
    plt.show()

# --- FunÃ§Ã£o Principal para Executar o Programa ---
def main():
    """
    Orquestra a execuÃ§Ã£o das funÃ§Ãµes do programa.
    """
    criar_e_popular_banco()
    dados_do_banco = ler_dados_do_banco()
    gerar_grafico_colunas(dados_do_banco)

if __name__ == '__main__':
    main()
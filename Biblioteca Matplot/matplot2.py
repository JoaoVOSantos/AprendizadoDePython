import mysql.connector
from mysql.connector import Error
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'python_graficos'
}

def conectar_banco():
    """Tenta conectar ao banco de dados MySQL."""
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("ConexÃ£o com o MySQL bem-sucedida!")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def popular_banco_dados(conn):
    """Cria a tabela de usuÃ¡rios e a popula com dados fictÃ­cios de cadastro."""
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            data_cadastro TIMESTAMP NOT NULL
        )
    """)

    # Limpa a tabela para garantir que os dados sejam novos a cada execuÃ§Ã£o
    cursor.execute("TRUNCATE TABLE usuarios")
    print("Tabela 'usuarios' limpa.")

    # Gera 100 usuÃ¡rios fictÃ­cios com datas de cadastro nos Ãºltimos 30 dias
    nomes = [f"UsuÃ¡rio {i+1}" for i in range(100)]
    data_hoje = datetime.now()

    for nome in nomes:
        # Gera uma data de cadastro aleatÃ³ria nos Ãºltimos 30 dias
        dias_atras = random.randint(0, 30)
        data_cadastro = data_hoje - timedelta(days=dias_atras)
        
        # O placeholder para o mysql-connector Ã© %s
        query = "INSERT INTO usuarios (nome, data_cadastro) VALUES (%s, %s)"
        cursor.execute(query, (nome, data_cadastro))

    conn.commit()
    cursor.close()
    print("Banco de dados populado com 100 usuÃ¡rios fictÃ­cios.")

def ler_e_agregar_dados(conn):
    """LÃª os dados e os agrupa por dia, contando o nÃºmero de cadastros."""
    cursor = conn.cursor()

    query = """
        SELECT DATE(data_cadastro) AS dia, COUNT(id) AS total_cadastros
        FROM usuarios
        GROUP BY DATE(data_cadastro)
        ORDER BY dia;
    """
    
    cursor.execute(query)
    dados = cursor.fetchall()
    cursor.close()
    return dados

def gerar_grafico(dados):
    """Gera um grÃ¡fico de colunas com os dados de cadastros diÃ¡rios."""
    if not dados:
        print("NÃ£o foram encontrados dados para gerar o grÃ¡fico.")
        return

    # Separa as datas e as contagens em listas separadas
    datas = [item[0] for item in dados]
    contagens = [item[1] for item in dados]

    # Cria o grÃ¡fico
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(datas, contagens, color='teal', width=0.6)

    # FormataÃ§Ã£o do eixo X para exibir as datas de forma legÃ­vel
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # Marca um dia a cada 3 dias
    fig.autofmt_xdate() # Rotaciona e alinha as datas para nÃ£o sobrepor

    # TÃ­tulos e rÃ³tulos
    plt.title('NÃºmero de Cadastros de UsuÃ¡rios por Dia')
    plt.xlabel('Data do Cadastro')
    plt.ylabel('NÃºmero de UsuÃ¡rios')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Exibe o grÃ¡fico
    plt.show()


# --- FunÃ§Ã£o Principal ---
def main():
    conn = conectar_banco()
    if conn:
        popular_banco_dados(conn)
        dados_agregados = ler_e_agregar_dados(conn)
        conn.close() # Fecha a conexÃ£o apÃ³s o uso
        print("ConexÃ£o com o MySQL fechada.")
        
        gerar_grafico(dados_agregados)

if __name__ == "__main__":
    main()
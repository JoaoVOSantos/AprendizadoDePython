import mysql.connector
from mysql.connector import Error
import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# ------------------ CONFIGURAÇÃO DO BANCO ------------------
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'desempenho_escolar'
}

# ------------------ FUNÇÕES DE BANCO ------------------
def conectar_banco():
    """Conecta ao banco de dados MySQL."""
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexão com o MySQL bem-sucedida!")
            return conn
    except Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao MySQL: {e}")
        return None


def popular_banco_dados(conn):
    """Cria e popula a tabela NOTAS_ALUNOS com dados aleatórios."""
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas_alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            aluno VARCHAR(255) NOT NULL,
            bimestre INT NOT NULL,
            disciplina VARCHAR(255) NOT NULL,
            nota DOUBLE NOT NULL
        )
    """)

    cursor.execute("TRUNCATE TABLE notas_alunos")
    alunos = [f"Aluno {i+1}" for i in range(100)]
    disciplinas = ['Matemática', 'Português', 'História', 'Ciências', 'Biologia', 'Ética']

    for aluno in alunos:
        for bimestre in range(1, 5):
            for disciplina in disciplinas:
                nota = round(random.uniform(0, 10), 2)
                query = "INSERT INTO notas_alunos (aluno, disciplina, bimestre, nota) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (aluno, disciplina, bimestre, nota))

    conn.commit()
    cursor.close()
    messagebox.showinfo("Sucesso", "Banco de dados populado com sucesso!")


# ------------------ FUNÇÕES DE CONSULTA ------------------
def notas_por_disciplina(conn, aluno):
    cursor = conn.cursor()
    query = """
        SELECT disciplina, AVG(nota) 
        FROM notas_alunos
        WHERE aluno = %s
        GROUP BY disciplina
        ORDER BY disciplina;
    """
    cursor.execute(query, (aluno,))
    dados = cursor.fetchall()
    cursor.close()
    return dados


def media_por_bimestre(conn):
    cursor = conn.cursor()
    query = """
        SELECT bimestre, ROUND(AVG(nota), 2) AS media_bimestre
        FROM notas_alunos
        GROUP BY bimestre
        ORDER BY bimestre;
    """
    cursor.execute(query)
    dados = cursor.fetchall()
    cursor.close()
    return dados


def comparacao_entre_alunos(conn):
    cursor = conn.cursor()
    query = """
        SELECT aluno, ROUND(AVG(nota), 2) AS media_geral
        FROM notas_alunos
        GROUP BY aluno
        ORDER BY media_geral DESC;
    """
    cursor.execute(query)
    dados = cursor.fetchall()
    cursor.close()
    return dados


def evolucao_aluno(conn, nome_aluno):
    cursor = conn.cursor()
    query = """
        SELECT bimestre, ROUND(AVG(nota), 2) AS media_bimestre
        FROM notas_alunos
        WHERE aluno = %s
        GROUP BY bimestre
        ORDER BY bimestre;
    """
    cursor.execute(query, (nome_aluno,))
    dados = cursor.fetchall()
    cursor.close()
    return dados


# ------------------ GRÁFICOS ------------------
def grafico_notas_por_disciplina(conn):
    nome = simpledialog.askstring("Aluno", "Digite o nome do aluno (ex: Aluno 1):")
    if not nome:
        return
    dados = notas_por_disciplina(conn, nome)
    if not dados:
        messagebox.showinfo("Aviso", "Aluno não encontrado.")
        return

    disciplinas = [d[0] for d in dados]
    medias = [d[1] for d in dados]
    plt.figure(figsize=(8, 6))
    plt.bar(disciplinas, medias, color='royalblue')
    plt.title(f"Média de Notas por Disciplina - {nome}")
    plt.xlabel("Disciplina")
    plt.ylabel("Média")
    plt.ylim(0, 10)
    plt.show()


def grafico_media_bimestre(conn):
    dados = media_por_bimestre(conn)
    bimestres = [str(d[0]) for d in dados]
    medias = [d[1] for d in dados]
    plt.figure(figsize=(8, 6))
    plt.bar(bimestres, medias, color='teal')
    plt.title("Média Geral das Notas por Bimestre")
    plt.xlabel("Bimestre")
    plt.ylabel("Média das Notas")
    plt.ylim(0, 10)
    plt.show()


def grafico_comparacao_alunos(conn):
    dados = comparacao_entre_alunos(conn)
    top_alunos = dados[:10]  # mostra só os 10 melhores
    nomes = [d[0] for d in top_alunos]
    medias = [d[1] for d in top_alunos]
    plt.figure(figsize=(10, 6))
    plt.barh(nomes, medias, color='orange')
    plt.title("Top 10 Alunos - Desempenho Geral")
    plt.xlabel("Média")
    plt.xlim(0, 10)
    plt.gca().invert_yaxis()
    plt.show()


def grafico_evolucao_aluno(conn):
    nome = simpledialog.askstring("Aluno", "Digite o nome do aluno (ex: Aluno 1):")
    if not nome:
        return
    dados = evolucao_aluno(conn, nome)
    if not dados:
        messagebox.showinfo("Aviso", "Aluno não encontrado.")
        return

    bimestres = [str(d[0]) for d in dados]
    medias = [d[1] for d in dados]
    plt.figure(figsize=(8, 6))
    plt.plot(bimestres, medias, marker='o', color='purple')
    plt.title(f"Evolução das Notas - {nome}")
    plt.xlabel("Bimestre")
    plt.ylabel("Média")
    plt.ylim(0, 10)
    plt.grid(True)
    plt.show()


# ------------------ INTERFACE TKINTER ------------------
def main():
    conn = conectar_banco()
    if not conn:
        return

    janela = tk.Tk()
    janela.title("Análise de Desempenho Escolar")
    janela.geometry("500x400")
    janela.configure(bg="#f0f0f0")

    titulo = tk.Label(janela, text="📊 Sistema de Análise Escolar", font=("Arial", 16, "bold"), bg="#f0f0f0")
    titulo.pack(pady=20)

    ttk.Button(janela, text="Popular Banco de Dados", command=lambda: popular_banco_dados(conn)).pack(pady=10)
    ttk.Button(janela, text="Notas por Disciplina (Aluno)", command=lambda: grafico_notas_por_disciplina(conn)).pack(pady=5)
    ttk.Button(janela, text="Média de Notas por Bimestre", command=lambda: grafico_media_bimestre(conn)).pack(pady=5)
    ttk.Button(janela, text="Comparação de Desempenho entre Alunos", command=lambda: grafico_comparacao_alunos(conn)).pack(pady=5)
    ttk.Button(janela, text="Evolução de um Aluno", command=lambda: grafico_evolucao_aluno(conn)).pack(pady=5)

    ttk.Button(janela, text="Sair", command=lambda: (conn.close(), janela.destroy())).pack(pady=20)

    janela.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

def connectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
    )

# Criação da tabela
def criar_tabela():
    conexao = connectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS musica (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255),
            artista VARCHAR(255),
            palavras_chave TEXT,
            album VARCHAR(255),
            genero VARCHAR(100),
            ano INT,
            duracao_segundos INT,
            compositor VARCHAR(255),
            gravadora VARCHAR(255),
            caminho_arquivo TEXT
        )
    ''')
    conexao.commit()
    conexao.close()

# Inserir música
def inserir_musica_bd(titulo, artista, palavras, album, genero, ano, duracao, compositor, gravadora, caminho):
    conexao = connectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO musica (titulo, artista, palavras_chave, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (titulo, artista, palavras, album, genero, int(ano), int(duracao), compositor, gravadora, caminho))
    conexao.commit()
    conexao.close()

# Buscar todas
def buscar_musicas():
    conexao = connectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM musica')
    musicas = cursor.fetchall()
    conexao.close()
    return musicas

# Deletar música
def deletar_musica_bd(id_musica):
    conexao = connectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM musica WHERE id = %s', (id_musica,))
    conexao.commit()
    conexao.close()

# Atualizar música
def atualizar_musica_bd(id_musica, titulo, artista, palavras, album, genero, ano, duracao, compositor, gravadora, caminho):
    conexao = connectar()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE musica
        SET titulo = %s, artista = %s, palavras_chave = %s, album = %s, genero = %s, ano = %s,
            duracao_segundos = %s, compositor = %s, gravadora = %s, caminho_arquivo = %s
        WHERE id = %s
    ''', (titulo, artista, palavras, album, genero, int(ano), int(duracao), compositor, gravadora, caminho, id_musica))
    conexao.commit()
    conexao.close()

# Tela para adicionar nova música
def abrir_janela_adicionar():
    def salvar_musica():
        try:
            inserir_musica_bd(
                campo_titulo.get(),
                campo_artista.get(),
                campo_palavras.get(),
                campo_album.get(),
                campo_genero.get(),
                campo_ano.get(),
                campo_duracao.get(),
                campo_compositor.get(),
                campo_gravadora.get(),
                campo_caminho.get()
            )
            messagebox.showinfo("Sucesso", "Música adicionada com sucesso!")
            janela.destroy()
            atualizar_tabela()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    janela = tk.Toplevel(janela_principal)
    janela.title("Nova Música")

    labels = ["Título", "Artista", "Palavras-chave", "Álbum", "Gênero", "Ano", "Duração (seg)", "Compositor", "Gravadora", "Caminho"]
    entradas = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, sticky="w")

    campo_titulo = tk.Entry(janela)
    campo_artista = tk.Entry(janela)
    campo_palavras = tk.Entry(janela)
    campo_album = tk.Entry(janela)
    campo_genero = tk.Entry(janela)
    campo_ano = tk.Entry(janela)
    campo_duracao = tk.Entry(janela)
    campo_compositor = tk.Entry(janela)
    campo_gravadora = tk.Entry(janela)
    campo_caminho = tk.Entry(janela)

    entradas = [campo_titulo, campo_artista, campo_palavras, campo_album, campo_genero,
                campo_ano, campo_duracao, campo_compositor, campo_gravadora, campo_caminho]

    for i, entrada in enumerate(entradas):
        entrada.grid(row=i, column=1)

    tk.Button(janela, text="Salvar", command=salvar_musica).grid(row=len(labels), columnspan=2, pady=10)

# Atualizar tabela principal
def atualizar_tabela():
    for item in tabela_musicas.get_children():
        tabela_musicas.delete(item)
    for musica in buscar_musicas():
        tabela_musicas.insert("", "end", values=musica)

# Deletar
def deletar_musica_tabela():
    selecionado = tabela_musicas.selection()
    if selecionado:
        id_musica = tabela_musicas.item(selecionado[0])['values'][0]
        deletar_musica_bd(id_musica)
        atualizar_tabela()
        messagebox.showinfo("Removido", "Música deletada.")
    else:
        messagebox.showwarning("Atenção", "Selecione uma música para deletar.")

# Atualizar música selecionada
def abrir_janela_editar():
    selecionado = tabela_musicas.selection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione uma música.")
        return

    dados = tabela_musicas.item(selecionado[0])['values']
    id_musica = dados[0]

    def salvar_alteracao():
        try:
            atualizar_musica_bd(
                id_musica,
                campo_titulo.get(),
                campo_artista.get(),
                campo_palavras.get(),
                campo_album.get(),
                campo_genero.get(),
                campo_ano.get(),
                campo_duracao.get(),
                campo_compositor.get(),
                campo_gravadora.get(),
                campo_caminho.get()
            )
            messagebox.showinfo("Sucesso", "Música atualizada!")
            janela.destroy()
            atualizar_tabela()
        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    janela = tk.Toplevel(janela_principal)
    janela.title("Editar Música")

    labels = ["Título", "Artista", "Palavras-chave", "Álbum", "Gênero", "Ano", "Duração (seg)", "Compositor", "Gravadora", "Caminho"]
    valores = dados[1:]

    campos = []
    for i, label in enumerate(labels):
        tk.Label(janela, text=label).grid(row=i, column=0, sticky="w")

    campo_titulo = tk.Entry(janela)
    campo_artista = tk.Entry(janela)
    campo_palavras = tk.Entry(janela)
    campo_album = tk.Entry(janela)
    campo_genero = tk.Entry(janela)
    campo_ano = tk.Entry(janela)
    campo_duracao = tk.Entry(janela)
    campo_compositor = tk.Entry(janela)
    campo_gravadora = tk.Entry(janela)
    campo_caminho = tk.Entry(janela)

    entradas = [campo_titulo, campo_artista, campo_palavras, campo_album, campo_genero,
                campo_ano, campo_duracao, campo_compositor, campo_gravadora, campo_caminho]

    for i, (campo, valor) in enumerate(zip(entradas, valores)):
        campo.insert(0, valor)
        campo.grid(row=i, column=1)

    tk.Button(janela, text="Salvar Alterações", command=salvar_alteracao).grid(row=len(labels), columnspan=2, pady=10)

# Inicialização
criar_tabela()

janela_principal = tk.Tk()
janela_principal.title("Catálogo Musical")
janela_principal.state('zoomed')  # TELA CHEIA no Windows

# Frame principal que contém tudo
frame_conteudo = tk.Frame(janela_principal)
frame_conteudo.pack(fill="both", expand=True)

# Frame lateral esquerdo (botões)
frame_botoes = tk.Frame(frame_conteudo, padx=10, pady=10)
frame_botoes.pack(side="left", fill="y")

# Botões na vertical
tk.Button(frame_botoes, text="Adicionar Música", width=20, command=abrir_janela_adicionar).pack(pady=10)
tk.Button(frame_botoes, text="Editar Música", width=20, command=abrir_janela_editar).pack(pady=10)
tk.Button(frame_botoes, text="Deletar Música", width=20, command=deletar_musica_tabela).pack(pady=10)
tk.Button(frame_botoes, text="Sair", width=20, command=janela_principal.destroy).pack(pady=10)

# Frame da tabela de músicas
frame_tabela = tk.Frame(frame_conteudo)
frame_tabela.pack(side="right", fill="both", expand=True)

# Scrollbar vertical
scrollbar_y = tk.Scrollbar(frame_tabela)
scrollbar_y.pack(side="right", fill="y")

# Scrollbar horizontal
scrollbar_x = tk.Scrollbar(frame_tabela, orient="horizontal")
scrollbar_x.pack(side="bottom", fill="x")

# Tabela de músicas
colunas = ('ID', 'Título', 'Artista', 'Palavras-chave', 'Álbum', 'Gênero', 'Ano', 'Duração', 'Compositor', 'Gravadora', 'Caminho')
tabela_musicas = ttk.Treeview(frame_tabela, columns=colunas, show='headings',
                              yscrollcommand=scrollbar_y.set,
                              xscrollcommand=scrollbar_x.set)

for coluna in colunas:
    tabela_musicas.heading(coluna, text=coluna)
    tabela_musicas.column(coluna, width=150, anchor="w")

tabela_musicas.pack(fill="both", expand=True)

# Conecta scrollbars
scrollbar_y.config(command=tabela_musicas.yview)
scrollbar_x.config(command=tabela_musicas.xview)

# Atualiza os dados
atualizar_tabela()

# Inicia a interface
janela_principal.mainloop()

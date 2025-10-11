import pandas as pd
import unidecode
from fuzzywuzzy import fuzz, process
from datetime import datetime
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import subprocess
import sys

def normalizar_nome(nome):
    if pd.isna(nome):
        return ""
    nome = unidecode.unidecode(str(nome)).lower().strip()
    return " ".join(nome.split())

def calcular_diferenca_minutos(horario1, horario2):
    try:
        if not isinstance(horario1, str):
            horario1 = horario1.strftime("%H:%M")
        if not isinstance(horario2, str):
            horario2 = horario2.strftime("%H:%M")
        h1 = datetime.strptime(horario1.strip(), "%H:%M")
        h2 = datetime.strptime(horario2.strip(), "%H:%M")
        return abs((h1 - h2).total_seconds() / 60)
    except:
        return None

def processar_arquivo(input_path, status_label):
    try:
        status_label.config(text="🔄 Processando arquivo, aguarde...", fg="blue")
        output_path = "comparacao.xlsx"

        # Lê o arquivo Excel
        abas = pd.read_excel(input_path, sheet_name=None, engine="openpyxl")
        df = pd.concat(abas.values(), ignore_index=True)

        # Garante colunas corretas
        df.columns = ["Nome_SPA", "Hora_SPA", "Nome_iZeus", "Hora_iZeus"]

        # Normaliza nomes
        df["Nome_SPA_norm"] = df["Nome_SPA"].apply(normalizar_nome)
        df["Nome_iZeus_norm"] = df["Nome_iZeus"].apply(normalizar_nome)

        spa_list = df[["Nome_SPA", "Hora_SPA", "Nome_SPA_norm"]].dropna()
        izeus_list = df[["Nome_iZeus", "Hora_iZeus", "Nome_iZeus_norm"]].dropna()

        comparacao, diferenca, sem_correspondencia = [], [], []
        nomes_processados = set()

        for _, row_spa in spa_list.iterrows():
            nome_spa = row_spa["Nome_SPA_norm"]
            hora_spa = row_spa["Hora_SPA"]

            if nome_spa in nomes_processados:
                continue

            resultado = process.extractOne(nome_spa, izeus_list["Nome_iZeus_norm"], scorer=fuzz.token_sort_ratio)
            if not resultado or resultado[1] < 70:
                sem_correspondencia.append({
                    "Nome": row_spa["Nome_SPA"],
                    "Hora_SPA": hora_spa,
                    "Hora_iZeus": None,
                    "Diferença (min)": None,
                    "Observação": "Sem correspondência"
                })
                continue

            correspondencia = resultado[0]
            candidato = izeus_list[izeus_list["Nome_iZeus_norm"] == correspondencia].iloc[0]
            nome_izeus = candidato["Nome_iZeus"]
            hora_izeus = candidato["Hora_iZeus"]

            diferenca_min = calcular_diferenca_minutos(hora_spa, hora_izeus)
            nomes_processados.add(nome_spa)
            nomes_processados.add(correspondencia)

            if diferenca_min is None:
                sem_correspondencia.append({
                    "Nome": row_spa["Nome_SPA"],
                    "Hora_SPA": hora_spa,
                    "Hora_iZeus": hora_izeus,
                    "Diferença (min)": None,
                    "Observação": "Erro no formato de hora"
                })
            elif diferenca_min > 5:
                diferenca.append({
                    "Nome": row_spa["Nome_SPA"],
                    "Nome_iZeus": nome_izeus,
                    "Hora_SPA": hora_spa,
                    "Hora_iZeus": hora_izeus,
                    "Diferença (min)": round(diferenca_min, 1)
                })
            else:
                comparacao.append({
                    "Nome": row_spa["Nome_SPA"],
                    "Nome_iZeus": nome_izeus,
                    "Hora_SPA": hora_spa,
                    "Hora_iZeus": hora_izeus,
                    "Diferença (min)": round(diferenca_min, 1)
                })

        for _, row_izeus in izeus_list.iterrows():
            nome_izeus = row_izeus["Nome_iZeus_norm"]
            if nome_izeus in nomes_processados:
                continue
            sem_correspondencia.append({
                "Nome": row_izeus["Nome_iZeus"],
                "Hora_SPA": None,
                "Hora_iZeus": row_izeus["Hora_iZeus"],
                "Diferença (min)": None,
                "Observação": "Sem correspondência"
            })

        # Salva resultado
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            pd.DataFrame(comparacao).to_excel(writer, sheet_name="Comparação", index=False)
            pd.DataFrame(diferenca).to_excel(writer, sheet_name="Diferença", index=False)
            pd.DataFrame(sem_correspondencia).to_excel(writer, sheet_name="Sem_correspondência", index=False)

        status_label.config(text=f"✅ Comparação concluída! Arquivo salvo em '{output_path}'.", fg="green")
        messagebox.showinfo("Sucesso", f"Comparação concluída!\nArquivo salvo como:\n{os.path.abspath(output_path)}")

    except Exception as e:
        status_label.config(text=f"❌ Erro: {e}", fg="red")
        messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo:\n{e}")

def selecionar_arquivo(entry, status_label):
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
    if arquivo:
        entry.delete(0, tk.END)
        entry.insert(0, arquivo)
        status_label.config(text=f"Arquivo selecionado: {os.path.basename(arquivo)}", fg="black")

def abrir_pasta_saida():
    caminho = os.path.abspath(".")
    if sys.platform == "win32":
        os.startfile(caminho)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", caminho])
    else:
        subprocess.Popen(["xdg-open", caminho])

def iniciar_processamento(entry, status_label):
    caminho = entry.get()
    if not caminho:
        messagebox.showwarning("Atenção", "Selecione um arquivo antes de processar.")
        return
    threading.Thread(target=processar_arquivo, args=(caminho, status_label), daemon=True).start()

# ====== INTERFACE TKINTER ======
root = tk.Tk()
root.title("🔍 Comparador SPA x iZeus")
root.geometry("550x300")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

titulo = tk.Label(root, text="Comparador SPA x iZeus", font=("Segoe UI", 16, "bold"), bg="#f2f2f2", fg="#333")
titulo.pack(pady=15)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

entry = tk.Entry(frame, width=45, font=("Segoe UI", 10))
entry.grid(row=0, column=0, padx=5, pady=5)

botao_arquivo = tk.Button(frame, text="📂 Selecionar Arquivo", command=lambda: selecionar_arquivo(entry, status_label), bg="#0078D7", fg="white", relief="flat", padx=10, pady=5)
botao_arquivo.grid(row=0, column=1, padx=5, pady=5)

botao_processar = tk.Button(root, text="⚙️ Processar Comparação", command=lambda: iniciar_processamento(entry, status_label), bg="#28a745", fg="white", font=("Segoe UI", 11, "bold"), relief="flat", padx=10, pady=8)
botao_processar.pack(pady=10)

botao_abrir = tk.Button(root, text="📁 Abrir pasta de saída", command=abrir_pasta_saida, bg="#ffc107", fg="black", relief="flat", padx=10, pady=5)
botao_abrir.pack(pady=5)

status_label = tk.Label(root, text="Selecione o arquivo para iniciar a comparação.", bg="#f2f2f2", font=("Segoe UI", 10), fg="#555")
status_label.pack(pady=10)

root.mainloop()

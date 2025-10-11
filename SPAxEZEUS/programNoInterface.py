import pandas as pd
import unidecode
from fuzzywuzzy import fuzz, process
from datetime import datetime
import os

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

def processar_arquivo():
    input_path = "ArquivoTeste.xlsx"
    output_path = "comparacao.xlsx"

    if not os.path.exists(input_path):
        print(f"❌ Arquivo '{input_path}' não encontrado no diretório atual.")
        return

    try:
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

        print(f"✅ Comparação concluída! Resultado salvo em '{output_path}'.")

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    processar_arquivo()

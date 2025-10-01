import pandas as pd
import sqlite3
import os

DB_FILE = 'empresa.db'
TABLE_NAME = 'usuarios'
EXCEL_FILE = 'usuarios_exportados.xlsx'

def exportar_sqlite_para_excel():
    if not os.path.exists(DB_FILE):
        print(f"Erro: O arquivo de banco de dados '{DB_FILE}' não foi encontrado.")
        return
    
    try:
        conn = sqlite3.connect(DB_FILE)
        query = f"SELECT * FROM '{TABLE_NAME}'"

        df = pd.read_sql_query(query, conn)
        conn.close()

        df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

        print(f"Sucesso! Os dados da tabela '{TABLE_NAME}' foram exportados para '{EXCEL_FILE}'")
    
    except sqlite3.OperationalError as e:
        print(f"Erro de SQL: {e}. Verifique se a tabela '{TABLE_NAME}' existe.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: '{e}'")

if __name__ == "__main__":
    exportar_sqlite_para_excel() 



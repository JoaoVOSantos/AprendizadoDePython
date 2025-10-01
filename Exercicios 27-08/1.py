import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular():
    try:

        data1 = entrada_data1.get()
        data2 = entrada_data2.get()
        formato = "%d/%m/%Y"
        d1 = datetime.strptime(data1, formato)
        d2 = datetime.strptime(data2, formato)
        diferenca = abs((d2 - d1).days)
        
        label_resultado.config(text=f"Diferença em dias: {diferenca} Dias")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor insira numeros validos")

janela = tk.Tk()
janela.title("Compra de Ingresso Simples")
janela.geometry("350x300")
janela.resizable(False, False)

label_ingresso = tk.Label(janela, text="Valor do ingresso: R$20,00")
label_ingresso.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_data1 = tk.Label(janela, text="Digite a primeira data (dd/mm/yyyy): ")
label_data1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_data1 = tk.Entry(janela)
entrada_data1.grid(row=1, column=1, padx=10, pady=10)

label_data2 = tk.Label(janela, text="Digite a segunda data (dd/mm/yyyy): ")
label_data2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_data2 = tk.Entry(janela)
entrada_data2.grid(row=2, column=1, padx=10, pady=10)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=5, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.grid(row=6, column=0, columnspan=2)

janela.mainloop()
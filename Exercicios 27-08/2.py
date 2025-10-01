import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular():
    try:
        ingresso = 20
        qtde = int(entrada_qtde.get())
        tipo = comboBox.get()  # Pega o valor selecionado na combobox

        resultado = 0

        if tipo == 'Inteira':
            resultado = ingresso * qtde
        elif tipo == "Meia":
            resultado = (ingresso * 0.5) * qtde
        elif tipo == "Idoso":
            resultado = (ingresso * 0.4) * qtde
        elif tipo == "Criança":
            label_resultado.config(text=f"Ingresso gratuito para criança.")
            return

        label_resultado.config(text=f"Total a Pagar: R${resultado}")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor insira numeros validos")

# Janela principal
janela = tk.Tk()
janela.title("Compra de Ingresso Simples")
janela.geometry("350x300")
janela.resizable(False, False)

# Informações
label_ingresso = tk.Label(janela, text="Valor do ingresso: R$20,00")
label_ingresso.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Quantidade
label_quantidade = tk.Label(janela, text="Quantidade de Ingressos:")
label_quantidade.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_qtde = tk.Entry(janela)
entrada_qtde.grid(row=1, column=1, padx=10, pady=10)

# ComboBox para tipo de ingresso
label_tipo = tk.Label(janela, text="Tipo de ingresso:")
label_tipo.grid(row=2, column=0, padx=10, pady=10, sticky="w")

opcoes = ["Inteira", "Meia", "Idoso", "Criança"]
comboBox = ttk.Combobox(janela, values=opcoes, state="readonly")
comboBox.grid(row=2, column=1, padx=10, pady=10)  # ok
comboBox.set("Inteira")  # Valor padrão


# Botão de calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=20)

# Resultado
label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.grid(row=4, column=0, columnspan=2)

# Iniciar app
janela.mainloop()

import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        ingresso = 20
        qtde = int(entrada_qtde.get())
        
        tipo = var_tipo.get()
        
        resultado = 0
        
        if tipo == 'Inteira':
            r = (ingresso * 100) / 100
            resultado = r * qtde 
            
        elif tipo == "Meia":
            r = (ingresso * 50) / 100
            resultado = r * qtde 
        elif tipo == "Idoso":
            r = (ingresso * 40) / 100
            resultado = r * qtde
        elif tipo == "Crianca":
            resultado = "Gratis"
            
        label_resultado.config(text=f"Total a Pagar: R${resultado}")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor insira numeros validos")

janela = tk.Tk()
janela.title("Compra de Ingresso Simples")
janela.geometry("350x300")
janela.resizable(False, False)

label_ingresso = tk.Label(janela, text="Valor do ingresso: R$20,00")
label_ingresso.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_quantidade = tk.Label(janela, text="Quantidade de Ingresso: ")
label_quantidade.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_qtde = tk.Entry(janela)
entrada_qtde.grid(row=1, column=1, padx=10, pady=10)

label_operacao = tk.Label(janela, text="Escolha a operação: ")
label_operacao.grid(row=2, column=0, columnspan=2, pady=5)

var_tipo = tk.StringVar(value="Inteira")

radio_soma = tk.Radiobutton(janela, text="Inteira", variable=var_tipo, value="Inteira")
radio_soma.grid(row=3, column=0, sticky="w", padx=20)

radio_sub = tk.Radiobutton(janela, text="Meia", variable=var_tipo, value="Meia")
radio_sub.grid(row=3, column=1, sticky="w", padx=20)

radio_mult = tk.Radiobutton(janela, text="Idoso", variable=var_tipo, value="Idoso")
radio_mult.grid(row=4, column=0, sticky="w", padx=20)

radio_div = tk.Radiobutton(janela, text="Criança", variable=var_tipo, value="Crianca")
radio_div.grid(row=4, column=1, sticky="w", padx=20)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=5, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.grid(row=6, column=0, columnspan=2)

janela.mainloop()
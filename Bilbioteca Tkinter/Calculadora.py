import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        
        operacao = var_operacao.get()
        
        resultado = 0
        operador_texto = ""
        
        if operacao == 'soma':
            resultado = num1 + num2
            operador_texto = "+"
        elif operacao == "subtracao":
            resultado = num1 - num2
            operador_texto = "-"
        elif operacao == "multiplicacao":
            resultado = num1 * num2
            operador_texto = "*"
        elif operacao == "divisao":
            if num2 == 0:
                messagebox.showerror("Erro de por zero não é permitida")
                return
            resultado = num1 / num2
            operador_texto = "/"
            
        label_resultado.config(text=f"Resultado: {num1} {operador_texto} {num2} = {resultado}")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor insira numeros validos")

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("350x300")
janela.resizable(False, False)

label_num1 = tk.Label(janela, text="Primeiro numero: ")
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_num1 = tk.Entry(janela)
entrada_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(janela, text="Segundo numero")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_num2 = tk.Entry(janela)
entrada_num2.grid(row=1, column=1, padx=10, pady=10)

label_operacao = tk.Label(janela, text="Escolha a operação: ")
label_operacao.grid(row=2, column=0, columnspan=2, pady=5)

var_operacao = tk.StringVar(value="soma")

radio_soma = tk.Radiobutton(janela, text="Soma (+)", variable=var_operacao, value="soma")
radio_soma.grid(row=3, column=0, sticky="w", padx=20)

radio_sub = tk.Radiobutton(janela, text="Subtração (-)", variable=var_operacao, value="subtracao")
radio_sub.grid(row=3, column=1, sticky="w", padx=20)

radio_mult = tk.Radiobutton(janela, text="Multiplicação (*)", variable=var_operacao, value="multiplicacao")
radio_mult.grid(row=4, column=0, sticky="w", padx=20)

radio_div = tk.Radiobutton(janela, text="Divisão (/)", variable=var_operacao, value="divisao")
radio_div.grid(row=4, column=1, sticky="w", padx=20)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=5, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.grid(row=6, column=0, columnspan=2)

janela.mainloop()
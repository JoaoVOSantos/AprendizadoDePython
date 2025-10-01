import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário com valores base por destino
precos_base = {
    "São Paulo": 500,
    "Rio de Janeiro": 450,
    "Salvador": 600,
    "Fortaleza": 650
}

def calcular():
    destino = combo_destinos.get()
    tipo_assento = var_assento.get()

    if destino not in precos_base:
        messagebox.showerror("Erro", "Por favor, selecione um destino válido.")
        return

    valor_base = precos_base[destino]

    if tipo_assento == "Economica":
        valor_total = valor_base
    elif tipo_assento == "Executiva":
        valor_total = valor_base * 1.5
    elif tipo_assento == "Primeira":
        valor_total = valor_base * 2
    else:
        messagebox.showerror("Erro", "Por favor, selecione o tipo de assento.")
        return

    label_resultado.config(text=f"Valor da passagem: R${valor_total:.2f}")

# Janela principal
janela = tk.Tk()
janela.title("Compra de Passagem Aérea")
janela.geometry("400x300")
janela.resizable(False, False)

# Destino
tk.Label(janela, text="Escolha o destino:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
destinos = list(precos_base.keys())
combo_destinos = ttk.Combobox(janela, values=destinos, state="readonly")
combo_destinos.grid(row=0, column=1, padx=10, pady=10)
combo_destinos.set("São Paulo")

# Tipo de assento
tk.Label(janela, text="Tipo de assento:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

var_assento = tk.StringVar()
frame_assento = tk.Frame(janela)
frame_assento.grid(row=1, column=1, padx=10, pady=10)

tk.Radiobutton(frame_assento, text="Econômica", variable=var_assento, value="Economica").pack(anchor="w")
tk.Radiobutton(frame_assento, text="Executiva", variable=var_assento, value="Executiva").pack(anchor="w")
tk.Radiobutton(frame_assento, text="Primeira Classe", variable=var_assento, value="Primeira").pack(anchor="w")

# Botão calcular
tk.Button(janela, text="Calcular Valor", command=calcular).grid(row=2, column=0, columnspan=2, pady=20)

# Resultado
label_resultado = tk.Label(janela, text="Valor da passagem: ", font=("Arial", 12, "bold"))
label_resultado.grid(row=3, column=0, columnspan=2)

janela.mainloop()

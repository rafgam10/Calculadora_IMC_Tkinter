import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from comados import add_placeholder, calcular_imc

# Configuração da janela
root = ttk.Window(themename="darkly")
root.title("Calculadora IMC")
root.geometry("350x400")

# Criando estilo para placeholders
style = ttk.Style()
style.configure("Placeholder.TEntry", foreground="gray")

# Dados do peso
entry_peso = ttk.Entry(root, width=25, style="Placeholder.TEntry", justify="center")
entry_peso.grid(row=0, column=0, columnspan=2, padx=20, pady=5)
add_placeholder(entry_peso, "Digite seu peso (kg)")

# Dados da altura
entry_altura = ttk.Entry(root, width=25, style="Placeholder.TEntry", justify="center")
entry_altura.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
add_placeholder(entry_altura, "Digite sua altura (m)")

# Label para resultado do IMC (Centralizado)
label_resultado = ttk.Label(
    root, text="", width=30, font=("Helvetica", 14), anchor="center", justify="center"
)
label_resultado.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Botão de envio
button_enviar = ttk.Button(
    root, text="Calcular IMC", width=20,
    command=lambda: calcular_imc(entry_peso, entry_altura, label_resultado)
)
button_enviar.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

root.mainloop()

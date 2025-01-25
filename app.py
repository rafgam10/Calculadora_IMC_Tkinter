import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from comados import *

# CÓDIGO DA CONFIGURAÇÃO:
root =  ttk.Window(themename="darkly")
root.title("Calculadora IMC")
root.geometry("220x400")


# CÓDIGO DO LAYOUT:

#Dados do peso
entry_peso = ttk.Entry(root, width=20)
entry_peso.grid(row=0, column=0, padx=10, pady=5)

#Dados da altura
entry_altura = ttk.Entry(root, width=20)
entry_altura.grid(row=1, column=0, padx=10, pady=5)


label_resultado = ttk.Label(root, text="", width=20, font=("Helvetica", 12))
label_resultado.grid(row=3, column=0, padx=20, pady=10)

#Button enviar dados;
button_enviar = ttk.Button(root, text="Enviar", width=10, command=lambda:calcular_imc(entry_peso, entry_altura, label_resultado))
button_enviar.grid(row=2, column=0, padx=10, pady=5)









root.mainloop()
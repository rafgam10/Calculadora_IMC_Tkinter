from math import pow
import ttkbootstrap as ttk

# Função de calcular:

def calcular_imc(entry_peso, entry_altura, label_resultado):
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / pow(altura, 2)
        

    
        if imc < 18.5:
            categoria = "Magreza"
            cor = "warning"
        elif 18.5 <= imc < 24.9:
            categoria = "Normal"
            cor = "success"
        elif 24.9 <= imc < 29.9:
            categoria = "Sobrepeso"
            cor = "warning"
        elif 30.0 <= imc < 34.9:
            categoria = "Obesidade grau I"
            cor = "danger"
        elif 35.0 <= imc < 39.9:
            categoria = "Obesidade grau II"
            cor = "danger"
        else:
            categoria = "Obesidade grau III"
            cor = "danger"

        entry_peso.delete(0, "end")
        entry_altura.delete(0, "end")
        label_resultado.config(text=f"IMC: {imc:.2f} ({categoria})", bootstyle=cor)



    except ValueError:
        label_resultado.config(text="Insira valores válidos!")

# Função de eventos para o entry:

def add_placeholder(entry, text):
    """Adiciona placeholder ao Entry."""
    entry.insert(0, text)
    entry.config(foreground="gray")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, "end")
            entry.config(foreground="white")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(foreground="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
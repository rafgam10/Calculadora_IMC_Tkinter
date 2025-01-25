from math import pow

def calcular_imc(entry_peso, entry_altura, label_resultado):
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / pow(altura, 2)
        entry_peso.delete(0, "end")
        entry_altura.delete(0, "end")

        label_resultado.config(text=f"IMC: {imc:.2f}")
    except ValueError:
        label_resultado.config(text="Insira valores válidos!")

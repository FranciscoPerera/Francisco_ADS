# Desafio Interface Grafica

import tkinter as tk
from tkinter import messagebox      

def calcular_imc(): 
    valor_peso = float(peso.get())
    valor_altura = float(altura.get())
    imc = valor_peso / (valor_altura ** 2)

    if imc < 18.5:
        resultado.config(text=f"{nome.get()} seu IMC é: {imc:.2f}")
        messagebox.showinfo("Mensagem !!", "Voce esta abaixo do peso")
    elif 18.6 <= imc < 24.9:
        resultado.config(text=f"{nome.get()} seu IMC é: {imc:.2f}")
        messagebox.showinfo("Mensagem !!", "Voce esta com o peso normal")
    elif 25 <= imc < 29.9:
        resultado.config(text=f"{nome.get()} seu IMC é: {imc:.2f}")
        messagebox.showinfo("Mensagem !!", "Voce esta com sobrepeso")
    elif 30 <= imc < 34.9:
        resultado.config(text=f"{nome.get()} seu IMC é: {imc:.2f}")
        messagebox.showinfo("Mensagem !!", "Voce esta com Obesidade grau 1")
    elif 35 <= imc < 39.9:
        resultado.config(text=f"{nome.get()} seu IMC é: {imc:.2f}")
        messagebox.showinfo("Mensagem !!", "Voce esta com Obesidade grau 2")
    else:
        resultado.config(text=f"{nome.get()} seu IMC é: {imc:.2f}")
        messagebox.showinfo("Mensagem !!", "Voce esta com Obesidade grau 3")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculador de IMC")
janela.geometry("400x400")

# Cria os componentes
entrada_nome = tk.Label(janela, text="Digite seu nome: ", font="Arial")
nome = tk.Entry(janela, font="Arial")

entrada_peso = tk.Label(janela, text="Digite seu peso (em kg): ", font="Arial")
peso = tk.Entry(janela, font="Arial")

entrada_altura = tk.Label(janela, text="Digite sua altura em metros(Ex.1.80): ", font="Arial")
altura = tk.Entry(janela, font="Arial")

bt = tk.Button(janela, text="Descobrir!", width=10, command=calcular_imc)
resultado = tk.Label(janela, text="", font="Arial")
resultado2 = tk.Label(janela, text="", font="Arial")

# Adiciona os componentes à janela
entrada_nome.pack(pady=5)
nome.pack(pady=5)
entrada_peso.pack(pady=5)
peso.pack(pady=5)
entrada_altura.pack(pady=5)
altura.pack(pady=5)
bt.pack(pady=5)
resultado.pack(pady=5)
resultado2.pack(pady=5)

# Inicia a interface
janela.mainloop()
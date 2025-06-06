# Desafio Interface Grafica

import tkinter as tk

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.6 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def prof(nome):
    if nome.strip().lower() == "aguado":
        print("Não interessa. Você está perfeito!!")
        exit()

print("--------------Calculador de IMC----------")
nome = input("Qual seu nome: ")
prof(nome)
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura em metros(Ex.1.80): "))
    
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
    
print(f"{nome} seu IMC é: {imc:.2f}")
print(f"Classificado como: {classificacao}")

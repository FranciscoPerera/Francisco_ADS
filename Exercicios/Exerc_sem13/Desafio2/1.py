# Desafio Interface Grafica

import tkinter as tk

nome = input("Digite seu nome: ")

s1 = float(input("Qual seu salario de janeiro: "))
s2 = float(input("Qual seu salario de fevereiro: "))
s3 = float(input("Qual seu salario de março: "))

salario = s1 + s2 + s3

print(nome ,"Neste ano você recebeu R$", salario)

if (salario <= 15000):
    print("Hey! Até agora você está isento de pagar Imposto de Renda!!!")
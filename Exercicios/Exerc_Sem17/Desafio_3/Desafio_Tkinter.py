# Crie um programa em Python, utilizando interface gráfica Tkinter que calcule a média na disciplina Lógica de Programação e retorne a mensagem se o/a estudante está aprovado/ 
# ou reprovado/a. As informações que deverão ser inseridas são:
# Nome: 
# Média dos Exercícios: 
# Nota Desafio 1:     Nota Desafio 2:    Nota Desafio 3:   
# Notas Projeto    Fase 1:    Fase 2:     Fase 3:    
# Calcule a média ((Média Atividades + Média Desafios + Projeto*2) / 4). As possíveis saídas são: 
# Se nota maior ou igual 6: 
# Parabéns! Você foi aprovado com nota ??? 
# Se nota entre 4 e 6: 
# Você ainda não foi aprovado! Sua nota foi ???. Você terá a opção de fazer o IFA!!!
# Se nota menor que 4: 
# Com a nota ??? você não foi aprovado! Veja pelo lado bom, você irá cursar a disciplina novamente semestre que vem!!!

import tkinter as tk
from tkinter import messagebox

def calcular():
    nome_aluno = nome.get()
    media_exercicios = float(media_ex.get())

    d1 = float(nota_d1.get())
    d2 = float(nota_d2.get())
    d3 = float(nota_d3.get())
    media_desafios = (d1 + d2 + d3) / 3

    f1 = float(nota_f1.get())
    f2 = float(nota_f2.get())
    f3 = float(nota_f3.get())
    media_fase = (f1 + f2 + f3) / 3
    media_final = (media_exercicios + media_desafios + 2 * media_fase) / 4

    if media_final >= 6:
        mensagem = f"Parabéns {nome_aluno}! Você foi aprovado(a) com nota {media_final:.2f}."
    elif 4 <= media_final < 6:
        mensagem = (f"{nome_aluno}, você ainda não foi aprovado(a). Sua nota foi {media_final:.2f}. Você terá a opção de fazer o IFA!!!")
    else:
        mensagem = (f"{nome_aluno}, com nota {media_final:.2f} você não foi aprovado(a). Mas veja pelo lado bom: você cursará a disciplina novamente no próximo semestre!")

    messagebox.showinfo("Resultado", mensagem)

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de media")
janela.geometry("400x600")

# Campos de entrada e saida
entrada_nome = tk.Label(janela, text="Digite seu nome: ", font="Arial").pack(pady=5)
nome = tk.Entry(janela, font="Arial")
nome.pack(pady=5)

entrada_media_ex = tk.Label(janela, text="Média dos Exercícios:", font="Arial").pack(pady=5)
media_ex = tk.Entry(janela, font="Arial")
media_ex.pack(pady=5)

entrada_nota_d1 = tk.Label(janela, text="Nota do Desafio 1:", font="Arial").pack(pady=5)
nota_d1 = tk.Entry(janela, font="Arial")
nota_d1.pack(pady=5)

entrada_nota_d2 = tk.Label(janela, text="Nota do Desafio 2:", font="Arial").pack(pady=5)
nota_d2 = tk.Entry(janela, font="Arial")
nota_d2.pack(pady=5)

entrada_nota_d3 = tk.Label(janela, text="Nota do Desafio 3:", font="Arial").pack(pady=5)
nota_d3 = tk.Entry(janela, font="Arial")
nota_d3.pack(pady=5)

entrada_nota_f1 = tk.Label(janela, text="Projeto – Fase 1:", font="Arial").pack(pady=5)
nota_f1 = tk.Entry(janela, font="Arial")
nota_f1.pack(pady=5)

entrada_nota_f2 = tk.Label(janela, text="Projeto – Fase 2:", font="Arial").pack(pady=5)
nota_f2 = tk.Entry(janela, font="Arial")
nota_f2.pack(pady=5)

entrada_nota_f3 = tk.Label(janela, text="Projeto – Fase 3:", font="Arial").pack(pady=5)
nota_f3 = tk.Entry(janela, font="Arial")
nota_f3.pack(pady=5)

bt = tk.Button(janela, text="Calcular Média", command=calcular, width=20, bg="#4CAF50")
bt.pack(pady=20)

janela.mainloop()

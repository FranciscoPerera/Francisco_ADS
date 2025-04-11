# Atividade_Desafio
# Faça um programa em Python que pergunte ao usuário: a) o nome de uma disciplina; b) a nota dele/a na disciplina e c) a quantidade de faltas na disciplina. Se sua nota for
# inferior a 4 OU tiver mais que 20 faltas, escreva “Está reprovado/a”; Se sua nota estiver entre 4 e 6 e tiver menos que 20 faltas, escreva “Você está de IFA!”; Se sua nota for igual
# ou maior que 6 e tiver menos que 20 faltas, escreva “Aprovado/a”!

disciplina = input("Digite o nome da disciplina: ")
nota = float(input("Digite sua nota na disciplina: "))
faltas = int(input("Digite a quantidade de faltas: "))

if nota < 4 or faltas > 20:
    print("Está reprovado/a")
elif 4 <= nota < 6 and faltas <= 20:
    print("Você está de IFA!")
elif nota >= 6 and faltas <= 20:
    print("Aprovado/a")
    
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

def calcular(media_ex, media_des, media_fase):
    return (media_ex + media_des + media_fase * 2) / 4

print("CALCULADORA DE MEDIA")
nome = input("Digite seu nome: ")

media_ex = float(input("Digite média dos seus exercícios: "))

nota_d1 = float(input("Digite a nota do desafio 1: "))
nota_d2 = float(input("Digite a nota do desafio 2: "))
nota_d3 = float(input("Digite a nota do desafio 3: "))
media_des = (nota_d1 + nota_d2 + nota_d3) / 3

nota_f1 = float(input("Digite a nota da fase 1: "))
nota_f2 = float(input("Digite a nota da fase 2: "))
nota_f3 = float(input("Digite a nota da fase 3: "))
media_fase = (nota_f1 + nota_f2 + nota_f3) / 3

nota_final = calcular(media_ex, media_des, media_fase)

if nota_final >= 6:
    print(f"Parabéns {nome}! Você foi aprovado com nota: {nota_final:.2f}")
elif 4 <= nota_final < 6:
    print(f"{nome}, você ainda não foi aprovado. Sua nota foi {nota_final:.2f}. Você terá a opção de fazer o IFA!")
else:
    print(f"{nome}, com nota {nota_final:.2f} você não foi aprovado. Mas veja pelo lado bom: você cursará a disciplina novamente no próximo semestre!")

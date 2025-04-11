# Atividade_Desafio
# Você sabia que um ano para ser bissexto, precisa ser múltiplo de 4? Sabendo disso, faça um programa em Python que pergunte o ano de nascimento da pessoa e caso seja
# bissexto, escreverá “Você nasceu em um ano bissexto!”. Caso esse ano não seja bissexto, o programa escreverá “Você não nasceu em um ano bissexto!”

ano = int(input("Digite o ano do seu nascimento: "))

if (ano % 4 == 0):
    print("Você nasceu em um ano bissexto!")
else:
    print("Você não nasceu em um ano bissexto!")

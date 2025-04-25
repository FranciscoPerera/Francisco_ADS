# 1) Escreva um algoritmo que receba 7 valores numéricos e retorne na tela a mensagem:
# “Entre os 7 valores, X são números negativos!”.

Numero1 = int(input("Digite o primeiro número: "))
Numero2 = int(input("Digite o segundo número: "))   
Numero3 = int(input("Digite o terceiro número: "))
Numero4 = int(input("Digite o quarto número: "))
Numero5 = int(input("Digite o quinto número: "))
Numero6 = int(input("Digite o sexto número: "))
Numero7 = int(input("Digite o sétimo número: "))

numeros = [Numero1, Numero2, Numero3, Numero4, Numero5, Numero6, Numero7]

contagem = 0
for numero in numeros:
    if numero < 0:
        contagem += 1

print(f"Entre os 7 valores, apenas {contagem} são números negativos!")

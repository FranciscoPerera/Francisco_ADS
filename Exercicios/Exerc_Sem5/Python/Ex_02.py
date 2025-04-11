# O banco do brasil está com uma campanha para incentivar as pessoas a usarem seu cartão de crédito. De acordo com o valor da fatura no mês, um certo percentual de 
# cashback será creditado na conta corrente do usuário. Se o valor da fatura for de até R$1000,00, não haverá cashback. Faturas entre R$1000,00 e R$4000,00 terão 
# cashback de 1%. Faturas entre R$4000,00 e R$8000,00 terão cashback de 2%. Faturas acima de R$8000,00 terão cashback de 5%. Faça um software em que o usuário 
# informe o valor de sua fatura e você retornará na tela para ele, qual o valor de cashback que ele terá naquele mês.

print("------------Calculadora de cashback--------------")
nome = input("Qual é o seu nome? ")
valor = float(input("Qual o valor de sua fatura: "))

def calcular_cas(valor):
    if valor <= 1000:
        print("Não haverá cashback")
        exit()
    elif valor <= 4000:
        return valor * 0.01
    elif valor <= 8000:
        return valor * 0.02
    else:
        return valor * 0.05

cashback = calcular_cas(valor)
print(f"{nome}, voce terá R${cashback} de cashback")

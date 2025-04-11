# O supermercado Delta está fazendo uma promoção. Se a pessoa for sócio do Clube Delta ou ela tiver mais de 60 anos, terá R$10,00 de desconto no valor total da compra. 
# Além disso, para os sócio do Clube Delta que estão fazendo aniversário naquele dia, haverá um desconto adicional de R$ 5,00. Esses descontos todos são validos 
# somente para compras acima de R$ 100,00. Faça o melhor software possível, que receba as informações necessárias do usuário e ao final diga o valor total da compra.

print("------------Mercado Delta--------------")
socio = input("Você é sócio do Clube Delta? (sim/nao): ").lower()
idade = int(input("Qual sua idade? "))
niver = input("Você faz aniversário hoje? (sim/nao): ").lower()
valor = float(input("Qual o valor de sua compra? R$ "))

def calcular_var(valor):
    desconto = 0
    if socio == "sim" or idade > 60:
        desconto = 10
    if socio == "sim" and niver == "sim":
        desconto += 5
    return valor - desconto

if valor > 100:
    valor_final = calcular_var(valor)
    print(f"O valor total da compra é: R$ {valor_final}")
else:
    print(f"O valor da compra é: R$ {valor:.2f}")
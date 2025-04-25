# O supermercado Delta está fazendo uma promoção. Se a pessoa for sócio do Clube Delta ou ela tiver mais de 60 anos, terá R$10,00 de desconto no valor total da compra. 
# Além disso, para os sócio do Clube Delta que estão fazendo aniversário naquele dia, haverá um desconto adicional de R$ 5,00. Esses descontos todos são validos 
# somente para compras acima de R$ 100,00. Faça o melhor software possível, que receba as informações necessárias do usuário e ao final diga o valor total da compra.

from datetime import datetime

def calcular_valor(valor, idade, socio, aniversario):
    desconto = 0
    if valor > 100:
        if socio == "sim" or idade >= 60:
            desconto += 10
        if socio == "sim" and aniversario:
            desconto += 5
    return valor - desconto

while True:
    print("\n------------Mercado Delta--------------")
    print("1. Calcular valor da compra")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor da compra: R$ "))
        data_nasc = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")
        socio = input("Você é sócio do Clube Delta? (sim/nao): ").lower()

        # Converte a data de nascimento para um objeto datetime
        data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
        hoje = datetime.now()

        # Calcula a idade do usuário
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

        # Verifica se hoje é o aniversário do usuário
        aniversario = (hoje.day == data_nasc.day and hoje.month == data_nasc.month)

        valor_final = calcular_valor(valor, idade, socio, aniversario)

        print(f"O valor total da compra é: R$ {valor_final:.2f}")
    elif opcao == "2":
        print("Obrigado por usar o Mercado Delta.")
        break
    else:
        print("Opção inválida. Tente novamente.")

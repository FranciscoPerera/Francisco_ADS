# Melhore o programa que desenvolvemos no item 3 da lista de exercícios, para que o usuário apenas precise informar:
# - Valor da compra; - Data de Nascimento; - Se é ou não sócio do clube;
# DICA: Vocês precisam descobrir como a) obter a data do computador em Python; b) como fazer operações com datas.

from datetime import datetime 

valor = float(input("Digite o valor da compra: "))
data_nasc = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")
socio = int(input("Digite 1 se você for sócio do Clube Delta ou 0 se não: "))
data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y") # Converte a data de nascimento de string para datetime.
hoje = datetime.now() # Pega a data atual

# Calcula a idade do usuário com base na data de nascimento e na data atual.
# Subtrai o ano de nascimento do ano atual e ajusta caso o aniversário ainda não tenha ocorrido este ano.
idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

# Verifica se hoje é o aniversário do usuário.
aniversario = (hoje.day == data_nasc.day and hoje.month == data_nasc.month)

# Aplica descontos ao valor da compra, caso o valor seja maior ou igual a R$ 100,00.
if valor >= 100.00:
    desconto = 0
    if socio == 1 and aniversario:
        desconto = 10
    elif socio == 1 or idade >= 60:
        desconto = 5
    return valor - desconto

print(f"Valor total da compra: R$ {valor:.2f}")
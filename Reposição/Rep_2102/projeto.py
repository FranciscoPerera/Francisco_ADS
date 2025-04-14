# Melhore o programa que desenvolvemos no item 3 da lista de exercícios, para que o usuário apenas precise informar:
# - Valor da compra; - Data de Nascimento; - Se é ou não sócio do clube;
# DICA: Vocês precisam descobrir como a) obter a data do computador em Python; b) como fazer operações com datas.

from datetime import datetime

valor = float(input("Digite o valor da compra: "))
data_nascimento = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")
socio = int(input("Digite 1 se você for sócio do Clube Delta ou 0 se não: "))

# Processamento da data de nascimento
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
hoje = datetime.now()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

# Verifica se é aniversário
aniversario = (hoje.day == data_nascimento.day and hoje.month == data_nascimento.month)

if valor >= 100.00:
    if socio == 1 and aniversario:
        valor -= 15.00
    elif socio == 1 or idade >= 60:
        valor -= 10.00

print(f"Valor total da compra: R$ {valor:.2f}")
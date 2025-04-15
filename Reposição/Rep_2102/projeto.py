# Melhore o programa que desenvolvemos no item 3 da lista de exercícios, para que o usuário apenas precise informar:
# - Valor da compra; - Data de Nascimento; - Se é ou não sócio do clube;
# DICA: Vocês precisam descobrir como a) obter a data do computador em Python; b) como fazer operações com datas.

from datetime import datetime

# Função para calcular o valor com desconto
def calcular_valor_com_desconto(valor, idade, socio, aniversario):
    if valor >= 100.00:
        if socio == 1 and aniversario:
            return valor - 15.00
        elif socio == 1 or idade >= 60:
            return valor - 10.00
    return valor

# Entrada de dados do usuário
valor = float(input("Digite o valor da compra: "))
data_nasc = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")
socio = int(input("Digite 1 se você for sócio do Clube Delta ou 0 se não: "))

# Converte a data de nascimento de string para datetime
data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
hoje = datetime.now()

# Calcula a idade do usuário
idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

# Verifica se hoje é o aniversário do usuário
aniversario = (hoje.day == data_nasc.day and hoje.month == data_nasc.month)

# Calcula o valor final com desconto
valor_final = calcular_valor_com_desconto(valor, idade, socio, aniversario)

# Exibe o valor total da compra
print(f"Valor total da compra: R$ {valor_final:.2f}")
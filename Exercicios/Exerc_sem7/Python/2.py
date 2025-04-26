# 2) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário 
# e número de filhos. A prefeitura deseja saber:  

# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$00,1000.

# Faça um software que permita a coleta desses dados e ao final, imprima na tela as informações desejadas.

sal = []
fil = []

while True:
    salario = float(input("Qual o seu salário? (Digite -1 para sair): "))
    if salario == -1:
        break

    filhos = int(input("Quantos filhos você tem? "))
    sal.append(salario)
    fil.append(filhos)

    if len(sal) > 0:
        med_salario = sum(sal) / len(sal)
        med_filhos = sum(fil) / len(fil)
        maior = max(sal)
        percentual = (len([s for s in sal if s <= 1000]) / len(sal)) * 100

        print(f"\nMédia de salário da população: R${med_salario:.2f}")
        print(f"Média do número de filhos: {med_filhos:.2f}")
        print(f"Maior salário: R${maior:.2f}")
        print(f"Percentual com salário até R$1000: {percentual:.2f}%")
    else:
        print("Nenhum dado foi inserido.")



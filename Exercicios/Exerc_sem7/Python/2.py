# 2) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário 
# e número de filhos. A prefeitura deseja saber:  

# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$00,1000.

# Faça um software que permita a coleta desses dados e ao final, imprima na tela as informações desejadas.

sair = 1
sai = 1

while (sair != "0"):
    sal = []
    fil = []

    while (sai != "1"):
        
        salario = int(input("Qual o seu salario: "))
        filhos = int(input("Quantos filhos voce tem: "))

        if salario or filhos == -1:
            break
        sal.append(salario)
        fil.append(filhos)

        if len(sal) > 0:
            med_salario = sum(sal) / len(sal)
            med_filhos = sum(fil) / len(fil)
            maior = max(sal)
            percentual = (len([s for s in sal if s <= 1000]) / len(sal)) * 100

    
            print(f"A media de salario da população é: {med_salario}")
            print(f"A média do número de filhos é: {med_filhos}")
            print(f"O maior salario é: {maior}")
            print(f"O percentual de pessoas com salário até R$1000 é: {percentual}")

        else:
            print("Nenhum numero digitado.")

        sai = input("Digite 1 pra finanlizar. Ou clique em algo para continuar.  ")

    sair = input("Digite 0 pra finanlizar. Ou clique em algo para continuar.  ")



# 3) Escreva um algoritmo que leia n valores numéricos (quantos o usuário quiser digitar) e 
# encontre o maior, o menor deles e a média aritmética. Mostre o resultado.

sair = 1
sai = 1

while (sair != "0"):
    pessoas = []

    while (sai != "1"):
        
        numero = int(input("Digite um numero: "))
        if numero == -1:
            break
        pessoas.append(numero)

        if pessoas:
            menor = min(pessoas)
            maior = max(pessoas)
            media = sum(pessoas)
    
            print(f"A menor altura do grupo é {menor}")
            print(f"A maior altura do grupo é {maior}")
            print(f"A media aritmetica do grupo é {media}")
        else:
            print("Nenhum numero digitado.")

        sai = input("Digite 1 pra finanlizar. Ou clique em algo para continuar.  ")

    sair = input("Digite 0 pra finanlizar. Ou clique em algo para continuar.  ")



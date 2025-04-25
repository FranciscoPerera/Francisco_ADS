# 4) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar :
# 	a) A menor altura do grupo;
# 	b) A maior altura do grupo;

pessoas = []
for i in range(15):
    altura = float(input("Digite sua altura: "))
    pessoas.append(altura)

menor = min(pessoas)
maior = max(pessoas)

print(f"A menor altura do grupo é {menor}")
print(f"A maior altura do grupo é {maior}")


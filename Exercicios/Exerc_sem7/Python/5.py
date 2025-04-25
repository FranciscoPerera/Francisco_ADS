# 5) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

for i in range(1, 201):
    if i % 2 != 0:
        print(f"{i} é um números ímpar entre 100 e 200")
    else:
        print(i)

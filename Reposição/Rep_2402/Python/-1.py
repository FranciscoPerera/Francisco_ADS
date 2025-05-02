# -1) Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: “Múltiplo de 10”.

for i in range(1, 101):
    if i % 10 == 0:
        print(f"{i} é um Múltiplo de 10")
    else:
        print(i)
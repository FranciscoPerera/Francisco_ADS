# BONUS - DESAFIO 2

print("-----Calculadora-----")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Escolha uma opção: "))

n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))

if opcao == 1:
    print("Resultado: ", n1 + n2)
elif opcao == 2:
    print("Resultado: ", n1 - n2)
elif opcao == 3:
    print("Resultado: ", n1 * n2)
elif opcao == 4:
    if n1 != 0 and n2 != 0:
        print("Resultado: ", n1 / n2)
    else:
        print("Erro: Divisão por zero não permitida.")
else:
    print("Opção inválida!")

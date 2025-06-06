# 1) Escreva um algoritmo que receba 5 números, armazene em um vetor, imprima na tela os valores, ordene esses
# valores do maior para o menor e por fim reimprima os valores do vetor ordenados.

print("-------------- Algoritmo ----------")
N1 = int(input("Digite o primeiro numero: "))
N2 = int(input("Digite o segundo numero: "))
N3 = int(input("Digite o terceiro numero: "))
N4 = int(input("Digite o quarto numero: "))
N5 = int(input("Digite o quinto numero: "))

lista = [N1, N2, N3, N4, N5]
print("Vetor inicial:", lista)
lista.sort(reverse=True) 
print("Vetor ordenado:", lista)


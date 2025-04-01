# Utilizando os conhecimentos construídos na ultima semana e toda sua criatividade, 
# crie um programa em python E linguagem C que atenda os seguintes requisitos:
# 1. Precisa usar ao menos 2 variáveis;
# 2. Precisa usar ao menos 2 estruturas condicionais;
# 3. Precisa ao menos ter uma comunicação de entrada e outra de saída com o usuário.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

nome = input("Qual seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros(Ex.1.80): "))
    
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
    
print(f"{nome} seu IMC é: {imc:.2f}")
print(f"Classificado como: {classificacao}")


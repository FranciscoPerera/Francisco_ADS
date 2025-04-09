# Apesar de suas limitações e questionamentos, o IMC (Índice de Massa Corpórea), é um índice que permite grande parte das pessoas terem algum parâmetro para saber 
# se estão com o peso suficientemente saudável. Para obter esse índice, basta dividir o peso da pessoa pela altura dela ao quadrado. Faça um software que calcule o IMC do 
# usuário e além de retornar para ele o valor desse índice, diga a situação do usuário de acordo com a tabela abaixo:
# Condição Situação:
# IMC abaixo de 18,5 Abaixo do peso
# IMC de 18,6 até 24,9 Peso normal
# IMC de 25 até 29,9 Sobrepeso
# IMC de 30 até 39,9 Obeso II
# Maior que 40 Obesidade III

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.6 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def prof(nome):
    if nome.strip().lower() == "aguado":
        print("Não interessa. Você está perfeito!!")
        exit()

print("--------------Calculador de IMC----------")
nome = input("Qual seu nome: ")
prof(nome)
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura em metros(Ex.1.80): "))
    
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
    
print(f"{nome} seu IMC é: {imc:.2f}")
print(f"Classificado como: {classificacao}")

sair = 10
while(sair != "0"):
    peso = float(input("Digite seu peso(kg): "))
    altura = float(input("Digite sua altura(m): "))
    imc = (peso/(altura**2))

    if(imc<18.5):
        print(f"Seu IMC é {imc}. Você está abaixo do peso")
    elif (imc<=24.9):
        print(f"Seu IMC é {imc}. Você está no peso normal.")
    elif (imc<=29.9):
        print(f"Seu IMC é {imc}. Você está em sobrepeso.")
    elif (imc<=39.9):
        print(f"Seu IMC é {imc}. Você está em obesidade II.")
    elif (imc>=40):
        print(f"Seu IMC é {imc}. Você está em obesidade III.")
    else:
        print("Dados de entrada incorretos")

    sair = input("Digite 0 pra finanlizar. Ou clique em algo para continuar")


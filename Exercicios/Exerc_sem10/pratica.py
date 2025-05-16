# Lista sobre algoritmos

lista = []
sair = ""

while sair != "0":
    print("-------------- Algoritmos Em Redes Sociais ----------")
    
    empresa = input("Digite uma empresa que usa algoritmos para te atrair: ")
    dono_empresa = input("Quem é o dono dessa empresa? ")
    gosta = input("Você gosta dessa empresa? ")

    algoritmos = {
        "Empresa": empresa,
        "DonoEmpresa": dono_empresa,
        "VoceGosta": gosta
    }

    lista.append(algoritmos)
    sair = input("Digite 0 para finalizar ou qualquer outra tecla para continuar: ")

print("\n---------- Lista final: ---------------")
for item in lista:
    print(item)

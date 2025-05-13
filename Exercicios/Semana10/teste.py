# Lista sobre algoritmos

lista = []
sair = 1
while(sair != "0"):
    print("-------------- Algoritmos Em Redes Sociais ----------")
    
    empresas = input("Digite empresas que usam algoritmos para te atarir: ")
    algoritmos.append(empresas)
    dono_empresa = input("Quem é o dono dessa empresa: ")
    algoritmos.append(dono_empresa)
    gosta = input("Voce gosta dessa empresa: ")
    algoritmos.append(gosta)

    algoritmos = {
    "Empresa": empresas,
    "DonoEmpresa": dono_empresa,
    "VoceGosta": gosta
    }

    lista.append(algoritmos)
    sair = input("Digite 0 pra finanlizar. Ou clique em algo para continuar. ")
else:
    print("Saindo...")
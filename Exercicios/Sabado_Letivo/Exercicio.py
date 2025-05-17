# Na segunda-feira vocês fizeram um programa que recebia um conjunto de dados do usuário, armazenava em uma lista de dicionário e depois imprimia na tela os valores.
# Pois bem, agora você irá adicionar uma funcionalidade que permite ao usuário, caso queira, excluir o item que desejar da lista criada!
# Faça a postagem do código na atividade. Essa postagem será equivalente a presença na aula desse sábado, dia 17.

lista = []
sair = ""

while sair != "0":
    print("-------------- Algoritmos Nas Redes Sociais ----------")
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

from datetime import datetime
import pytz  # Biblioteca para lidar com fusos horários

# Configuração do fuso horário
fuso_horario = pytz.timezone("America/Sao_Paulo")  # Ajuste para o fuso horário correto

# Tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Tabela de Registros dos ponto (Entrada, Saida intervalo, Retorno Intervalo e Saida)
registros_ponto = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

# Função que adicionar o ponto na lista de registros do funcionário
def adiciona_ponto(cod, tipo):
    agora = datetime.now(fuso_horario)  # Obtém a data e hora no fuso horário configurado
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))

# Função que verificar o usuário
def verifica_usuario(cod):
    return codigo.get(cod, None)

print("-----------------Folha Ponto------------------")
usuario = None
while usuario is None:
    cod = input("Qual seu código: ")
    usuario = verifica_usuario(cod)
    if usuario is None:
        print("Usuário inexistente!! Tente novamente.")

print(f"Bem-vindo(a), {usuario}!")
print("--------------Registre seu ponto--------------")
print("1) Entrada")
print("2) Saída intervalo")
print("3) Retorno intervalo")
print("4) Saída")

while True:
    resposta = input("Registrar (1-4) ou 'sair' para encerrar: ").strip()
    
    if resposta.lower() == 'sair':
        print("Encerrando o registro de ponto !")
        break

    if resposta in ["1", "2", "3", "4"]:
        tipos = {
            "1": "Entrada",
            "2": "Saída intervalo",
            "3": "Retorno intervalo",
            "4": "Saída"
        }
        tipo = tipos[resposta]
        adiciona_ponto(cod, tipo)
        agora = datetime.now(fuso_horario)
        print(f"Ponto registrado: {tipo} às {agora.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Opção inválida! Tente novamente.")
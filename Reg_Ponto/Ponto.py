from datetime import datetime # Biblioteca para lidar com datas e horas
import pytz  # Biblioteca para lidar com fusos horários 

# Configura para o fuso horário do Brasil (São Paulo)
fuso_horario = pytz.timezone("America/Sao_Paulo")  

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

# Função para adicionar o ponto na lista de registros do funcionário
def adicionar_ponto(cod, tipo):
    agora = datetime.now(fuso_horario) # informa a data e hora configurada
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S"))) # formata a data e hora

# Função para ver os registros do funcionário
def ver_registros(cod):
    print("\n---------- Seus Registros de Ponto ----------")
    if registros_ponto[cod]: # Verifica se tem registros do funcionário
        for tipo, horario in registros_ponto[cod]: # Percorre cada registro (tipo e horário) da tabela registros_ponto 
            print(f"{tipo}: {horario}") 
    else:
        print("Nenhum ponto registrado ainda !")
    print("---------------------------------------------\n")

# Função para verificar o usuário
def verificar_usuario(cod):
    return codigo.get(cod, None) # verifica se o cod existe na tabela funcionários

print("-----------------Folha Ponto------------------")
usuario = None
while usuario is None: 
    cod = input("Qual seu código: ")
    usuario = verificar_usuario(cod)
    if usuario is None: 
        print("Usuário inexistente!! Tente novamente.")

print(f"Bem-vindo(a), {usuario}!")
print("--------------Registre seu ponto--------------")
print("1) Entrada")
print("2) Saída intervalo")
print("3) Retorno intervalo")
print("4) Saída")
print("5) Ver registros")

while True:
    resposta = input("Opção (1-5) ou 'sair' para encerrar: ").strip() # strip() remove espaços em branco 
    
    if resposta.lower() == 'sair': # lower() converte a string para minúscula ou maiúscula
        print("Encerrando o registro de ponto !")
        break

    if resposta in ["1", "2", "3", "4"]: # Verifica se a resposta está entre as opções
        tipos = {
            "1": "Entrada",
            "2": "Saída intervalo",
            "3": "Retorno intervalo",
            "4": "Saída"
        }
        tipo = tipos[resposta] # Atribui o tipo de ponto com base na resposta
        adicionar_ponto(cod, tipo) # Adiciona o ponto na lista de registros do funcionário
        agora = datetime.now(fuso_horario) # informa a data e hora configurada
        print(f"Ponto registrado: {tipo} às {agora.strftime('%d/%m/%Y %H:%M:%S')}") # formata a data e hora
    elif resposta == "5":
        ver_registros(cod) # Exibe os registros do funcionário
    else:
        print("Opção inválida! Tente novamente.")
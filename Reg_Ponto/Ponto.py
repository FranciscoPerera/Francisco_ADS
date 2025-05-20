from datetime import datetime # Biblioteca para lidar com datas e horas
import pytz  # Biblioteca para lidar com fusos horários 

# Configura para o fuso horário do Brasil (São Paulo)
fuso_horario = pytz.timezone("America/Sao_Paulo")  

# Tabela de funcionários
codigo_turma = {
    "01": "Eu",
    "3096629": "Amanda", 
    "3095169": "Andre",
    "3095479": "Brendo",
    "3095321": "Caio",
    "3102564": "Carlos", 
    "3096866": "Davi",
    "3103234": "Enrico",
    "3096998": "Felipe",
    "3096556": "Francisco", 
    "3096726": "Guilherme",
    "3098184": "Joey",
    "3095126": "Marcelo",
    "309670X": "Matheus",
    "3096807": "Mauricio",
    "3102645": "Pietra",
    "3095568": "Renan",
    "3096611": "Roger",
    "3102653": "Vinicuis"
}

# Tabela de Registros dos ponto (Entrada, Saida intervalo, Retorno Intervalo e Saida)
registros_ponto = {
    "01": [],
    "3096629": [],
    "3095169": [],
    "3095479": [],
    "3095321": [],
    "3102564": [],
    "3096866": [],
    "3103234": [],
    "3096998": [],
    "3096556": [],
    "3096726": [],
    "3098184": [],
    "3095126": [],
    "309670X": [],
    "3096807": [],
    "3102645": [],
    "3095568": [],
    "3096611": [],
    "3102653": []
}

# Função para adicionar o ponto na lista de registros do funcionário
def adicionar_ponto(cod, tipo):
    agora = datetime.now(fuso_horario) # informa a data e hora configurada
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S"))) # formata a data e hora

# Função para ver os registros do funcionário
def ver_registros(cod):
    print(f"\n---------- Registros de {usuario} ----------")
    if registros_ponto[cod]: # Verifica se tem registros do funcionário
        for tipo, horario in registros_ponto[cod]: # Percorre cada registro (tipo e horário) da tabela registros_ponto 
            print(f"{tipo}: {horario}") 
    else:
        print("Nenhum ponto registrado ainda !")
    print("---------------------------------------------\n")

# Função para verificar o usuário
def verificar_usuario(cod):
    return codigo_turma.get(cod, None) # verifica se o cod existe na tabela funcionários

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
            "1": "✅ Entrada",
            "2": "⏸️ Saída intervalo",
            "3": "🔁 Retorno intervalo",
            "4": "❌ Saída"
        }
        tipo = tipos[resposta] # Atribui o tipo de ponto com base na resposta
        adicionar_ponto(cod, tipo) # Adiciona o ponto na lista de registros do funcionário
        agora = datetime.now(fuso_horario) # informa a data e hora configurada
        print(f"Ponto registrado: {tipo} às {agora.strftime('%d/%m/%Y %H:%M:%S')}") # formata a data e hora
    elif resposta == "5":
        ver_registros(cod) # Exibe os registros do funcionário
    else:
        print("Opção inválida! Tente novamente.")

from datetime import datetime # Biblioteca para lidar com datas e horas
import pytz  # Biblioteca para lidar com fusos horários 

# Configura para o fuso horário do Brasil
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Tabela de funcionários
codigo_turma = {
    "01": "Aguado",
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

# Função para dar cor as palavras no terminal
def cor(texto, cor):
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "negrito": "\033[1m",
        "reset": "\033[0m"
    }
    return f"{cores.get(cor, '')}{texto}{cores['reset']}" # Retorna o texto com a cor, depois encerra o código (reset), voltando a cor normal

# Função para adicionar o ponto na lista de registros do funcionário
def adicionar_ponto(cod, tipo):
    try:
        agora = datetime.now(fuso_horario) # informa a data e hora configurada
        registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S"))) # formata a data e hora
    except Exception as e:
        print(cor(f"❌  Erro ao registrar ponto: {e}", "vermelho"))

# Função para ver os registros do funcionário
def ver_registros(cod):
    print(cor(f"\n📋 REGISTROS DE {usuario.upper()}", "negrito"))
    if registros_ponto[cod]: # Verifica se tem registros do funcionário
        for tipo, horario in registros_ponto[cod]: # Percorre cada registro (tipo e horário) da tabela registros_ponto 
            print(cor(f"\033[1m {tipo} \033[0m: {horario}", "negrito")) # Deixa o tipo do registro em negrito e depois da um reset, para o resto
    else:
        print(cor("⚠️  Nenhum ponto registrado ainda!", "amarelo"))
    print("---------------------------------------------\n")
        
# Função para verificar o usuário
def verificar_usuario(cod):
    return codigo_turma.get(cod, None) # verifica se o cod existe na tabela funcionários

print(cor("💼  BEM-VINDO AO SISTEMA DE FOLHA DE PONTO", "negrito"))
usuario = None
while usuario is None: 
    cod = input("🔐  Qual seu CV: ")
    usuario = verificar_usuario(cod)
    if usuario is None: 
        print(cor("🚫  Usuário inexistente!! Tente novamente.", "vermelho"))

print(cor(f"\n👋  Bem Vindo(a),\033[1m{usuario}!\033[0m", "negrito")) # Deixa o usuario em negrito e depois da um reset, para o resto
print(cor("📲  Escolha uma opção para registrar seu ponto:", "negrito"))
print("1) Entrada")
print("2) Saída intervalo")
print("3) Retorno intervalo")
print("4) Saída")
print("5) Ver registros")

while True:
    resposta = input("👉  Opção (1-5) ou 'sair' para encerrar: ").strip() # strip remove espaços em branco 
    
    if resposta.lower() == 'sair':
        print("👋  Até logo! Encerrando o registro de ponto !")
        break

    if resposta in ["1", "2", "3", "4"]: # Verifica se a resposta está entre as opções
        tipos = {
            "1": "✅  Entrada",
            "2": "⏸️   Saída intervalo",
            "3": "🔁  Retorno intervalo",
            "4": "❌  Saída"
        }
        tipo = tipos[resposta] # Atribui o tipo de ponto com base na resposta
        adicionar_ponto(cod, tipo) # Adiciona o ponto na lista de registros do funcionário
        agora = datetime.now(fuso_horario) # informa a data e hora configurada
        print(cor(f"🕒  Ponto registrado: {tipo} às {agora.strftime('%d/%m/%Y %H:%M:%S')}\n", "verde"))
    elif resposta == "5":
        ver_registros(cod) # Exibe os registros do funcionário
    else:
        print(cor("⚠️  Opção inválida! Digite um número de 1 a 5 ou 'sair'.\n", "amarelo"))

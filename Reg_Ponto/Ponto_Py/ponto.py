from datetime import datetime

# Cria a tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Tabela para armazenar os registros de ponto
registros = {cod: [] for cod in codigo.keys()}

# Função para verificar o usuário
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
resposta = input("Registrar: ")

# Adiciona o registro na tabela com horários automáticos
hora_atual = datetime.now().strftime("%H:%M")
if resposta == "1":
    registros[cod].append({"entrada": hora_atual, "saida_intervalo": "", "retorno_intervalo": "", "saida": ""})
elif resposta == "2":
    registros[cod].append({"entrada": "", "saida_intervalo": hora_atual, "retorno_intervalo": "", "saida": ""})
elif resposta == "3":
    registros[cod].append({"entrada": "", "saida_intervalo": "", "retorno_intervalo": hora_atual, "saida": ""})
elif resposta == "4":
    registros[cod].append({"entrada": "", "saida_intervalo": "", "retorno_intervalo": "", "saida": hora_atual})

("Registros atualizados:", registros)
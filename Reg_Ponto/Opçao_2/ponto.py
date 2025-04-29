# Cria a tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Cria a tabela de Registros de ponto
registros = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

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


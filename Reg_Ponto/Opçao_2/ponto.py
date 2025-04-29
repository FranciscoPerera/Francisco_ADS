# Cria a tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Função para verificar o usuário
def verifica_usuario(cod):
    resultado = codigo.count(cod)
    if resultado:
        return resultado[0]
    else:
        return None

print("-----------------Folha Ponto------------------")
usuario = None
while not codigo:
    cod = input("Qual seu código: ")
    codigo = verifica_usuario(cod)
    if not usuario:
        print("Usuário inexistente!! Tente novamente.")

print("--------------Registre seu ponto--------------")
print("1) Entrada")
print("2) Saída intervalo")
print("3) Retorno intervalo")
print("4) Saída")
respostas = input("Registrar: ")



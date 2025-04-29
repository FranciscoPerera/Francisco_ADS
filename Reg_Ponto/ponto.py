# Abaixar a extençao sqlite para visualizar a tabela
import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect("Reg_Ponto/ponto.db")
cursor = conn.cursor()

# Cria a tabela de funcionários
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    codigo TEXT PRIMARY KEY,
    nome TEXT NOT NULL
)
""")

# Cria a tabela de registros
cursor.execute("""
CREATE TABLE IF NOT EXISTS registros (
    entrada TEXT PRIMARY KEY,
    saida_int TEXT NOT NULL,
    retorno_int TEXT NOT NULL,
    saida TEXT NOT NULL
)
""")

# Funcionários da empresa
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiz"
}

# Inseri os funcionarios da empresa no banco funcionarios
dados = list(codigo.items()) # Converte (chave, valor) do dicionário em dados
cursor.executemany("INSERT OR IGNORE INTO funcionarios (codigo, nome) VALUES (?, ?)", dados)
conn.commit()

# Função para verificar o usuário
def verifica_usuario(cod):
    cursor.execute("SELECT nome FROM funcionarios WHERE codigo = ?", (cod,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return None

print("-----------------Folha Ponto------------------")
usuario = None
while not usuario:
    cod = input("Qual seu código: ")
    usuario = verifica_usuario(cod)
    if not usuario:
        print("Usuário inexistente!! Tente novamente.")

print("--------------Registre seu ponto--------------")
print("1) Entrada")
print("2) Saída intervalo")
print("3) Retorno intervalo")
print("4) Saída")
respostas = input("Registrar: ")

# Fechar conexão
conn.close()

import sqlite3
from datetime import datetime

def criar_banco():
    conn = sqlite3.connect("folha_ponto.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cod_usuario TEXT,
            tipo TEXT,
            horario TEXT,
            FOREIGN KEY (cod_usuario) REFERENCES usuarios (id)
        )
    """)
    
    conn.commit()
    conn.close()

def inserir_usuarios():
    usuarios = [
        ("01", "Francisco"),
        ("02", "Aguado"),
        ("03", "Carlos"),
        ("04", "Ana")
    ]
    
    conn = sqlite3.connect("folha_ponto.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO usuarios (id, nome) VALUES (?, ?)", usuarios)
    conn.commit()
    conn.close()

def obter_usuario(cod):
    conn = sqlite3.connect("folha_ponto.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM usuarios WHERE id = ?", (cod,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario[0] if usuario else None

def registrar_ponto(cod_usuario, tipo):
    conn = sqlite3.connect("folha_ponto.db")
    cursor = conn.cursor()
    horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO registros (cod_usuario, tipo, horario) VALUES (?, ?, ?)", (cod_usuario, tipo, horario))
    conn.commit()
    conn.close()
    print("Registro realizado com sucesso!")

def main():
    criar_banco()
    inserir_usuarios()
    while True:
        print("\nFolha Ponto: Registre seus horários!!")
        cod = input("Digite seu código: ")
        
        usuario = obter_usuario(cod)
        if usuario:
            print(f"Bem-vindo, {usuario}!")
        else:
            print("Código de usuário não encontrado!")
            continue
        
        print("1) Entrada")
        print("2) Saída intervalo")
        print("3) Retorno intervalo")
        print("4) Saída")
        print("5) Sair")
        
        opcoes = {"1": "Entrada", "2": "Saída intervalo", "3": "Retorno intervalo", "4": "Saída"}
        reg = input("Digite qual você deseja registrar: ")
        
        if reg in opcoes:
            registrar_ponto(cod, opcoes[reg])
        elif reg == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

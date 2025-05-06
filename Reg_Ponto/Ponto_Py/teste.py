import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz

# Fuso horário do Brasil
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Tabela de Registros de ponto
registros_ponto = {cod: [] for cod in codigo}

# Função para adicionar ponto
def adiciona_ponto(cod, tipo):
    agora = datetime.now(fuso_horario)
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))
    return agora.strftime("%d/%m/%Y %H:%M:%S")

# Função de login
def fazer_login():
    cod = entry_codigo.get()
    usuario = codigo.get(cod)

    if usuario:
        label_boas_vindas.config(text=f"Bem-vindo(a), {usuario}!")
        botoes_frame.pack(pady=10)
        entry_codigo.config(state='disabled')
        btn_login.config(state='disabled')
    else:
        messagebox.showerror("Erro", "Código inválido!")

# Função para registrar ponto
def registrar_ponto(tipo):
    cod = entry_codigo.get()
    hora = adiciona_ponto(cod, tipo)
    messagebox.showinfo("Registrado", f"{tipo} registrado às {hora}")

# Criar interface
janela = tk.Tk()
janela.title("Sistema de Ponto")
janela.geometry("300x400")

# Campo de entrada do código
tk.Label(janela, text="Digite seu código:").pack(pady=5)
entry_codigo = tk.Entry(janela)
entry_codigo.pack()

# Botão de login
btn_login = tk.Button(janela, text="Login", command=fazer_login)
btn_login.pack(pady=5)

# Mensagem de boas-vindas
label_boas_vindas = tk.Label(janela, text="", font=("Arial", 10, "bold"))
label_boas_vindas.pack(pady=10)

# Frame para os botões de ponto
botoes_frame = tk.Frame(janela)

btn_entrada = tk.Button(botoes_frame, text="Entrada", width=20, command=lambda: registrar_ponto("Entrada"))
btn_saida_i = tk.Button(botoes_frame, text="Saída Intervalo", width=20, command=lambda: registrar_ponto("Saída intervalo"))
btn_retorno = tk.Button(botoes_frame, text="Retorno Intervalo", width=20, command=lambda: registrar_ponto("Retorno intervalo"))
btn_saida = tk.Button(botoes_frame, text="Saída", width=20, command=lambda: registrar_ponto("Saída"))

btn_entrada.pack(pady=2)
btn_saida_i.pack(pady=2)
btn_retorno.pack(pady=2)
btn_saida.pack(pady=2)

janela.mainloop()

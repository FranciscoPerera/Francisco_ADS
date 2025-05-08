import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
import pytz

# Configura o fuso horário do Brasil (São Paulo)
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado",
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Tabela de registros de ponto
registros_ponto = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

# Função para adicionar ponto
def adicionar_ponto(tipo):
    cod = entry_codigo.get()
    if cod not in codigo:
        messagebox.showerror("Erro", "Código inválido!")
        return
    agora = datetime.now(fuso_horario)
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))
    messagebox.showinfo("Sucesso", f"{tipo} registrado com sucesso!")

# Função para ver registros
def ver_registros():
    cod = entry_codigo.get()
    if cod not in codigo:
        messagebox.showerror("Erro", "Código inválido!")
        return
    texto_registros.delete('1.0', tk.END)
    texto_registros.insert(tk.END, f"--- Registros de {codigo[cod]} ---\n")
    if registros_ponto[cod]:
        for tipo, horario in registros_ponto[cod]:
            texto_registros.insert(tk.END, f"{tipo}: {horario}\n")
    else:
        texto_registros.insert(tk.END, "Nenhum ponto registrado ainda.\n")

# Criando interface
janela = tk.Tk()
janela.title("Sistema de Ponto")
janela.geometry("400x500")
janela.resizable(False, False)

# Widgets
tk.Label(janela, text="Código do Funcionário:").pack(pady=5)
entry_codigo = tk.Entry(janela, width=10, justify='center')
entry_codigo.pack()

tk.Button(janela, text="Entrada", width=20, command=lambda: adicionar_ponto("Entrada")).pack(pady=5)
tk.Button(janela, text="Saída Intervalo", width=20, command=lambda: adicionar_ponto("Saída intervalo")).pack(pady=5)
tk.Button(janela, text="Retorno Intervalo", width=20, command=lambda: adicionar_ponto("Retorno intervalo")).pack(pady=5)
tk.Button(janela, text="Saída", width=20, command=lambda: adicionar_ponto("Saída")).pack(pady=5)
tk.Button(janela, text="Ver Registros", width=20, command=ver_registros).pack(pady=10)

texto_registros = scrolledtext.ScrolledText(janela, width=45, height=15)
texto_registros.pack(pady=10)

janela.mainloop()

import tkinter as tk  # Biblioteca para criar a interface gráfica
from tkinter import messagebox, scrolledtext  # Biblioteca para exibir mensagens
from datetime import datetime  # Biblioteca para lidar com datas e horas
import pytz  # Biblioteca para lidar com fusos horários 

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

# Tabela de Registros dos ponto (Entrada, Saida intervalo, Retorno Intervalo e Saida)
registros_ponto = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

# Função para adicionar o ponto na lista de registros do funcionário
def adicionar_ponto(tipo):
    cod = entry_codigo.get()  # Pega o código do funcionário  
    if cod not in codigo:  # Verifica se o código do funcionário é válido
        messagebox.showerror("Erro", "Código inválido!")  # Mostra a mensagem de erro se o código não for válido
        return
    agora = datetime.now(fuso_horario)  # informa a data e hora configurada
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))  # formata a data e hora
    messagebox.showinfo("Sucesso", f"{tipo} registrado com sucesso!")  # Mostra a mensagem de sucesso

# Função para ver os registros do funcionário
def ver_registros():
    cod = entry_codigo.get()  # Pega o código do funcionário 
    if cod not in codigo:  # Verifica se o código do funcionário é válido
        messagebox.showerror("Erro", "Código inválido!")  # Mostra a mensagem de erro se o código não for válido
        return
    texto_registros.delete('1.0', tk.END)  # Limpa o conteúdo atual da área de registros
    texto_registros.insert(tk.END, f"--- Registros de {codigo[cod]} ---\n")  # Exibe o nome do funcionário
    if registros_ponto[cod]: # Verifica se tem registros do funcionário
        for tipo, horario in registros_ponto[cod]:  # Para cada registro de ponto
            texto_registros.insert(tk.END, f"{tipo}: {horario}\n")  # Mostra o tipo e o horário do registro
    else:
        texto_registros.insert(tk.END, "Nenhum ponto registrado ainda.\n")  # Caso não haja registros, mostra a  mensagem

# Criando a janela
janela = tk.Tk()  # Cria a janela 
janela.title("Sistema de Ponto")  # Define o título da janela
janela.geometry("400x500")  # Define o tamanho da janela
janela.resizable(False, False)  # Impede que a janela seja redimensionada

# Componentes da interface gráfica
tk.Label(janela, text="Código do Funcionário:").pack(pady=5)  # Texto pedindp o código do funcionário
entry_codigo = tk.Entry(janela, width=15, justify='center')  # Caixa de entrada para o código do funcionário
entry_codigo.pack() # Adiciona a caixa à janela

# Botões de ponto
tk.Button(janela, text="✅ Entrada", width=20, bg="#00FF00", command=lambda: adicionar_ponto("Entrada")).pack(pady=5)
tk.Button(janela, text="⏸️ Saída Intervalo", width=20, bg="#F0E68C", command=lambda: adicionar_ponto("Saída intervalo")).pack(pady=5)
tk.Button(janela, text="🔁 Retorno Intervalo", width=20, bg="#00BFFF", command=lambda: adicionar_ponto("Retorno intervalo")).pack(pady=5)
tk.Button(janela, text="❌ Saída", width=20, bg="#DC143C", command=lambda: adicionar_ponto("Saída")).pack(pady=5)
tk.Button(janela, text="Ver Registros", width=20, bg="white", command=ver_registros).pack(pady=10)

# Área para ver os registros de ponto
texto_registros = scrolledtext.ScrolledText(janela, width=45, height=15)  # Cria uma área de texto para mostrar os registros
texto_registros.pack(pady=10) # Adiciona essa área à janela

# Inicia um loop, ate ser fechado
janela.mainloop()

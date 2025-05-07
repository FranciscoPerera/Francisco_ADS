import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz

# Fuso horário do Brasil
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Registros de ponto
registros_ponto = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

# Funções
def verifica_usuario(cod):
    return codigo.get(cod, None)

def adiciona_ponto(cod, tipo):
    agora = datetime.now(fuso_horario)
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))
    messagebox.showinfo("Ponto Registrado", f"{tipo} registrado às {agora.strftime('%H:%M:%S')}")

def exibe_registros(cod):
    if registros_ponto[cod]:
        texto = "\n".join([f"{tipo}: {hora}" for tipo, hora in registros_ponto[cod]])
    else:
        texto = "Nenhum ponto registrado ainda!"
    messagebox.showinfo("Registros de Ponto", texto)

# Interface gráfica
class FolhaPontoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Folha Ponto")
        self.cod_usuario = None

        self.frame_login = tk.Frame(root)
        self.frame_login.pack(pady=20)

        tk.Label(self.frame_login, text="Digite seu código:").pack()
        self.entry_codigo = tk.Entry(self.frame_login)
        self.entry_codigo.pack()

        self.btn_login = tk.Button(self.frame_login, text="Entrar", command=self.login)
        self.btn_login.pack(pady=5)

        self.frame_opcoes = tk.Frame(root)

    def login(self):
        cod = self.entry_codigo.get().strip()
        usuario = verifica_usuario(cod)
        if usuario:
            self.cod_usuario = cod
            self.usuario_nome = usuario
            messagebox.showinfo("Bem-vindo", f"Bem-vindo(a), {usuario}!")
            self.frame_login.pack_forget()
            self.tela_opcoes()
        else:
            messagebox.showerror("Erro", "Código inválido!")

    def tela_opcoes(self):
        self.frame_opcoes.pack(pady=10)

        tk.Label(self.frame_opcoes, text=f"Usuário: {self.usuario_nome}", font=("Arial", 12, "bold")).pack()

        botoes = [
            ("Entrada", "Entrada"),
            ("Saída intervalo", "Saída intervalo"),
            ("Retorno intervalo", "Retorno intervalo"),
            ("Saída", "Saída"),
            ("Ver Registros", "ver")
        ]

        for texto, tipo in botoes:
            action = lambda t=tipo: self.registrar_ou_mostrar(t)
            tk.Button(self.frame_opcoes, text=texto, width=20, command=action).pack(pady=3)

    def registrar_ou_mostrar(self, tipo):
        if tipo == "ver":
            exibe_registros(self.cod_usuario)
        else:
            adiciona_ponto(self.cod_usuario, tipo)

# Inicia o app
root = tk.Tk()
app = FolhaPontoApp(root)
root.mainloop()

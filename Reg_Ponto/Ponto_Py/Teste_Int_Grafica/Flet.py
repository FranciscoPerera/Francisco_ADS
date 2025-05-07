import flet as ft
from datetime import datetime
import pytz

# Fuso horário de São Paulo
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado", 
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Registros
registros_ponto = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

def main(page: ft.Page):
    page.title = "Folha de Ponto"
    page.window_width = 500
    page.window_height = 600
    page.scroll = ft.ScrollMode.AUTO

    # Elementos da interface
    cod_input = ft.TextField(label="Código do Funcionário", width=300)
    msg_text = ft.Text("", color="blue")
    registro_output = ft.Text("", selectable=True)
    
    btns = []

    usuario = {"nome": None, "codigo": None}

    def verifica_usuario(cod):
        return codigo.get(cod, None)

    def on_confirmar_click(e):
        cod = cod_input.value.strip()
        nome = verifica_usuario(cod)
        if nome:
            usuario["nome"] = nome
            usuario["codigo"] = cod
            msg_text.value = f"Bem-vindo(a), {nome}!"
            for b in btns:
                b.disabled = False
        else:
            msg_text.value = "Usuário inexistente!"
            for b in btns:
                b.disabled = True
        registro_output.value = ""
        page.update()

    def adiciona_ponto(tipo):
        agora = datetime.now(fuso_horario)
        registros_ponto[usuario["codigo"]].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))
        msg_text.value = f"Ponto registrado: {tipo} às {agora.strftime('%d/%m/%Y %H:%M:%S')}"
        page.update()

    def ver_registros(e):
        cod = usuario["codigo"]
        saida = f"\n----- Registros de {usuario['nome']} -----\n"
        if registros_ponto[cod]:
            for tipo, horario in registros_ponto[cod]:
                saida += f"{tipo}: {horario}\n"
        else:
            saida += "Nenhum ponto registrado ainda!"
        saida += "------------------------------------"
        registro_output.value = saida
        page.update()

    # Botões
    btn_entrada = ft.ElevatedButton("Entrada", on_click=lambda e: adiciona_ponto("Entrada"), disabled=True)
    btn_saida_int = ft.ElevatedButton("Saída intervalo", on_click=lambda e: adiciona_ponto("Saída intervalo"), disabled=True)
    btn_retorno = ft.ElevatedButton("Retorno intervalo", on_click=lambda e: adiciona_ponto("Retorno intervalo"), disabled=True)
    btn_saida = ft.ElevatedButton("Saída", on_click=lambda e: adiciona_ponto("Saída"), disabled=True)
    btn_ver = ft.ElevatedButton("Ver registros", on_click=ver_registros, disabled=True)

    btns.extend([btn_entrada, btn_saida_int, btn_retorno, btn_saida, btn_ver])

    # Layout
    page.add(
        ft.Text("Folha de Ponto", size=30, weight="bold"),
        cod_input,
        ft.ElevatedButton("Confirmar", on_click=on_confirmar_click),
        msg_text,
        ft.Column(btns, spacing=10),
        ft.Divider(),
        registro_output
    )

ft.app(target=main)

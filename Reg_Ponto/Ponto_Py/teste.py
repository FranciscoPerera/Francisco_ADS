import flet as ft
from datetime import datetime
import pytz

# Configuração do fuso horário
fuso_horario = pytz.timezone("America/Sao_Paulo")

# Tabela de funcionários
codigo = {
    "01": "Francisco",
    "02": "Aguado",
    "03": "Luiza",
    "04": "Gabriel",
    "05": "Ana"
}

# Tabela de Registros dos ponto (Entrada, Saída intervalo, Retorno Intervalo e Saída)
registros_ponto = {
    "01": [],
    "02": [],
    "03": [],
    "04": [],
    "05": []
}

# Função que adiciona o ponto na lista de registros do funcionário
def adiciona_ponto(cod, tipo):
    agora = datetime.now(fuso_horario)
    registros_ponto[cod].append((tipo, agora.strftime("%d/%m/%Y %H:%M:%S")))
    return f"Ponto registrado: {tipo} às {agora.strftime('%d/%m/%Y %H:%M:%S')}"

# Função principal da interface
def main(page: ft.Page):
    page.title = "Registro de Ponto"
    page.window_width = 600
    page.window_height = 600

    # Elementos da interface
    codigo_input = ft.TextField(label="Código do Funcionário", width=300)
    mensagem = ft.Text(value="", color="red")
    registro_mensagem = ft.Text(value="", color="green")
    botoes_ponto = ft.Column(visible=False)
    tabela_registros = ft.Text(value="", visible=False)

    def verificar_usuario(e):
        cod = codigo_input.value.strip()
        if cod in codigo:
            mensagem.value = f"Bem-vindo(a), {codigo[cod]}!"
            mensagem.color = "green"
            botoes_ponto.visible = True
        else:
            mensagem.value = "Usuário inexistente! Tente novamente."
            mensagem.color = "red"
            botoes_ponto.visible = False
        registro_mensagem.value = ""
        tabela_registros.visible = False
        page.update()

    def registrar_ponto(tipo):
        cod = codigo_input.value.strip()
        if cod in codigo:
            registro_mensagem.value = adiciona_ponto(cod, tipo)
            registro_mensagem.color = "green"
        else:
            registro_mensagem.value = "Erro ao registrar ponto. Código inválido."
            registro_mensagem.color = "red"
        tabela_registros.visible = False
        page.update()

    def exibir_tabela(e):
        cod = codigo_input.value.strip()
        if cod in registros_ponto and registros_ponto[cod]:
            tabela = "\n".join([f"{tipo}: {hora}" for tipo, hora in registros_ponto[cod]])
            tabela_registros.value = f"Registros de {codigo[cod]}:\n{tabela}"
            tabela_registros.color = "black"
        else:
            tabela_registros.value = "Nenhum registro encontrado para este funcionário."
            tabela_registros.color = "red"
        tabela_registros.visible = True
        page.update()

    # Botões para registrar ponto
    botoes_ponto.controls = [
        ft.ElevatedButton("Entrada", on_click=lambda e: registrar_ponto("Entrada")),
        ft.ElevatedButton("Saída intervalo", on_click=lambda e: registrar_ponto("Saída intervalo")),
        ft.ElevatedButton("Retorno intervalo", on_click=lambda e: registrar_ponto("Retorno intervalo")),
        ft.ElevatedButton("Saída", on_click=lambda e: registrar_ponto("Saída")),
        ft.ElevatedButton("Ver Registros", on_click=exibir_tabela),
    ]

    # Layout da página
    page.add(
        ft.Text("Registro de Ponto", size=24, weight="bold"),
        codigo_input,
        ft.ElevatedButton("Verificar Usuário", on_click=verificar_usuario),
        mensagem,
        botoes_ponto,
        registro_mensagem,
        tabela_registros,
    )

# Executa a aplicação
if __name__ == "__main__":
    ft.app(target=main)
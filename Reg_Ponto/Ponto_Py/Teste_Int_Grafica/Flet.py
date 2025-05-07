import flet as ft

def main(page: ft.Page):
    page.title = "Flet"

    texto = ft.Text("Olá, mundo!")
    
    botao = ft.ElevatedButton(
        text="Clique aqui",
        on_click=lambda e: texto.update("Você clicou!")
    )

    page.add(
        texto,
        botao
    )

ft.app(target=main)

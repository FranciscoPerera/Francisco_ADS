import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.theme_mode = "light"

    tarefas = ft.Column()

    def adicionar_tarefa(e):
        if campo_tarefa.value:
            nova_tarefa = ft.Checkbox(label=campo_tarefa.value)
            tarefas.controls.append(nova_tarefa)
            campo_tarefa.value = ""
            page.update()

    campo_tarefa = ft.TextField(label="Nova tarefa", expand=True, on_submit=adicionar_tarefa)
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)

    page.add(
        ft.Row([campo_tarefa, botao_adicionar]),
        tarefas
    )

ft.app(target=main)

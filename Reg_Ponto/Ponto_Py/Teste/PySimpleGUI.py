import PySimpleGUI as sg

layout = [
    [sg.Text("Olá, mundo!", key="-LABEL-")],
    [sg.Button("Clique aqui")]
]

window = sg.Window("PySimpleGUI", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Clique aqui":
        window["-LABEL-"].update("Você clicou!")

window.close()

# 2) Refaça os programas acima de forma que ele escreva uma mensagem dizendo quais dias e quais temperaturas medidas que estavam abaixo da média semanal.

import statistics

pesquisa = {
    "Domingo": 27,
    "Segunda": 30,
    "Terça": 27.6,
    "Quarta": 23.5,
    "Quinta": 29.3,
    "Sexta": 24,
    "Sábado": 21
}

media = statistics.mean(pesquisa.values())

print(f"A média semanal de temperatura foi: {media:.2f}°C")

print("Dias com temperaturas abaixo da média:")
for dia, temperatura in pesquisa.items():
    if temperatura < media:
        print(f"{dia}: {temperatura:.2f}°C")

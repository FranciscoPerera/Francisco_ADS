# 3) Refaça o programa anterior de forma que ao invés de considerar somente 1 semana, sejam armazenadas as temperaturas da semana 1, 2 e 3 do mês. 
# Dessa vez, peça para o usuário inserir os valores medidos em cada dia de cada semana.
import statistics

dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
semanas = []

for i in range(1, 4):
    semana = {}
    print(f"\nInsira as temperaturas da semana {i}:")
    for dia in dias_da_semana:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                semana[dia] = temp
                break
            except ValueError:
                print("Por favor, insira um número válido.")
    semanas.append(semana)

todas_temperaturas = []
for semana in semanas:
    todas_temperaturas.extend(semana.values())

media_geral = statistics.mean(todas_temperaturas)
print(f"\nA média geral de temperatura nas 3 semanas foi: {media_geral:.2f}°C")

print("\nDias com temperaturas abaixo da média:")
for i, semana in enumerate(semanas, 1):
    for dia, temperatura in semana.items():
        if temperatura < media_geral:
            print(f"Semana {i} - {dia}: {temperatura:.2f}°C")

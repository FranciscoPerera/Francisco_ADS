# 1) Um grupo da Licenciatura em Química coletou as temperaturas do campus Capivari nos 7 dias da semana passada.
# Domingo: 27 / Segunda: 30 / Terça: 27.6 / Quarta: 23.5 / Quinta: 29.3 / Sexta: 24 / Sábado: 21
# Utilizando vetores, faça um programa em linguagem C e outro em Python que retorne, após processar:
# A menor temperatura identificada foi ? e a maior temperatura foi ?

temperatura = [
    27,
    30,
    27.6,
    23.5,
    29.3,
    24,
    21
]

menor = min(temperatura) 
maior = max(temperatura)
print(f"A menor temperatura identificada foi: {menor}")
print(f"A maior temperatura identificada foi: {maior}")


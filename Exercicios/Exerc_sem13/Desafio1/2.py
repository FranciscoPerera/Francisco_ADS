# 2) Crie um programa que faça o que o software TERMO faz, ou seja, um jogo de adivinhação de letras e palavras.

palavra = "piano"

print("Bem-vindo ao jogo TERMO!")
print("Adivinhe a palavra de 5 letras. Você tem 6 tentativas.\n")

# Repetir até 6 tentativas
for tentativa in range(1, 7):
    palpite = input(f"Tentativa {tentativa}: ")

    # Verifica se acertou
    if palpite == palavra:
        print("Parabéns! Você acertou a palavra!")
        break

    # Mostrar dica para cada letra
    print("Dica:")
    for i in range(5):
        letra = palpite[i]
        if letra == palavra[i]:
            print(f"{letra} - certa e no lugar certo")
        elif letra in palavra:
            print(f"{letra} - certa, mas no lugar errado")
        else:
            print(f"{letra} - não está na palavra")
    print()

# Se não acertou 
if palpite != palavra:
    print(f"Você perdeu! A palavra correta era: {palavra}")

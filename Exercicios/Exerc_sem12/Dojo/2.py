# Refaça esse programa de forma que você peça para o usuário que ele digite uma palavra. 
# Você irá substituir cada letra da palavra pela próxima letra do alfabeto e imprimir a palavra com essas substituições. 
# Essa substituição deverão ser feitas através de uma função chamada troca().

alfabeto = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def troca(palavra):
    nova = ""
    for letra in palavra:  # Percorre a palavra original
        for i in range(len(alfabeto)):  # Percorre o alfabeto para achar a letra
            if letra == alfabeto[i]:  # Achar a letra
                if i == 25:
                    nova += alfabeto[0]  # Se letra for'z', Volta para a letra 'a'
                else:
                    nova += alfabeto[i + 1]  # Senao pega a próxima letra
                break
    return nova

palavra = input("Digite uma palavra: ").lower()
print("Palavra nova é:",troca(palavra))

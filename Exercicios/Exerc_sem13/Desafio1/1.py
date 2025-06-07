# Existe um problema no nosso código. A letra Z, por exemplo, não tem substituta na criptografia. 

# Em Python, crie uma lista que contenha todas as letras do alfabeto, de forma ordenada. Ao final, percorra a lista com um laço de repetição, imprimindo as letras;
alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u', 'v','w','x','y','z']

def troca(pl):
    cripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = (i + 1) % len(alfabeto)  # Volta pro início 
        cripto.append(alfabeto[i])
    return cripto
        

#Pedir usuario uma palavra
palavra = input("Digite uma palavra: ").lower()
lista = troca(palavra)
print(lista)
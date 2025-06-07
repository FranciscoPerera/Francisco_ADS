import tkinter as tk
from tkinter import messagebox

alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u', 'v','w','x','y','z']

def troca():
    pl = palavra.get().lower()
    cripto = []
    for letra in pl:
        if letra in alfabeto:
            i = alfabeto.index(letra)
            i = (i + 1) % len(alfabeto)
            cripto.append(alfabeto[i])
        else:
            cripto.append(letra)  
    resultado.config(text=''.join(cripto))

# Cria a janela principal
janela = tk.Tk()
janela.title("Muda Palavras !!")
janela.geometry("300x200")
        
# Cria e Adiciona os componentes
entrada_palavra = tk.Label(janela, text="Digite uma palavra: ", font="Arial")
entrada_palavra.pack(pady=5)

palavra = tk.Entry(janela, font="Arial")
palavra.pack(pady=5)

bt = tk.Button(janela, text="Mudar!", width=10, command=troca)
bt.pack(pady=5)

resultado = tk.Label(janela, text="", font="Arial")
resultado.pack(pady=5)

# Inicia a interface
janela.mainloop()

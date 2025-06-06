import tkinter as tk

def soma():
    valor1 = float(s1.get())
    valor2 = float(s2.get())
    valor3 = float(s3.get())
    total = valor1 + valor2 + valor3
    resultado.config(text=f"{nome.get()}, neste ano você recebeu R$ {total:.2f}")
    if(total <= 15000):
        resultado2.config(text=f"Até agora você está isento de pagar imposto de renda!")
    
# Cria a janela principal
janela = tk.Tk()
janela.title("Imposto de Renda")
janela.geometry("400x400")

# Cria os componentes
entrada_nome = tk.Label(janela, text="Digite seu nome: ", font="Arial")
nome = tk.Entry(janela, font="Arial")

entrada_s1 = tk.Label(janela, text="Digite seu primeiro salário: ", font="Arial")
s1 = tk.Entry(janela, font="Arial")

entrada_s2 = tk.Label(janela, text="Digite seu segundo salário: ", font="Arial")
s2 = tk.Entry(janela, font="Arial")

entrada_s3 = tk.Label(janela, text="Digite seu terceiro salário: ", font="Arial")
s3 = tk.Entry(janela, font="Arial")

bt = tk.Button(janela, text="Descobrir!", width=10, command=soma)
resultado = tk.Label(janela, text="", font="Arial")

resultado2 = tk.Label(janela, text="", font="Arial")


# Adiciona os componentes à janela
entrada_nome.pack(pady=5)
nome.pack(pady=5)
entrada_s1.pack(pady=5)
s1.pack(pady=5)
entrada_s2.pack(pady=5)
s2.pack(pady=5)
entrada_s3.pack(pady=5)
s3.pack(pady=5)
bt.pack(pady=10)
resultado.pack(pady=10)
resultado2.pack(pady=10)

# Inicia a interface
janela.mainloop()


# Atividade_Desafio
# Escolha um assunto de seu interesse e elabore uma questão de múltipla escolha sobre esse assunto. Ela precisará ter 4 alternativas de resposta, sendo somente 1 delas a correta.
# Faça um programa que a) mostre ao usuário essa pergunta e as opções de respostas, b) receba a resposta do usuário e c) escreva pra ele se ele acertou ou se ele errou! Se ele
# escreveu uma resposta diferente das 4 opções, escreva “Alternativa inválida!”

    
Lista_Perguntas = [
    "1 - Qual destas linguagens é usada para análise de dados e inteligência artificial?",
    "A) Java",
    "B) Python",
    "C) C",
    "D) JavaScript",
    
    "2 - Qual destas linguagens é usada para aplicativos mobile?",
    "A) Java",
    "B) Python",
    "C) C",
    "D) JavaScript",
    
    "3 - Qual destas linguagens é usada no maker?",
    "A) Java",
    "B) Python",
    "C) C",
    "D) JavaScript",
    
    "4 - Qual destas linguagens é usada para design web?",
    "A) Java",
    "B) Python",
    "C) C",
    "D) JavaScript"
]

respostas_corretas = ['B', 'A', 'C', 'D']  

def fazer_pergunta(indice):
    print(Lista_Perguntas[indice * 5])  
    print(Lista_Perguntas[indice * 5 + 1])  
    print(Lista_Perguntas[indice * 5 + 2])  
    print(Lista_Perguntas[indice * 5 + 3])  
    print(Lista_Perguntas[indice * 5 + 4]) 
    
    resposta = input("Escolha uma alternativa (A, B, C, D): ").upper()

    if resposta == respostas_corretas[indice]:
        print("Você acertou!")
    elif resposta in ['A', 'B', 'C', 'D']:
        print("Você errou!")
    else:
        print("Alternativa inválida!")

for i in range(4):
    fazer_pergunta(i)

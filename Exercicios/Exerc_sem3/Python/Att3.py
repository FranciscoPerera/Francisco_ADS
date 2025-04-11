# Atividade_Desafio
# Escolha um assunto de seu interesse e elabore uma questão de múltipla escolha sobre esse assunto. Ela precisará ter 4 alternativas de resposta, sendo somente 1 delas a correta.
# Faça um programa que a) mostre ao usuário essa pergunta e as opções de respostas, b) receba a resposta do usuário e c) escreva pra ele se ele acertou ou se ele errou! Se ele
# escreveu uma resposta diferente das 4 opções, escreva “Alternativa inválida!”

print("Qual destas linguagens é usada para análise de dados e inteligência artificial?")
print("A) Java")
print("B) Python")
print("C) C")
print("D) JavaScript")

resposta = input("Digite a resposta (De forma maiuscula): ")

if resposta == "B" or "b":
    print("Resposta correta! Python é usado para análise de dados e IA.")
elif resposta and ["A", "C", "D", "a", "b", "d"]:
    print("Resposta errada! A resposta correta é a letra B.")
else:
    print("Alternativa inválida!")

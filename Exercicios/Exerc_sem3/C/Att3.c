/* Atividade_Desafio */
/* Escolha um assunto de seu interesse e elabore uma questão de múltipla escolha sobre esse assunto. Ela precisará ter 4 alternativas de resposta, sendo somente 1 delas a correta.
Faça um programa que a) mostre ao usuário essa pergunta e as opções de respostas, b) receba a resposta do usuário e c) escreva pra ele se ele acertou ou se ele errou! Se ele
escreveu uma resposta diferente das 4 opções, escreva “Alternativa inválida!” */


#include <stdio.h>
#include <ctype.h>

void main() {
    printf("Qual destas linguagens e usada para análise de dados e inteligência artificial?\n");
    printf("A) Java\n");
    printf("B) Python\n");
    printf("C) C\n");
    printf("D) JavaScript\n");

    char resposta;
    printf("Digite a letra correspondente a sua resposta: ");
    scanf(" %s", &resposta);
    resposta = toupper(resposta);

    if (resposta == 'B') {
        printf("Resposta correta! Python e usado para analise de dados e IA.\n");
    } else if (resposta == 'A' || resposta == 'C' || resposta == 'D') {
        printf("Resposta errada! A resposta correta e a letra B.\n");
    } else {
        printf("Alternativa invalida!\n");
    }

}

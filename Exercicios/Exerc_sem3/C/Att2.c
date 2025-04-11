/* Atividade_Desafio */
/* Faça um programa em Python que pergunte ao usuário: a) o nome de uma disciplina; b) a nota dele/a na disciplina e c) a quantidade de faltas na disciplina. Se sua nota for
inferior a 4 OU tiver mais que 20 faltas, escreva “Está reprovado/a”; Se sua nota estiver entre 4 e 6 e tiver menos que 20 faltas, escreva “Você está de IFA!”; Se sua nota for igual
ou maior que 6 e tiver menos que 20 faltas, escreva “Aprovado/a”! */


#include <stdio.h>

void main() {
    char disciplina[20];
    float nota;
    int faltas;

    printf("Digite o nome da disciplina: ");
    scanf("%s", disciplina);
    printf("Digite sua nota na disciplina: ");
    scanf("%f", &nota);
    printf("Digite a quantidade de faltas: ");
    scanf("%i", &faltas);

    if (nota < 4 || faltas > 20) {
        printf("Voce esta reprovado/a\n");
    } else if (nota >= 4 && nota < 6 && faltas <= 20) {
        printf("Voce esta de IFA!\n");
    } else if (nota >= 6 && faltas <= 20) {
        printf("Voce esta aprovado/a\n");
    }
}

/* Atividade(Slide) */
#include <stdio.h>

void main() {
    char nome[20];
    float s1, s2, s3, salario;

    printf("Qual seu nome? ");
    scanf("%s", &nome);

    printf("Qual seu salario de janeiro? ");
    scanf("%f", &s1);

    printf("Qual seu salario de fevereiro? ");
    scanf("%f", &s2);

    printf("Qual seu salario de marco? ");
    scanf("%f", &s3);

    salario = (s1 + s2 + s3);

    printf("%s Neste ano voce recebeu R$ %.2f", nome, salario);
}

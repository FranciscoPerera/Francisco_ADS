/* Atividade_Desafio */

#include <stdio.h>

int main() {
    char nome[20];
    float s1, s2, s3, salario;

    printf("Digite seu nome: ");
    scanf("%s", nome);

    printf("Qual seu salario de janeiro: ");
    scanf("%f", &s1);

    printf("Qual seu salario de fevereiro: ");
    scanf("%f", &s2);

    printf("Qual seu salario de março: ");
    scanf("%f", &s3);

    salario = s1 + s2 + s3;

    printf("%s, neste ano você recebeu R$ %.2f\n", nome, salario);

    if (salario <= 15000) {
        printf("Hey! Ate agora você esta isento de pagar Imposto de Renda!!!\n");
    }

}

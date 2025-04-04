/* Utilizando os conhecimentos construídos na ultima semana e toda sua criatividade, */
/* crie um programa em python E linguagem C que atenda os seguintes requisitos: */
/* 1. Precisa usar ao menos 2 variáveis; */
/* 2. Precisa usar ao menos 2 estruturas condicionais; */
/* 3. Precisa ao menos ter uma comunicação de entrada e outra de saída com o usuário. */

#include <stdio.h>

int main() {
    char nome[20];
    float peso, altura, imc;

    printf("Qual seu nome? ");
    scanf("%s", nome);

    printf("Qual seu peso em kg? ");
    scanf("%f", &peso);

    printf("Qual sua altura em cm? ");
    scanf("%f", &altura);

    altura = altura / 100;
    imc = peso / (altura * altura);

    printf("%s, seu IMC e %.2f.\n", nome, imc);

    if (imc < 18.5) {
        printf("Classificado como: Magreza\n");
    } else if (imc < 24.9) {
        printf("Classificado como: Normal\n");
    } else if (imc < 29.9) {
        printf("Classificado como: Sobrepeso\n");
    } else if (imc < 39.9) {
        printf("Classificado como: Obesidade\n");
    } else {
        printf("Classificado como: Obesidade Grave\n");
    }

}

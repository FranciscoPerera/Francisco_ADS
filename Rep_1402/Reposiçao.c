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
        printf("Classificado como: Abaixo do peso\n");
    } else if (imc < 24.9) {
        printf("Classificado como: Peso normal\n");
    } else if (imc < 29.9) {
        printf("Classificado como: Sobrepeso\n");
    } else if (imc < 34.9) {
        printf("Classificado como: Obesidade grau 1\n");
    } else if (imc < 39.9) {
        printf("Classificado como: Obesidade grau 2\n");
    } else {
        printf("Classificado como: Obesidade grau 3\n");
    }

}

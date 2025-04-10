// Apesar de suas limitações e questionamentos, o IMC (Índice de Massa Corpórea), é um índice que permite grande parte das pessoas terem algum parâmetro para saber 
// se estão com o peso suficientemente saudável. Para obter esse índice, basta dividir o peso da pessoa pela altura dela ao quadrado. Faça um software que calcule o IMC do 
// usuário e além de retornar para ele o valor desse índice, diga a situação do usuário de acordo com a tabela abaixo:
// Condição Situação:
// IMC abaixo de 18,5 Abaixo do peso
// IMC de 18,6 até 24,9 Peso normal
// IMC de 25 até 29,9 Sobrepeso
// IMC de 30 até 39,9 Obeso II
// Maior que 40 Obesidade III

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

// O banco do brasil está com uma campanha para incentivar as pessoas a usarem seu cartão de crédito. De acordo com o valor da fatura no mês, um certo percentual de
// cashback será creditado na conta corrente do usuário. Se o valor da fatura for de até R$1000,00, não haverá cashback. Faturas entre R$1000,00 e R$4000,00 terão
// cashback de 1%. Faturas entre R$4000,00 e R$8000,00 terão cashback de 2%. Faturas acima de R$8000,00 terão cashback de 5%. Faça um software em que o usuário
// informe o valor de sua fatura e você retornará na tela para ele, qual o valor de cashback que ele terá naquele mês.

#include <stdio.h>

float calcular_cashback(float valor) {
    if (valor <= 1000.0) {
        return 0;
    } else if (valor <= 4000.0) {
        return valor * 0.01;
    } else if (valor <= 8000.0) {
        return valor * 0.02;
    } else {
        return valor * 0.05;
    }
}

int main() {
    char nome[20];
    float valor, cashback;

    printf("------------Calculadora de cashback--------------\n");
    printf("Qual o seu nome: ");
    scanf("%s", nome);
    printf("Qual o valor de sua fatura: ");
    scanf("%f", &valor);

    cashback = calcular_cashback(valor);

    if (cashback > 0) {
        printf("%s, voce tera R$%.2f de cashback\n", nome, cashback);
    } else {
        printf("Nao havera cashback\n");
    }

}

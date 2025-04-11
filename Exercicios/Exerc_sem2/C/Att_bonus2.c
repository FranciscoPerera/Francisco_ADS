#include <stdio.h>

void main() {
    int opcao;
    float n1, n2;

    printf("-----Calculadora-----");
    printf("\n 1 - Soma");
    printf("\n 2 - Subtraçao");
    printf("\n 3 - Multiplicacao");
    printf("\n 4 - Divisao");
    printf("\n Escolha uma opcao: ");
    scanf("%d", &opcao);

    printf("Primeiro valor: ");
    scanf("%f", &n1);
    printf("Segundo valor: ");
    scanf("%f", &n2);

    if (opcao == 1) {
        printf("Resultado: %.2f", n1 + n2);
    }
    else if (opcao == 2) {
        printf("Resultado: %.2f", n1 - n2);
    }
    else if (opcao == 3) {
        printf("Resultado: %.2f", n1 * n2);
    }
    else if (opcao == 4) {
        if (n2 != 0) {
            printf("Resultado: %.2f", n1 / n2);
        } else {
            printf("Erro: Divisao por zero nao permitida.");
        }
    }
    else {
        printf("Opcao invalida!");
    }
}

/* 1) Escreva um algoritmo que receba 5 números, armazene em um vetor, imprima na tela os valores, ordene esses
valores do maior para o menor e por fim reimprima os valores do vetor ordenados. */

#include <stdio.h>

int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int main() {
    int N1, N2, N3, N4, N5;
    int lista[5];

    printf("-------------- Algoritmo ----------\n");
    printf("Digite o primeiro numero: ");
    scanf("%d", &N1);
    printf("Digite o segundo numero: ");
    scanf("%d", &N2);
    printf("Digite o terceiro numero: ");
    scanf("%d", &N3);
    printf("Digite o quarto numero: ");
    scanf("%d", &N4);
    printf("Digite o quinto numero: ");
    scanf("%d", &N5);

    lista[0] = N1;
    lista[1] = N2;
    lista[2] = N3;
    lista[3] = N4;
    lista[4] = N5;

    // Ordenando o vetor em ordem decrescente
    qsort(lista, 5, sizeof(int), compare);

    printf("Vetor ordenado do maior para o menor: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", lista[i]);
    }
    printf("\n");

}


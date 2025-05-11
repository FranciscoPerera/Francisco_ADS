/* 2) Refa�a os programas acima de forma que ele escreva uma mensagem dizendo quais dias e quais temperaturas medidas que estavam abaixo da m�dia semanal. */

#include <stdio.h>

int main() {
    float temperaturas[7] = {27.0, 30.0, 27.6, 23.5, 29.3, 24.0, 21.0};
    float soma = 0, media;

    // Cálculo da média
    for (int i = 0; i < 7; i++) {
        soma += temperaturas[i];
    }
    media = soma / 7;

    printf("Temperatura média da semana: %.2f C\n", media);
    printf("Dias com temperatura abaixo da média:\n");

    for (int i = 0; i < 7; i++) {
        if (temperaturas[i] < media) {
            printf("Dia %d: %.1f C\n", i + 1, temperaturas[i]);
        }
    }

    return 0;
}



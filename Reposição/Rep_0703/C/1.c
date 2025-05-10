/* 1) Um grupo da Licenciatura em Qu�mica coletou as temperaturas do campus Capivari nos 7 dias da semana passada.
Domingo: 27 / Segunda: 30 / Ter�a: 27.6 / Quarta: 23.5 / Quinta: 29.3 / Sexta: 24 / S�bado: 21
Utilizando vetores, fa�a um programa em linguagem C e outro em Python que retorne, ap�s processar:
A menor temperatura identificada foi ? e a maior temperatura foi ? */

#include <stdio.h>

int main() {
    float temperaturas[7] = {27.0, 30.0, 27.6, 23.5, 29.3, 24.0, 21.0};
    float menor = temperaturas[0], maior = temperaturas[0];

    for (int i = 1; i < 7; i++) {
        if (temperaturas[i] < menor) {
            menor = temperaturas[i];
        }
        if (temperaturas[i] > maior) {
            maior = temperaturas[i];
        }
    }

    printf("A menor temperatura identificada foi: %.1f C\n", menor);
    printf("A maior temperatura identificada foi: %.1f C\n", maior);

}


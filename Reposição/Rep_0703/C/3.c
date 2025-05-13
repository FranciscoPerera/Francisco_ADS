/* 3) Refaça o programa anterior de forma que ao invés de considerar somente 1 semana, sejam armazenadas as temperaturas da semana 1, 2 e 3 do mês.
Dessa vez, peça para o usuário inserir os valores medidos em cada dia de cada semana. */

#include <stdio.h>
#include <string.h>
#define SEMANAS 3
#define DIAS 7

int main() {
    char* dias_da_semana[DIAS] = {
        "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"
    };

    float temperaturas[SEMANAS][DIAS];
    float soma = 0.0;
    int total_dias = SEMANAS * DIAS;

    for (int semana = 0; semana < SEMANAS; semana++) {
        printf("\nInsira as temperaturas da semana %d:\n", semana + 1);
        for (int dia = 0; dia < DIAS; dia++) {
            printf("%s: ", dias_da_semana[dia]);
            while (scanf("%f", &temperaturas[semana][dia]) != 1) {
                printf("Entrada inválida. Digite novamente %s: ", dias_da_semana[dia]);
                while(getchar() != '\n');
            }
            soma += temperaturas[semana][dia];
        }
    }

    float media = soma / total_dias;
    printf("\nA média geral de temperatura nas 3 semanas foi: %.2f°C\n", media);

    printf("\nDias com temperaturas abaixo da média:\n");
    for (int semana = 0; semana < SEMANAS; semana++) {
        for (int dia = 0; dia < DIAS; dia++) {
            if (temperaturas[semana][dia] < media) {
                printf("Semana %d - %s: %.2f°C\n", semana + 1, dias_da_semana[dia], temperaturas[semana][dia]);
            }
        }
    }

    return 0;
}



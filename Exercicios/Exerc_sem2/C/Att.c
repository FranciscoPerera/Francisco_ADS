/* Atividade(Slide) */
#include <stdio.h>

void main() {
    char nome[20];
    char cidade[20];

    printf("Qual seu nome? ");
    scanf("%s", &nome);

    printf("Qual sua cidade? ");
    scanf("%s", &cidade);

    printf("Nobre %s de %s ! Nossa batalha pelo mundo da programaçao esta so comecando! O povo de %s se orgulhara de voce!", nome, cidade, cidade);
}

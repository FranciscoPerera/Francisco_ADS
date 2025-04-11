/* Atividade_Desafio */
/* Você sabia que um ano para ser bissexto, precisa ser múltiplo de 4? Sabendo disso,
faça um programa em Python que pergunte o ano de nascimento da pessoa e caso seja
bissexto, escreverá “Você nasceu em um ano bissexto!”. Caso esse ano não seja bissexto,
o programa escreverá “Você não nasceu em um ano bissexto!” */


#include <stdio.h>

void main() {
    int ano;
    printf("Digite o ano do seu nascimento: ");
    scanf("%i", &ano);
    if (ano % 4 == 0) {
        printf("Voce nasceu em um ano bissexto!\n");
    } else {
        printf("Voce não nasceu em um ano bissexto!\n");
    }
}

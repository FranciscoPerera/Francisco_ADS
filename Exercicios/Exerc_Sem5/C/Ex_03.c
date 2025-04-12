// O supermercado Delta está fazendo uma promoção. Se a pessoa for sócio do Clube Delta ou ela tiver mais de 60 anos, terá R$10,00 de desconto no valor total da compra. 
// Além disso, para os sócio do Clube Delta que estão fazendo aniversário naquele dia, haverá um desconto adicional de R$ 5,00. Esses descontos todos são validos 
// somente para compras acima de R$ 100,00. Faça o melhor software possível, que receba as informações necessárias do usuário e ao final diga o valor total da compra.

#include <stdio.h>
#include <string.h>

int main() {
    char socio[4], niver[4];
    int idade;
    float valor;

    printf("-------------Mercado Delta--------------\n");
    printf("Você é sócio do Clube Delta? (sim = 1|nao = 2): ");
    scanf("%s", socio);
    printf("Qual sua idade: ");
    scanf("%d", &idade);
    printf("Você faz aniversário hoje? (sim = 1|nao = 2): ");
    scanf("%s", niver);
    printf("Qual o valor de sua compra? R$ ");
    scanf("%f", &valor);

    if (valor < 100) {
        printf("Valor total da compra: R$%.2f\n", valor);
    } else {
        if (strcmp(socio, "1") == 0 && strcmp(niver, "1") == 0) {
            valor -= 15; 
        } else if (strcmp(socio, "1") == 0 || idade >= 60) {
            valor -= 10; 
        }
        printf("Valor total da compra: R$%.2f\n", valor);
    }

    return 0;
}

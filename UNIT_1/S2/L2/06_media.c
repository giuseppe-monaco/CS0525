#include <stdio.h>

int main()
{
    int a;
    int b;
    float media;

    printf("Inserisci due numeri e calcolerò la media.\n");

    printf("Digitare il primo numero: ");
    scanf("%d", &a);

    printf("Digitare il secondo numero: ");
    scanf("%d", &b);

    media = (a + b) / 2.0;

            printf("La media dei due numeri è: %.2f\n", media);

    return 0;
} 
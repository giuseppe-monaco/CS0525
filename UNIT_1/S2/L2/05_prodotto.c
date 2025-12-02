#include <stdio.h>

int main()
{
    int a;
    int b;
    int prodotto;

    printf("Inserisci il primo numero: ");
    scanf("%d", &a);
    /* 
    %d variabile per un numero intero
    la & serve per ricordare dove si trova l'indirizzo della scatola
    */
    printf("Inserisci il secondo numero: ");
    scanf("%d", &b);

    prodotto = a * b;

    printf("Il prodotto è: %d", prodotto);
    return 0;
}
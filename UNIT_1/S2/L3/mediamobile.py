def media_mobile(lista, finestra):
    risultato = [] #qui creo la lista vuota in cui si salveranno tutte le medie calcolate col for

    # Questo "for" è un ciclo che scorre ogni posizione della lista
    for posizione in range(len(lista)):
        if posizione < finestra - 1: #cosi utilizzo anche i valori non ancora "disponibili" della finestra 
            media = sum(lista[:posizione + 1]) / (posizione + 1)
        else:
            # per le posizioni successive uso gli ultimi n valori
            media = sum(lista[posizione - finestra + 1 : posizione + 1]) / finestra

        risultato.append(media)

    return risultato

# chiedi i numeri da inserire
lista = []
tot_numeri = int(input("Quanti numeri vuoi inserire? "))

for indice in range(tot_numeri):
    numero = float(input(f"Inserisci il numero {indice+1}: "))
    lista.append(numero)

# chiedi il valore della finestra
finestra = int(input("Inserisci il numero di cifre per la finestra di media mobile: "))

#   CALCOLO E RISULTATO
risultato = media_mobile(lista, finestra)

print("\nLista originale: ", lista)
print("Media mobile:    ", risultato)
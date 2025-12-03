import re

def conteggio_parole(testo):
    # Trasformiamo tutto in minuscolo
    testo = testo.lower()
    # Rimuoviamo la punteggiatura
    testo = re.sub(r'[^a-z0-9\s]', '', testo) 
    #spiegazione regex: la regex si imposta cosi re.sub(pattern, replacement, string)
    # PATTERN:^ significa negazione. Sto togliendo OGNI carattere che NON è elencato
    #dentro il pattern abbiamo tutte le minuscole dalla a alla z, tutte le cifre da 0 a 9 e qualsiasi carattere di spazio \s
    #REPLACEMENT vuoto
    #string = test = la stringa su cui lavoriamo

    # Dividiamo il testo in parole
    parole = testo.split()
    # Contiamo le occorrenze
    dizionario = {}
    for parola in parole:
        if parola in dizionario:
            dizionario[parola] += 1
        else:
            dizionario[parola] = 1
    return dizionario

#per provarla
testo = input("Inserisci un testo: ")
conteggio = conteggio_parole(testo)
print("\nConteggio parole:", conteggio)
def perimetro():
    print("Questo programma calcola il perimetro di una data figura geometrica")
    print("Quadrato - 1")
    print("Rettangolo - 2")
    print("Cerchio - 3")

    print("Digitare il numero corrispondente alla propria scelta: ")
    scelta = int(input(">>> "))
    if scelta == 1:
        print("Hai selezionato il quadrato!")
        lato =float(input("Inserisci il valore del lato del quadrato: "))
        perimetroq=float(lato*4)
        return perimetroq, scelta
    elif scelta == 2:
        print("Hai selezionato il perimetro del rettangolo")
        base = float(input("Inserisci il valore della base: "))
        altezza = float(input("Inserisci il valore dell'altezza "))
        perimetror=float(base*2+altezza*2)
        return perimetror, scelta
    elif scelta == 3:
        print("Hai selezionato la circonferenza del cerchio")
        raggio = float(input("Inserisci il valore del raggio: "))
        circonferenza=float(raggio*2*3.14)
        return circonferenza, scelta
    else:
        print("Digitare '1', '2' o '3'")
        return None

risultato, scelta = perimetro()

if risultato is not None:
    if scelta == 3:
        print("La circonferenza del cerchio è:", risultato)
    else:
        print("Il perimetro della figura è:", risultato)


          
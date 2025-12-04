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
        print(f"Il perimetro del quadrato, avente lato {lato} è: ", lato*4)
    elif scelta == 2:
        print("Hai selezionato il perimetro del rettangolo")
        base = float(input("Inserisci il valore della base: "))
        altezza = float(input("Inserisci il valore dell'altezza "))
        print (f"Il perimetro del rettangolo, avente base {base} e altezza {altezza} è: ", base*2 + altezza*2)
    elif scelta == 3:
        print("Hai selezionato la circonferenza del cerchio")
        raggio = float(input("Inserisci il valore del raggio: "))
        print(f"La circonferenza del cerchio, avente raggio {raggio} è: ", raggio*3.14)
    else:
        print("Digitare '1', '2' o '3'")

perimetro()
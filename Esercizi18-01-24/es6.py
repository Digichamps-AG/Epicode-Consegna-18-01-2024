# Scrivere una funzione che, data una lista di numeri, 
#fornisca in output i tre numeri più grandi; 
#gestire il caso in cui la lista sia più corta di tre, 
#e quando uno o più dei numeri selezionati sono uguali.

def numeriGrandi(lista):
    #creo una nuova lista dove mettere i valori unici
    nuovaLista = []

    #se la lista messa come argomento ha meno di 3 elementi
    if len(lista) < 3:
        print("La lista deve avere almeno 3 elementi!")
        #return None

    for numero in lista:
        if numero not in nuovaLista:
            nuovaLista.append(numero)
    nuovaLista.sort()
    nuovaLista.reverse()
    print(nuovaLista[0:3])
    return nuovaLista[0:3]


#esempio con lista corretta
print("Caso corretto:")
lista_numeri = [10, 10, 3, 25]
mieiNumeri = numeriGrandi(lista_numeri)


#esempio con lista errata
print("Caso errato:")
lista_numeri = [10, 10]
mieiNumeri = numeriGrandi(lista_numeri)

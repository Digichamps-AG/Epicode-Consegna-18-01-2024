# Scrivere una funzione che, data una lista di numeri, 
#fornisca in output i tre numeri più grandi; 
#gestire il caso in cui la lista sia più corta di tre, 
#e quando uno o più dei numeri selezionati sono uguali.



def numeriGrandi(lista):
    #creo una lista (listaOrdinata) che conterrà i valori ordinati in senso decrescente
    #sorted(lista) ordina "lista"; il parametro "reverse" è opzionale e di default è = False, cioè la lista è ordinata in ordine crescente
    #con sorted(lista, reverse = True) sto dicendo: Ordinami "lista" in senso decrescente (reverse=True)
    #la funzione set() prende solo i valori non ripetuti => ho creato una lista ordinata in senso decrescente senza valori ripetuti
    listaOrdinata = sorted(set(lista), reverse=True)

    #se la lunghezza della lista ordinata è <3 (cioè se ci sono meno di 3 elementi)
    if len(listaOrdinata)<3:
        #stampa questo
        print("La lista deve avere almeno 3 elementi!")
        print("E i valori ripetuti non contano!")
    
    #altrimenti stampa quest'altro
    else:
        print("I numeri più grandi sono i seguenti:")
        #qui stampo solo i primi 3 valori dalla listaOrdinata
        print(listaOrdinata[0:3])
    #infine restituisci questo valore
    #in questo modo l'utente si trova automaticamente stampato il risultato (con le print del blocco else)
    #ma se vuole può inserire il risultato della funzione in una variabile e saranno inseriti solo i 3 valori calcolati
    return listaOrdinata[0:3]



#esempio con lista corretta
print("Caso corretto:")
lista_numeri = [10, 10, 3, 25]
mieiNumeri = numeriGrandi(lista_numeri)


#esempio con lista errata
print("Caso errato:")
lista_numeri = [10, 10, 10, 25]
mieiNumeri = numeriGrandi(lista_numeri)
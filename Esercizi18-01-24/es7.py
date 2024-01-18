'''Scrivere una funzione che in input acquisisce una lista di numeri e un numero K; 
in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a K;
se non ce ne dovesse essere nessuno, dovrà stampare a schermo un messaggio adeguato.'''

'''def media_k (lista, k):
    listaMedia = []
    for numero in lista:
        if numero >= k:
            listaMedia.append(numero)
       
    return sum(listaMedia)/len(listaMedia)

lista = [1,2,3,4,5]
mia_media = media_k(lista, 6)
print(mia_media)'''


def media_k (lista, k):

    #creo una lista in cui mettere tutti i valori maggiori di k
    listaMedia = []
    #scorro fra tutti gli elementi della lista "lista" che l'utente inserisce come argomento
    for numero in lista:
        #se l'elemento della lista è >=k
        if numero >= k:
            #metti quell'elemento nella lista "listaMedia"
            listaMedia.append(numero)
    #esco dal for perchè non mi serve più scorrere
    #se listaMedia è vuota (not listaMedia), cioè se nessun valore della lista originale è stato messo lì
    # o in altri termini se nessun valore è >=k
    if not listaMedia:
        #ritorna questo messaggio
        return "Nessun valore è più grande di k!"          
    #ritorna la somma della listaMedia/la lunghezza della listaMedia (cioè la media dei valori >=k)
    return sum(listaMedia)/len(listaMedia)

print("Caso corretto:")
#esempio per testare la funzione
lista = [1,2,3,4,5]
mia_media = media_k(lista, 3)
print(mia_media)

print("Caso errato:")
#esempio di caso errato
lista = [1,2,3,4,5]
mia_media = media_k(lista, 6)
print(mia_media)


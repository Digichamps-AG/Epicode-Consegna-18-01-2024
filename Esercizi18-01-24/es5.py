# Scrivere una funzione che, data una lista di numeri, fornisca in output il minimo e il massimo 
#(possiamo usare o meno le funzioni min() e max() nel corpo).

#l'argomento sarà una lista immessa dall'utente
def min_max(lista):
    '''
    data una lista, restituisce il valore minimo, seguito da quello massimo
    '''
    #trova il minimo della lista fornita
    minimo = min(lista)
    #trova il massimo della lista fornita
    massimo = max(lista)
    #restituisce il minimo e il massimo appena calcolati, denrtro una lista
    #se non si mettono le quadre, essendo i valori separati da una virgola e basta, restituisce una tupla
    return [minimo, massimo]

#esempio: calcoliamo il minimo e il massimo in una lista di numeri da 1 a 10
lista_numeri = [0,1,2,3,4,5,6,7,8,9,10]

minimo_massimo = min_max(lista_numeri)
print(minimo_massimo)


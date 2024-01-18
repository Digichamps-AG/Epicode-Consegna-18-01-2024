'''Scrivere una funzione che, data una lista di numeri, come output stamperà lo stesso numero di asterischi su righe diverse,
ottenendo una semplice visualizzazione grafica 
Esempio, supponendo di chiamare la funzione "aster()":
numeri = [5, 2, 3, 4] aster(numeri) Output: ***** ** *** ****'''

def asterischi (lista):
    #scorre ogni elemento (numero) della lista inserita
    for numero in lista:
        #moltiplica ogni numero per la stringa "*" (moltiplicare le strighe significa ripeterle)
        print(numero * "*")

#esempio
miaLista = [0,1,2,3,10]

asterischi(miaLista)
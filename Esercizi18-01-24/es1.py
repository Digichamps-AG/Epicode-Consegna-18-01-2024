#Scegliere almeno 3 esercizi del giorno precedente e riscriverli con un ciclo for invece che while

#es1 Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while.
nome_scuola = "Epicode"

for elemento in nome_scuola:
    print(elemento)

#es2 Stampare a video tutti i numeri da 0 a 20
    
for x in range(0, 21):
    print(x)

#es3 Calcolare e stampare tutte le prime 10 potenze di 2
potenze = range(0,11)
base=2
for x in potenze:
    print(base**x)
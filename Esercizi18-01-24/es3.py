#Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

#Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto che non sono una Multipla.

for valore in auto.values():
    if valore != "Multipla":
        print(valore)
print()
print("Fatto capo!")


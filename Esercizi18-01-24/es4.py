#Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} 
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}

dizionario_auto.update(nuovi_proprietari)
print(dizionario_auto)

#Cosa è successo a Ben?
'''
visto che era presente in entrambi i dizionari,
con l'update il valore legato alla chiave "ben" 
si è aggiornato, prendendo il valore del secondo dizionario
(quello nella parentesi di update
)'''
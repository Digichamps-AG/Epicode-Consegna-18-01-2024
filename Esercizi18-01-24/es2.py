'''
Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo che: 
• Ada guida una Punto
 • Ben guida una Multipla
   • Charlie guida una Golf 
   • Debbie guida una 107 
   Stampiamo il dizionario per intero, e poi l'auto associata a Debbie.
'''

auto = {"Ada":"Punto", "Ben":"Multipla", "Charlie":"Golf", "Debbie": "107"}
print(auto)
print("L'auto di Debbie è: ", auto["Debbie"])
mio_dizionario={"mia_chiave1":"mio_valore1","eta":24,3.14:"pi_greco","primi":[1,2,3,5,7,9,13]} #costruito chiave valore
print(mio_dizionario[3.14])
mio_dizionario["nuova_chiave"] = "nuovo_valore" #inserisco la coppia chiave valore
print(mio_dizionario)

#voglio cambiare il valore alla chiave eta
mio_dizionario["eta"] = 99
print(mio_dizionario)

#dizionario elenco di valori non ordinati
#se avessimo un dizionario che ha le stesse coppie chiave e valori ma ordinati in maniera diversa
#cioe' eta 99 si trova all inizio, se comparassimo i due dizionari ci verrebbe come risultato True

if "zen" in mio_dizionario:
    print("OK")
else:
    print("NO")

#eliminare coppia valore
del mio_dizionario["mia_chiave1"]
print(mio_dizionario)

ita_eng= {"Ciao":"hello","arriverci": "goodbye", "uova":"eggs","gatto":"cat"}
#ottenere lista di tutte le chiavi presenti
print(ita_eng.keys())
#ottenere lista di tutti i valori presenti
print(ita_eng.values())
#ottnere una lista di tutte le coppie chiave-valore presente nel dizionario
print(ita_eng.items())

parole_eng=list(ita_eng.values())
print(parole_eng)

for chiave in ita_eng.keys():
    print(chiave)
#gestire in maniera blanda qualora non ci sia una chiave nel dizionario
if "birra" in ita_eng.keys():
    print(ita_eng["birra"])
else:
    print("Chiave non trovata!")
#posso scrivere la stessa cosa usando il metodo get specifico per i dizionari
print(ita_eng.get("birra","Chiave non trovata!!"))
#in questo caso mi restituisce il valore associato alla chiave Ciao
print(ita_eng.get("Ciao","Chiave non trovata!!"))
#inserisco un nuovo valore dentro il dizionario la nuova coppia birra beer
ita_eng.setdefault("birra","beer")
print(ita_eng.get("birra","Chiave non trovata!!"))


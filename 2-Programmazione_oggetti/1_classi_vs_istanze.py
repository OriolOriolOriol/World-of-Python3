class Studente:
    """ 
    ore_settimanali è una variabile di classe quindi condivisa da tutte le istanze. Può essere utile quando ad esempio vogliamo che tutte le 
    istanza condividano le stesse cose ad esempio per concludere la triennale ci vogliono 180 crediti. tuttavia prendendo questa variabile, 
    se consideriamo che tutti gli studenti mediamente frequentano 36 ore alla settimana, tuttavia studente uno(quindi un particolare studente)
    fa anche una scuola serale, bhe in questo caso sarebbe meglio mettere nella scheda personale self.ore_settimanali invece che Studente.ore_settimanali
    """
    ore_settimanali= 36 #variabile condivissa da tutte le istanze
    corpo_studentesco= 0# variabile di classe perche' non raprresenta una caratteristica intrinseca di una specifica istanza di classe
    #metodo inizializzatore. Permette di creare e memorizzare le varie istanza create. Fondamentale. senza esso le istanza non ci sarebbero

    def __init__(self,nome,cognome,corso_di_studi):#istanza di ogni signolo oggetto della classe self. Rappresenta una referenza per ogni oggetto della classe
        self.nome=nome
        self.cognome=cognome
        self.corso_di_studi=corso_di_studi
        Studente.corpo_studentesco += 1
        """nome cognome corso di studi sono variabili d'istanza. self rappresenta una referenza per ogni istanza della classe  """
    
    #stampo in maniera corretta le varie istanza usando questo metodo
    def scheda_personale(self):
        return f"Scheda Studente:\nNome: {self.nome}\nCognome: {self.cognome}\nCorso di studi: {self.corso_di_studi}\nOre settimanali: {Studente.ore_settimanali}"
    

studente_uno = Studente("Claudio","Rimensi","Informatica")
studente_due= Studente("Giulio","Beltrami","Ingegneria Meccanica")


print(studente_uno)
print(studente_due)


studente_uno.ore_settimanali += 4
print(studente_uno.scheda_personale())#***
print(studente_due.scheda_personale())
print("Numero studenti: " + str(Studente.corpo_studentesco)) #per ogni studente aggiunto faccio un contatore
#print(Studente.scheda_personale(studente_uno))#e' uguale a questo ***

#print(Studente.__dict__)
#print(studente_uno.__dict__)

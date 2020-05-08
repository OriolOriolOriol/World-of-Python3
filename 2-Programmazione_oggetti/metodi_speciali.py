class Studente:
 
    def __init__(self,nome,cognome,corso_di_studi):#istanza di ogni signolo oggetto della classe self. Rappresenta una referenza per ogni oggetto della classe
        self.nome=nome
        self.cognome=cognome
        self.corso_di_studi=corso_di_studi
    
    #stampo in maniera corretta le varie istanza usando questo metodo
    def scheda_personale(self):
        return f"Scheda Studente:\nNome: {self.nome}\nCognome: {self.cognome}\nCorso di studi: {self.corso_di_studi}"
    
    def __add__(self,other):
        """Solo per fini didattici usare io dunder in maniera intelligente!!!"""

        return self.nome + " " + other.cognome

    def __str__(self):
        """Rappresentaizone leggibile-per pubblico"""
        return f"Lo studente {self.nome} {self.cognome}"

    def __repr__(self):
        """Rappresentazione non ambigua per sviluppatori"""
        return f"Studente('{self.nome}'', '{self.cognome}','{self.corso_di_studi}')"
 
studente_uno= Studente("Claudio","Rimensi","Informatica")
studente_due=Studente("Giulio","Beltrami","Ingegneria")

#print(studente_uno + studente_due) #puoi usarlo perche' ce' il metodo speciale dunder __add__
#print(studente_uno)
#print(str(studente_due))#creiamo un metodo speciale str che un metodo dunder, non creato per noi
#print(studente_due + studente_uno)
print(Studente.__str__(studente_uno))
#questi due metodi sono uguali.Scegli quello che vuoi
print(Studente.__repr__(studente_due))
print(studente_due.__repr__())
#print(repr(studente_due))
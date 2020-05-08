class Persona:

    def __init__(self,nome,cognome,eta,residenza):
        self.nome= nome
        self.cognome= cognome
        self.eta = eta
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Eta: {self.eta}
        Residenza: {self.residenza}\n"""

        return scheda

    def modifica_scheda(self):
        print("""Modifica scheda:
        1- Nome
        2-Cognome
        3- Eta
        4-Residenza""")

        scelta= input("Cosa desideri modificare? ")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        
        if scelta == "2":
            self.cognome = input("Nuovo Cognome --> ")

        if scelta == "3":
            self.eta = input("Nuova eta --> ")

        if scelta == "4":
            self.residenza = input("Nuovo Residenza --> ")


class Studente(Persona):
    profilo = "Studente"
    #python va a vedere se e' presente un metodo costruttore
    def __init__(self,nome,cognome,eta,residenza,corso_di_studio):
        super().__init__(nome,cognome,eta,residenza)#prendeo quello che c'e' scritto in Persona grazie alla funzione super()
        self.corso_di_studio=corso_di_studio

    def scheda_personale(self):
        scheda= f"""
        Profilo:{Studente.profilo}
        Corso di studio: {self.corso_di_studio}"""
        return super().scheda_personale() + scheda


    def cambio_corso(self,corso):
        self.corso_di_studio=corso
        print("\nCorso aggiornato!!\n")


class Insegnante(Persona):
    profilo= "Insegnante"

    def __init__(self,nome,cognome,eta,residenza,materia=None):
        super().__init__(nome,cognome,eta,residenza)#prendeo quello che c'e' scritto in Persona grazie alla funzione super()
        if materia is None:
            self.materia=[]
        else:
            self.materia=materia

    def scheda_personale(self):
        scheda= f"""
        Profilo:{Insegnante.profilo}
        Elenco delle materie: {self.materia}"""
        return super().scheda_personale() + scheda


    def aggiungi_materia(self,nuova):
        if nuova not in self.materia:
            self.materia.append(nuova)
        print("\nElenco materie aggiornato!!\n")

if __name__ == "__main__":
    #Grazie all ereditarieta' le sottocalssi studente e insegnante hanno ereditato dalla classe genitore Persona tutto quello che ha e quindi anche
    #senza scrivere niente siamo riusciti ad ottenere le cose
    studente_uno=Studente("Claudio","Rimensi","24","Ferrara","Informatica")
    insegnante_uno=Insegnante("Mario","Rossi","40","Padova",["Python","C","Security"])
    print("*******************************")
    print(studente_uno.scheda_personale())
    print("*******************************")
    print(insegnante_uno.scheda_personale())
    print("*******************************")
    insegnante_uno.aggiungi_materia("Filosofia")
    print("*******************************")
    print(insegnante_uno.scheda_personale())
    studente_uno.cambio_corso("Sociologia")
    print("*******************************")
    print(studente_uno.scheda_personale())
    #print(help(Studente))#utile per studiare le classi
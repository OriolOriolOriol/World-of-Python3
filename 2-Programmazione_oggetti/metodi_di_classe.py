class Persona:


    def __init__(self,nome,cognome,eta,residenza):
        self.nome= nome
        self.cognome= cognome
        self.eta = eta
        self.residenza = residenza

    #i metodi di classe sono legati alla classe e non alle istanze
    @classmethod #decoratore per creare metodi di classe
    def from_string(cls,stringa_persona,*args):#*args rappresenta che possono esserci altri paramteri che ci sono da altre sottoclassi
        nome,cognome,eta,residenza = stringa_persona.split("-")
        return cls(nome,cognome,eta,residenza,*args)

    @classmethod
    def occupazione(cls):
        if cls.__name__=="Studente":
            return "Studente"
        else:
            return "Insegnante"

    #sono metodi che ueslano dal programma e che danno informazioni magari sull autore
    @staticmethod
    def info_prog():
        info="""
        Nome= Persona
        Creato da: Claudio Rimensi
        Sito ufficiale: www.nonesiste.com"""

        return info

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
    #non ho scritto una singola istanza particolare ma una stringa. va gestita con un metodo della classe
    iron_man="Tony-Stark-40-Torre Stark"
    zuck="mark-Zuckemberg-33-California"
    #persona1=Persona.from_string(iron_man)
    #print(persona1.scheda_personale())
    insegnante1=Insegnante.from_string(iron_man,"Ingegneria")
    studente1=Studente.from_string(zuck,"SEO")

   # print(insegnante1.scheda_personale())
    #print(studente1.scheda_personale())

    print(insegnante1.occupazione())
    print(studente1.occupazione())

    print(Persona.info_prog())




   
import os

os.chdir("C:\\Users\\claud\\Desktop")
#print(os.listdir(os.getcwd()))

for cartella,sottocartelle, files in os.walk(os.getcwd()):#os.walk crea un albero di tutte le cartelle sottocartelle e files del percorso scelto.Lavora con il ciclo for
    #print(f"1) Ci troviamo nella cartella: {cartella}")
    #print(f"2) Le sotto-cartelle presenti sono: {sottocartelle}")
    #print(f"3) I files sono: {files}")
    #voglio cercare solo una tipologia di files non mostrando altro
    for file in files:
        if file.endswith(".py"):
            print(f"3) {file}")
    #print() #serve per disintguere i file e fare in modo di capire che un file appartiene ad una cartella e un altro file ad un altra cartella
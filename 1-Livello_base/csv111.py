import csv,os

os.chdir("C:\\Users\\claud\\Desktop\\Python3.6")
with open("excel_prova.csv",newline="",encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=";")
    #print(lettore)
    #header= next(lettore)
    #print(header)#facendo cosi' mostro le colonne del mio file csv
    dati= [(riga[1],riga[2]) for riga in lettore if riga[1] == "LIVORNO" ]
    """ 
    # mi creo una sottolista da una lista grande
    dati e' composto da:

    (coppia) = sono i risultati
     poi hai un ciclo che presenta ogni singola riga del file csv presente in lettore che e' tutto il file. se riga[1] presenta LIVORNO
     mi stampi il comune quindi LIVORNO e l'etichetta
    
    """
    print(dati)
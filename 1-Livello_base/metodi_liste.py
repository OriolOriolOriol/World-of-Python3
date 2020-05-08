""" inventario=["torcia","spada","pane","arco"]
inventario.append("freccia")
print(inventario)


def riempi_inventario():
    inventario=[]
    while True:                   #ciclo infinito
        oggetto=input("Cosa vuoi aggiungere?(exit): ")
        if oggetto == "exit":
            break
        else:
            inventario.append(oggetto)
    return(inventario)

lista1=riempi_inventario()

print("Lista iniziale: " + str(lista1))

def rimuovi_elemento(lista1):
    print(lista1)
    for elemento in lista1:
        if elemento == "sei":
            lista1.remove(elemento) #remove non ritorna alcun valore. Quindi non si scrive lista1= lista1.remove(elemento)
            print(lista1)
            break
        

    return(lista1)

lista_finale=rimuovi_elemento(lista1) """

#lista.index(elemento) ---> ritorna l'inddice dell elemento

numeri=[1,2,4,5645,23,6,34,12]
numeri.sort(reverse=True) #come per remove o insert non restituisce niente, quindi numeri=numeri.sort() e' sbagliato
print(numeri)
print(numeri.index(2))# questo invece restituisce qualcosa.

feste=["capodanno","ferragosto","natale"]
feste.insert(1,"carnevale")#lo metto all' indice 1 della lista
print(feste)
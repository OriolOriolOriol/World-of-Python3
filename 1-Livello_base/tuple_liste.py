elenco = [2,5,"bacon",3.14,"eggs"]
#scrivi -1 accedi alla lista nell'ordine inverso
print(elenco[-1])

primi=[2,3,5,7,11,13,17,19,23,29]
print(primi[3:8])
print(primi[4:])
print(primi[:5])

numero = int(0)
for numero in range(5):
    print(numero)

print("\n***************************\n")
for primo in primi:
    print(primo)

#oltre al modo tradizionale [] le liste sono richiamate anche con la keyword list
lista_numerica = list(range(99,300))
print(lista_numerica)

lista_multipla =["spam","eggs",23,"bacon",[1,2,23,3],3]
#la prima [] rappresenta identificare la sottolista nella lista principale. Il secondo [] identifica un elemento della sottolista.
print(lista_multipla[-2][-1])
lista_multipla[3]="pancetta"
#elimino un elemento della lista principale
del lista_multipla[-2]
print(lista_multipla)


###################################
tuple1=(2,4,9,15,23)
tuple2=2,3,4
print(tuple1[1])
print(tuple2)
#con le tuple rispetto alle liste gli elementi non si possono modificare
#usare le tuple rispetto ad una lista quando l'elenco e' immutabile. L'iterazione di un tuple e' piu' veloce che in una lista.

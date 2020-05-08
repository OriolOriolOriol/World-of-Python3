spam="La pratica "
eggs="rende perfetti"
print(spam + eggs)
print(spam*3)
a=[1,2,"tre"]
b=[4,5,"sei"]
print(a + b)
print(a*3)

print(len(spam))
print(len(a))

#si può accedere a liste e stringhe senza problemi
alfa="abcdefghijlkmnopi"
#usa gli indici della stringa per ottenere il reverse. indice è 16 e ogni volta che decrementi prendi l'elemento corrispondente all'indice.
#Esempio: in sedici c'e' i in 15 c'e' p e cosi via..
def reverser(stringa):
    nuova_stringa =""
    indice=(len(stringa) -1)#perche' il primo elemento parte da 0
    while indice >=0:
        nuova_stringa= nuova_stringa + stringa[indice]
        indice = indice -1

    print("Stringa reversata: " + nuova_stringa)


reverser(alfa)

#conversione string to list
lista= list(alfa)
print(lista)
x = int(15)

def funzione_esempio():
    #prendo la variabile globale x
    #se non scrivessi global x ma solo x python creerebbe una variabile locale per la funzione funzione_esempio() che è differente dalla x iniziale
    global x
    #x = int(0)
    x +=2
    return (x)


def fun1():
    y=x
    y +=2
    return(y)

print(fun1())
print(funzione_esempio())

#se al posto di return avessi scritto print e poi in eggs avessi scritto spam invece che fun2(), mi avrebbe dato errore
#ricorda che ogni funzione ha una sua scatola con le propri3e variabili, e le variabili globali sono in un altra scatola.
#le puoi richiamare scrivendo global
def fun2():
    spam =24
    return(spam)

eggs= fun2() + 6
print(eggs)
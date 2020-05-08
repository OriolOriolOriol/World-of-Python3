nome="Claudio"
print("Ciao " + nome)
numero=18
#migliorare la concatenazione di stringhe. Si chiama formetted string liberals
print(f"Ciao{nome},questa e' la lezione n{numero}!Benvenuto")
saluto=f"Ciao{nome},questa e' la lezione n{numero}!Benvenuto"

z = 5
print(f"il quadrato di {z} e' {z*z}")

messaggio = "Fate il vostro gioco"
#questi due metodi restituiscono valori booleani. 
print(messaggio.startswith("f"))
print(messaggio.endswith("gioco"))

#restituiscono valori booleani
nome="alice"
print(nome.isupper()) #tutte le lettere sono maiuscole
print(nome.islower()) #tutte le lettere sono minuscole
print(nome.upper)#rende tutte maiuscole le lettere
print(nome.lower())#rende tutte minuscole le lettere
print(nome.isalpha())#controlla se una stringa e' composta solo da lettere. se avessi aggiunto uno spazio avrebbe dato false. solo LETTERE!!!
print(nome.isdecimal())#controlla se le stringhe sono composte solo da numeri
print(nome.isalnum())#per dire se una stringa e' composta sia da caratteri che da numeri non simboli
print(nome.isspace())#per dire se c'e uno spazio dentro la stringa. Naturalmente restituisce true o false

compiti= ["ciao","come va","tutto bene","io sto bene", "ottimo sono contento"]
#metodo join(da lista a stringa)
stringa = ", ".join(compiti)#unisce i vari valori della lista con join per formare una stringa
print(stringa)
fare="\n".join(compiti)
print(fare)
#metodo split(da stringa a lista)
serie_numerica="1492-1984-1233331-555"
print(serie_numerica.split("-"))

import os

contenuto = "Oggi e' una bellissima giornata!"
#scrivere
file1= open("C:\\Users\\claud\\Desktop\\esempio1.txt","w")
file1.write(contenuto)
file1.close()

#append
nuova="python e' una bomba"
file1= open("C:\\Users\\claud\\Desktop\\esempio1.txt","a")
file1.write(nuova)
file1.close()

#nuova riga
file1= open("C:\\Users\\claud\\Desktop\\esempio1.txt","a")
file1.write("\nNuovariga")
file1.close()

#leggere
var_lettura= open("C:\\Users\\claud\\Desktop\\esempio1.txt","r").readlines() #con readlines creiamo una lista tanto quando sono le righe nel file
print(var_lettura)
print(os.getcwd())
os.chdir("C:\\Users\\claud\\Desktop")
print(os.getcwd())#come vedi siamo cambiati
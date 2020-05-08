import os,shutil

""" print(os.getcwd())
print(os.listdir())
os.chdir("C:\\Users\\claud\\Desktop")#cambi il percorso della cartella dentro al programma e lui sa dove andare
print(os.getcwd())
try:
    os.makedirs("nuova")#creazione di una nuova cartella
except FileExistsError:
    pass

try:
    os.rename("nuova","lezione21")

except FileExistsError:
    pass

print(os.listdir()) """
shutil.copytree("C:\\Users\\claud\\Desktop\\lezione21","C:\\Users\\claud\\Desktop\\Python3.6\\lezione21copia")#copia cartelle e sotto-cartelle
shutil.rmtree("C:\\Users\\claud\\Desktop\\lezione21")
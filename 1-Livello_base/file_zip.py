import os, zipfile

os.chdir("C:\\Users\\claud\\Desktop")
""" #creazione archivio zip
archivio = zipfile.ZipFile("C:\\Users\\claud\\Desktop\\archivio.zip","w")#w oppure a
print(os.getcwd())
archivio.write("CV.pdf",compress_type=zipfile.ZIP_DEFLATED) # inseriamo il file dentro all archivio zip usando l algoritmo zipdeflated
archivio.close() """

#estrazione di un conteuto zip
archivio = zipfile.ZipFile("C:\\Users\\claud\\Desktop\\archivio.zip")
#archivio.extractall("C:\\Users\\claud\\Desktop\\cartella_estrazione")#estrazione di tutti i file
#archivio.extract("CV.txt","C:\\Users\\claud\\Desktop\\cartella_estrazione")#estrazione solo di un file
archivio.namelist()#lista del contenuto di un archivio
text_info= archivio.getinfo("CV.pdf")
print(text_info.file_size)#dimensione file CV presente dentro l'archivio
print(text_info.compress_size)#dimensione file CV presente dentro l'archivio zippato
archivio.close()